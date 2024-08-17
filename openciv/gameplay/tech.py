from __future__ import annotations

from typing import List, Generator, Tuple, Any
from openciv.engine.managers.i18n import T_TranslationOrStr, t_
from openciv.gameplay.age import Age


class Tech:
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr | None = None,
        description: T_TranslationOrStr | None = None,
        icon: T_TranslationOrStr | None = None,
        requires: List["Tech"] | None = None,
        contributes_to: List["Tech"] | None = None,
        tech_points_required: int = 1,
        age: Age | None = None,
        color: Tuple[int, int, int, int] | None = None,
    ) -> None:
        self.key: str = key

        self.name: T_TranslationOrStr | None = name if name is not None else t_(f"tech.{key}.name")
        self.description: T_TranslationOrStr | None = (
            description if description is not None else t_(f"tech.{key}.description")
        )
        self.icon: T_TranslationOrStr | None = description if description is not None else t_(f"tech.{key}.description")
        self.color: Tuple[int, int, int, int] | None = color

        self.requires: List[Tech] = requires if requires is not None else []
        self.contributes_to: List[Tech] = contributes_to if contributes_to is not None else []
        self.completed = False
        self.tech_points_required: int = tech_points_required

        # Age is not really meant to be set inside this object its suppose to be given by the tech tree object.
        # so for proper usage, it should be set by the tech tree object.
        self.age: Age | None = age

    def __repr__(self, recursive: bool = False):
        contributes_to = [tech.__repr__(recursive=recursive) for tech in self.contributes_to]
        contributes_to = f"[{'}, {'.join(contributes_to)}]"
        return f"{self.name}"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Tech):
            return self.name == other.name
        return False


class TechTree:
    def __init__(
        self, name: T_TranslationOrStr, description: T_TranslationOrStr, icon: T_TranslationOrStr | None = None
    ) -> None:
        self._items: List[Tech] = []
        self._ages: List[Age] = []  # noqa F821

        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.icon: T_TranslationOrStr | None = icon

    def items(self) -> Generator[Tech, None, None]:
        for item in self._items:
            yield item

    def add(self, item: Tech) -> None:
        self._items.append(item)

    def render(self) -> None:
        self.render_graph(techs=self._items, filename="TechTreeDump")

    def add_age(self, age: Age) -> None:
        self._ages.append(age)

    @classmethod
    def render_graph(cls, techs: List[Tech], filename: str = "tech_tree") -> None:
        from graphviz import Digraph

        dot = Digraph(comment="Tech Tree")

        # Add nodes
        for tech in techs:
            color = (
                "white"
                if tech.age is None or tech.age.color is None
                else cls.convert_rgba_to_color_name(tech.age.color)
            )
            dot.node(  # type: ignore
                name=str(tech.name),
                label=f"{str(tech.name)} ({'Completed' if tech.completed else 'Incomplete'})",
                shape="rectangle",
                fillcolor=f"{color}",
            )

        # Add edges
        for tech in techs:
            for req in tech.requires:
                dot.edge(tail_name=str(req.name), head_name=str(tech.name), label="requires")  # type: ignore

        dot.render(filename=filename, view=True)  # type: ignore

    @classmethod
    def closest_color(cls, requested_color: tuple[int, int, int, int]) -> str:
        import webcolors

        min_colors = {}
        for key, name in webcolors.CSS3_NAMES_TO_HEX.items():  # type: ignore
            r_c, g_c, b_c = webcolors.hex_to_rgb(name)  # type: ignore
            rd: int = (r_c - requested_color[0]) ** 2
            gd: int = (g_c - requested_color[1]) ** 2
            bd: int = (b_c - requested_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]  # type: ignore

    @classmethod
    def convert_rgba_to_color_name(cls, rgba: tuple[int, int, int, int]) -> str:
        import webcolors

        if rgba.__len__() == 4:
            rgb: Tuple[int, int, int] = rgba[:3]  # type: ignore # Ignore the alpha channel for color matching
        else:
            rgb: Tuple[int, int, int, int] = rgba
        try:
            # Get the closest color name directly
            closest_name = webcolors.rgb_to_name(rgb)  # type: ignore , This is a known issue with the library. It works.
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
