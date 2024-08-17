import pytest
import pathlib
from pathlib import Path
from unittest.mock import patch, mock_open

from openciv.engine.exceptions.i18n_exception import (
    I18NLoadException,
    I18NDecodeException,
    I18NTranslationNotFound,
    I18NNotLoadedException,
)

from openciv.engine.managers.i18n import Translation, set_i18n, _i18n  # type: ignore


def _objects(file: str = "") -> str:
    if file != "":
        file = f"/{file}"
    return str(object=(Path(__file__).resolve().parent / f"../../../resources/test_objects{file}").resolve())


def _i18n_instance() -> _i18n:
    return _i18n(base_path=_objects(), language="en_EN")


def test_i18n_initialization():
    i18n_instance: _i18n = _i18n_instance()
    assert i18n_instance.base_path == _objects()
    assert i18n_instance.language == "en_EN"


def test_i18n_generate_path() -> None:
    i18n_instance: _i18n = _i18n_instance()
    generated_path = i18n_instance.generate_path(path="en_EN.json")
    assert str(generated_path) == _objects() + "/en_EN.json"


@patch.object(target=pathlib.Path, attribute="exists", return_value=True)
def test_i18n_language_exists(mock_exists) -> None:  # type: ignore
    i18n_instance: _i18n = _i18n_instance()
    assert i18n_instance.language_exists(language="en_EN") is True
    mock_exists.assert_called()  # type: ignore


@patch("io.open", new_callable=mock_open, read_data='{"en_EN": {"key": "value", "testkey": "testvalue"}}')
def test_i18n_load_file(mock_file) -> None:  # type: ignore
    i18n_instance: _i18n = _i18n_instance()
    i18n_instance.load_file(path=_objects() + "/en_EN.json")
    i18n_instance.set_data(data={"en_EN": {"key": "value", "testkey": "testvalue"}})
    assert i18n_instance.lookup("en_EN.key") == "value"


@patch("builtins.open", side_effect=FileNotFoundError)
def test_i18n_load_file_not_found(mock_open) -> None:  # type: ignore
    i18n_instance: _i18n = _i18n_instance()
    with pytest.raises(expected_exception=I18NLoadException):
        i18n_instance.load_file(path=_objects() + "/_en_EN.json")


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_i18n_load_file_decode_error(mock_open) -> None:  # type: ignore
    i18n_instance: _i18n = _i18n_instance()
    with pytest.raises(expected_exception=I18NDecodeException):
        i18n_instance.load_file(path=_objects() + "/decode_error.json")


def test_i18n_current_language() -> None:
    i18n_instance: _i18n = _i18n_instance()
    assert i18n_instance.current_language() == "en_EN"


def test_i18n_set_current_language() -> None:
    i18n_instance: _i18n = _i18n_instance()
    i18n_instance.set_current_language(language="es_ES")
    assert i18n_instance.language == "es_ES"


def test_i18n_lookup_found() -> None:
    i18n_instance: _i18n = _i18n_instance()
    i18n_instance.set_data(data={"level1": {"level2": "value"}})
    assert i18n_instance.lookup(key="level1.level2") == "value"


def test_i18n_lookup_not_found() -> None:
    i18n_instance: _i18n = _i18n_instance()
    assert i18n_instance.lookup(key="nonexistent.key") == "nonexistent.key"


def test_i18n_lookup_not_found_fail() -> None:
    i18n_instance: _i18n = _i18n_instance()
    with pytest.raises(expected_exception=I18NTranslationNotFound):
        i18n_instance.lookup(key="nonexistent.key", fail_on_not_found=True)


def test_translation_repr_unloaded():
    translation = Translation(key="test.key")
    assert repr(translation) == "Translation(test.key) -> [!unloaded i18n engine!]"


def test_translation_str_unloaded() -> None:
    translation = Translation(key="test.key")
    with pytest.raises(expected_exception=I18NNotLoadedException):
        str(object=translation)


def test_translation_str_loaded() -> None:
    i18n_instance: _i18n = _i18n_instance()
    i18n_instance.set_data(data={"test": {"key": "value"}})
    set_i18n(i18n_instance=i18n_instance)
    translation = Translation(key="test.key")
    assert str(object=translation) == "value"


def test_translation_str_key_not_found() -> None:
    i18n_instance: _i18n = _i18n_instance()
    set_i18n(i18n_instance=i18n_instance)
    translation = Translation(key="nonexistent.key")
    assert str(object=translation) == "nonexistent.key"
