import json
from pathlib import Path
from typing import cast, Any, Final

from pydantic import BaseSettings, Extra
from pydantic.env_settings import SettingsSourceCallable

BASE_PATH: Final[Path] = Path(__file__).resolve().parent.parent


def secrets_settings_source(settings: BaseSettings) -> dict[str, Any]:
    encoding = settings.__config__.env_file_encoding
    secrets_path = Path(BASE_PATH).joinpath(Path('.secrets.json'))

    try:
        secrets_content = secrets_path.read_text(encoding)
    except FileNotFoundError:
        return {}

    return cast(dict[str, Any], json.loads(secrets_content))


class AppConfig(BaseSettings):
    port: int = 7000
    debug: bool = False
    session_secret_key: str

    class Config:
        extra = Extra.ignore
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'

        @classmethod
        def customise_sources(
                cls,  # noqa: WPS318
                init_settings: SettingsSourceCallable,
                env_settings: SettingsSourceCallable,
                file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            return (
                init_settings,            # параметры переданные напрямую - наивысший приоритет
                env_settings,             # env параметры
                file_secret_settings,     # файлы-параметры для локальной разработки
                secrets_settings_source,  # параметры для локальной разработки
            )


config = AppConfig()
