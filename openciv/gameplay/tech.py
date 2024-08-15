from typing import List, Generator, Tuple, Any
from openciv.engine.managers.i18n import T_TranslationOrStr


class Tech:
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr = None,
        description: T_TranslationOrStr = None,
        icon: T_TranslationOrStr = None,
        requires: List["Tech"] = None,
        contributes_to: List["Tech"] = None,
        tech_points_required: int = 1,
        age: "Age" = None,  # noqa F821
        color: Tuple[int, int, int, int] = None,
    ):
        self.key = key

        self.name: T_TranslationOrStr = name if name is not None else _t(f"tech.{key}.name")
        self.description: T_TranslationOrStr = description if description is not None else _t(f"tech.{key}.description")
        self.icon: T_TranslationOrStr = description if description is not None else _t(f"tech.{key}.description")
        self.color = color

        self.requires = requires if requires is not None else []
        self.contributes_to = contributes_to if contributes_to is not None else []
        self.completed = False
        self.tech_points_required: int = tech_points_required

        # Age is not really meant to be set inside this object its suppose to be given by the tech tree object.
        # so for proper usage, it should be set by the tech tree object.
        self.age: "Age" = age  # noqa F821

    def __repr__(self, recursive: bool = False):
        contributes_to = [tech.__repr__(recursive=recursive) for tech in self.contributes_to]
        contributes_to = f"[{'}, {'.join(contributes_to)}]"
        return f"{self.name}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Tech):
            return self.name == other.name
        return False


class TechTree:
    def __init__(self, name: T_TranslationOrStr, description: T_TranslationOrStr, icon: T_TranslationOrStr = None):
        self._items: List[Tech] = []
        self._ages: List["Age"] = []  # noqa F821

        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.icon: T_TranslationOrStr = icon

    def items(self) -> Generator[Tech, None, None]:
        for item in self._items:
            yield item

    def add(self, item: Tech) -> None:
        self._items.append(item)

    def render(self):
        self.render_graph(self._items, "TechTreeDump")

    def add_age(self, age: "Age") -> None:  # noqa F821 (forwardlookup)
        self._ages.append(age)

    @classmethod
    def render_graph(cls, techs: List[Tech], filename: str = "tech_tree"):
        from graphviz import Digraph

        dot = Digraph(comment="Tech Tree")

        # Add nodes
        for tech in techs:
            color = "white" if tech.age.color is None else cls.convert_rgba_to_color_name(tech.age.color)
            dot.node(
                str(tech.name),
                f"{str(tech.name)} ({'Completed' if tech.completed else 'Incomplete'})",
                shape="rectangle",
                fillcolor=f"{color}",
            )

        # Add edges
        for tech in techs:
            for req in tech.requires:
                dot.edge(str(req.name), str(tech.name), label="requires")

        dot.render(filename, view=True)

    @classmethod
    def closest_color(cls, requested_color: tuple) -> str:
        import webcolors

        min_colors = {}
        for key, name in webcolors.CSS3_NAMES_TO_HEX.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(name)
            rd = (r_c - requested_color[0]) ** 2
            gd = (g_c - requested_color[1]) ** 2
            bd = (b_c - requested_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]

    @classmethod
    def convert_rgba_to_color_name(cls, rgba: tuple[Any]) -> str:
        import webcolors

        if rgba.__len__() == 4:
            rgb = rgba[:3]  # Ignore the alpha channel for color matching
        else:
            rgb = rgba
        try:
            # Get the closest color name directly
            closest_name = webcolors.rgb_to_name(rgb)
        except ValueError:
            # Find the closest color name using the colormath library
            closest_name = cls.closest_color(rgb)
        return closest_name


if __name__ == "__main__":
    # Example usage:
    tech1 = Tech("Tech1")
    tech2 = Tech("Tech2", requires=[tech1])
    tech3 = Tech("Tech3", requires=[tech1])
    tech4 = Tech("Tech4", requires=[tech2, tech3])
    tech5 = Tech("Tech5", requires=[tech4])

    all_techs = [tech1, tech2, tech3, tech4, tech5]
