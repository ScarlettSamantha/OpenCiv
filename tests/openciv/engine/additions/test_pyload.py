from __future__ import annotations
import pytest
from openciv.engine.additions.pyload import PyLoad
from tests.resources.test_objects.generics import GenericBase


@pytest.fixture
def setup_test_dir():
    return "tests/resources/test_objects/"


def test_load_classes_by_name_pattern(setup_test_dir):
    classes = PyLoad.load_classes(directory=setup_test_dir, name_pattern="generic*.py")
    compare = list(classes.keys())
    assert "GenericExtend" in compare
    assert "NoneExistantTestClass" not in compare
    assert "GenericPropertyExtend" in compare


def test_load_classes_with_directory_list(setup_test_dir):
    classes = PyLoad.load_classes(directory=[setup_test_dir], name_pattern="generic*.py")
    compare = list(classes.keys())
    assert "GenericExtend" in compare
    assert "NoneExistantTestClass" not in compare
    assert "GenericPropertyExtend" in compare


def test_load_classes_by_base_class(setup_test_dir):
    classes = PyLoad.load_classes(directory=setup_test_dir, base_classes=GenericBase)
    compare = list(classes.keys())
    assert "GenericExtend" in compare
    assert "NoneExistantTestClass" not in compare
    assert "GenericPropertyExtend" in compare


def test_load_classes_by_properties(setup_test_dir):
    classes = PyLoad.load_classes(directory=setup_test_dir)
    compare = list(classes.keys())
    assert "GenericExtend" in compare
    assert "NoneExistantTestClass" not in compare
    assert "GenericPropertyExtend" in compare


def test_load_classes_by_base_class_and_properties(setup_test_dir):
    classes = PyLoad.load_classes(directory=setup_test_dir, base_classes=GenericBase)
    compare = list(classes.keys())
    assert "GenericExtend" in compare
    assert "NoneExistantTestClass" not in compare
    assert "GenericPropertyExtend" in compare


if __name__ == "__main__":
    test_load_classes_by_name_pattern("tests/resources/test_objects/")
    test_load_classes_with_directory_list("tests/resources/test_objects/")
    test_load_classes_by_base_class("tests/resources/test_objects/")
    test_load_classes_by_properties("tests/resources/test_objects/")
    test_load_classes_by_base_class_and_properties("tests/resources/test_objects/")
