# app/i18n.py
import gettext
import os
from typing import Callable

# Constants
DEFAULT_LANGUAGE = 'en'
MESSAGES_DOMAIN = 'messages'


def get_locale_dir() -> str:
    """Return the absolute path to the locale directory."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')


def get_translation(language_code: str = DEFAULT_LANGUAGE) -> gettext.GNUTranslations:
    """Get the translation object for the specified language."""
    locale_dir = get_locale_dir()
    print("locale_dir: ", locale_dir)
    return gettext.translation(MESSAGES_DOMAIN, locale_dir, languages=[language_code], fallback=True)


# Initialize with default language
_translation = get_translation()
_ = _translation.gettext


def init_i18n(language_code: str = DEFAULT_LANGUAGE) -> None:
    """
    Initialize or update the internationalization setup.

    Args:
        language_code (str): The language code to set. Defaults to DEFAULT_LANGUAGE.
    """
    global _, _translation
    _translation = get_translation(language_code)
    _ = _translation.gettext


# Export the _ function and init_i18n function
__all__ = ['_', 'init_i18n']
