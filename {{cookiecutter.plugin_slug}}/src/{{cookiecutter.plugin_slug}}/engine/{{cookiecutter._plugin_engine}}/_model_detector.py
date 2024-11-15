from typing import TYPE_CHECKING

from sunflare.engine.exengine import (
    {{ cookiecutter._plugin_base }}
)

if TYPE_CHECKING:
    from sunflare.config import DetectorModelInfo


class MyDetector({{ cookiecutter._plugin_base }}):
    def __init__(self, name: str, model_info: 'DetectorModelInfo') -> None:
        super().__init__(name, model_info)