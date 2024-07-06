import json
import pytest
from glob import glob
from typing import Dict, Any

# Define the expected structure for the 'leaders' block
expected_leader_structure = {
    "name": str,
    "description": str,
}

# Define the expected structure for different blocks
expected_structure = {
    "world": {"terrain": dict},
    "tiles": {"resources": dict},
    "civilization": {
        "name": str,
        "description": str,
        "leaders": dict,  # Simplified to just check if leaders is a dictionary
    },
    "tech": {"name": str, "description": str},
    "content": {
        "tech": {
            "trees": dict  # Simplified to just check if trees is a dictionary
        },
        "ages": dict,  # Simplified to just check if ages is a dictionary
    },
}

_data = {}


# Fixture to load JSON data
@pytest.fixture
def load_language_data() -> Dict[str, Any]:
    from copy import deepcopy

    global _data
    if _data == {}:
        for file in glob("openciv/i18n/*.json"):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for language, content in data.items():
                    _data[language] = deepcopy(content)
    return _data


# General function to check the structure of blocks
def check_block_structure(block: Dict[str, Any], structure: Dict[str, Any]) -> None:
    for key, value in structure.items():
        assert key in block, f"Missing key: {key}"
        if isinstance(value, dict):
            assert isinstance(block[key], dict), f"Key '{key}' should be a dictionary"
            check_block_structure(block[key], value)
        elif isinstance(value, list):
            assert isinstance(block[key], list), f"Key '{key}' should be a list"
            if value:
                for item in block[key]:
                    check_block_structure(item, value[0])
        else:
            assert isinstance(block[key], value), f"Key '{key}' should be of type {value.__name__}"


# Helper function to handle nested dictionaries with variable keys
def check_nested_block_structure(block: Any, structure: Any) -> None:
    if isinstance(structure, dict):
        for key, sub_structure in structure.items():
            assert key in block, f"Missing key: {key}"
            check_nested_block_structure(block[key], sub_structure)
    else:
        assert isinstance(block, structure), f"Block should be of type {structure.__name__}"


# Test for the top-level keys
def test_top_level_keys(load_language_data: Dict[str, Any]) -> None:
    for language in load_language_data.keys():
        assert language in load_language_data, f"Key '{language}' not found in top level keys"


# Test the structure of the 'world' block
def test_world_structure(load_language_data: Dict[str, Any]) -> None:
    for language, data in load_language_data.items():
        world = data["world"]
        check_block_structure(world, expected_structure["world"])


# Test the structure of the 'tiles' block
def test_tiles_structure(load_language_data: Dict[str, Any]) -> None:
    for language, data in load_language_data.items():
        tiles = data["tiles"]
        check_block_structure(tiles, expected_structure["tiles"])


# Test the structure of the 'civilization' block
def test_civilization_structure(load_language_data: Dict[str, Any]) -> None:
    for language, data in load_language_data.items():
        civilizations = data["civilization"]
        for civ in civilizations.values():
            check_block_structure(civ, expected_structure["civilization"])


# Test the structure of the 'leaders' block within each civilization
def test_leaders_structure(load_language_data: Dict[str, Any]) -> None:
    for language, data in load_language_data.items():
        civilizations = data["civilization"]
        for civ in civilizations.values():
            for leader in civ["leaders"].values():
                check_block_structure(leader, expected_leader_structure)


# Test the structure of the 'tech' block
def test_tech_structure(load_language_data: Dict[str, Any]) -> None:
    for language, data in load_language_data.items():
        tech = data["tech"]
        for tech_item in tech.values():
            check_block_structure(tech_item, expected_structure["tech"])


# Test the structure of the 'content' block
def test_content_structure(load_language_data: Dict[str, Any]) -> None:
    for language, data in load_language_data.items():
        content = data["content"]
        for key in expected_structure["content"].keys():
            check_nested_block_structure(content[key], expected_structure["content"][key])
