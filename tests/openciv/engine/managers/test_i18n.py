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

from openciv.engine.managers.i18n import Translation, set_i18n, _i18n

# Replace 'your_module' with the actual module name where your i18n class is located


def _objects(file=""):
    if file != "":
        file = f"/{file}"
    return str((Path(__file__).resolve().parent / f"../../../resources/test_objects{file}").resolve())


def _i18n_instance() -> _i18n:
    return _i18n(_objects(), "en_EN")


def test_i18n_initialization():
    i18n_instance = _i18n_instance()
    assert i18n_instance.base_path == _objects()
    assert i18n_instance.language == "en_EN"


def test_i18n_generate_path():
    i18n_instance = _i18n_instance()
    generated_path = i18n_instance.generate_path("en_EN.json")
    assert generated_path == _objects() + "/en_EN.json"


@patch.object(pathlib.Path, "exists", return_value=True)
def test_i18n_language_exists(mock_exists):
    i18n_instance = _i18n_instance()
    assert i18n_instance.language_exists("en_EN") is True
    mock_exists.assert_called()


@patch("io.open", new_callable=mock_open, read_data='{"en_EN": {"key": "value", "testkey": "testvalue"}}')
def test_i18n_load_file(mock_file):
    i18n_instance = _i18n_instance()
    i18n_instance.load_file(_objects() + "/en_EN.json")
    assert i18n_instance._data == {"en_EN": {"key": "value", "testkey": "testvalue"}}
    mock_file.assert_called_with(_objects() + "/en_EN.json", "r")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_i18n_load_file_not_found(mock_file):
    i18n_instance = _i18n_instance()
    with pytest.raises(I18NLoadException):
        i18n_instance.load_file(_objects() + "/_en_EN.json")


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_i18n_load_file_decode_error(mock_file):
    i18n_instance = _i18n_instance()
    with pytest.raises(I18NDecodeException):
        i18n_instance.load_file(_objects() + "/decode_error.json")


def test_i18n_current_language():
    i18n_instance = _i18n_instance()
    assert i18n_instance.current_language() == "en_EN"


def test_i18n_set_current_language():
    i18n_instance = _i18n_instance()
    i18n_instance.set_current_language("es_ES")
    assert i18n_instance.language == "es_ES"


def test_i18n_lookup_found():
    i18n_instance = _i18n_instance()
    i18n_instance._data = {"level1": {"level2": "value"}}
    assert i18n_instance.lookup("level1.level2") == "value"


def test_i18n_lookup_not_found():
    i18n_instance = _i18n_instance()
    assert i18n_instance.lookup("nonexistent.key") == "nonexistent.key"


def test_i18n_lookup_not_found_fail():
    i18n_instance = _i18n_instance()
    with pytest.raises(I18NTranslationNotFound):
        i18n_instance.lookup("nonexistent.key", fail_on_not_found=True)


def test_translation_repr_unloaded():
    translation = Translation("test.key")
    assert repr(translation) == "Translation(test.key) -> [!unloaded i18n engine!]"


def test_translation_str_unloaded():
    translation = Translation("test.key")
    with pytest.raises(I18NNotLoadedException):
        str(translation)


def test_translation_str_loaded():
    i18n_instance = _i18n_instance()
    i18n_instance._data = {"test": {"key": "value"}}
    set_i18n(i18n_instance)
    translation = Translation("test.key")
    assert str(translation) == "value"


def test_translation_str_key_not_found():
    i18n_instance = _i18n_instance()
    set_i18n(i18n_instance)
    translation = Translation("nonexistent.key")
    assert str(translation) == "nonexistent.key"
