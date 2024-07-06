import os
import ast
import fnmatch
import importlib.util
from typing import Dict, Type, List, Union, Tuple
from openciv.engine.managers.log import LogManager


class GenericClassVisitor(ast.NodeVisitor):
    def __init__(self, base_classes: Union[Type, List[Type]] = None, properties: List[Tuple[str, str]] = None):
        self.subclasses = []
        self.base_classes = base_classes if isinstance(base_classes, list) else [base_classes]
        self.properties = properties or []

    def visit_ClassDef(self, node: ast.ClassDef):
        self.subclasses.append(node.name)
        self.generic_visit(node)

    def _is_base_class(self, base_class, base_node):
        if base_class is None:
            return False
        if isinstance(base_node, ast.Name):
            return base_class.__name__ == base_node.id
        elif isinstance(base_node, ast.Attribute):
            return base_class.__name__ == base_node.attr
        return False


class PyLoad:
    @staticmethod
    def load_classes(
        directory: str,
        name_pattern: str = "*.py",
        base_classes: Union[Type, List[Type]] = None,
        properties: List[Tuple[str, str]] = None,
    ) -> Dict[str, Type]:
        """
        Loads and returns classes from Python files in the given directory based on the provided criteria.

        :param directory: Directory to search for Python files.
        :param name_pattern: File name pattern to match Python files.
        :param base_classes: Base class or list of base classes to match subclasses.
        :param properties: List of tuples containing class property names and values to match.
        :return: Dictionary of class names and their corresponding types.
        """
        loaded_classes = {}
        for root, _, files in os.walk(directory):
            for file in files:
                if fnmatch.fnmatch(file, name_pattern):
                    file_path = os.path.join(root, file)
                    LogManager._get_instance().engine.debug(f"Processing file: {file_path}")  # Debug statement
                    with open(file_path, "r") as f:
                        file_content = f.read()
                        try:
                            tree = ast.parse(file_content)
                            visitor = GenericClassVisitor(base_classes=base_classes, properties=properties)
                            visitor.visit(tree)
                            for class_name in visitor.subclasses:
                                LogManager._get_instance().engine.debug(f"Found class: {class_name}")  # Debug statement
                                module_name = os.path.splitext(os.path.basename(file_path))[0]
                                spec = importlib.util.spec_from_file_location(module_name, file_path)
                                module = importlib.util.module_from_spec(spec)
                                spec.loader.exec_module(module)
                                loaded_classes[class_name] = getattr(module, class_name)
                        except SyntaxError as e:
                            LogManager._get_instance().engine.debug(f"Skipping {file_path} due to syntax error: {e}")
        return loaded_classes
