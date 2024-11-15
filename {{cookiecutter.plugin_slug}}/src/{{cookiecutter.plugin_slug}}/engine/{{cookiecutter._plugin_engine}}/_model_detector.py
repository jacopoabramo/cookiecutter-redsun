from typing import TYPE_CHECKING

from sunflare.engine.exengine import (
    {{ cookiecutter._plugin_base }}
)

from sunflare.engine.exengine import (
    ExEngineDetectorModel,
    ExEngineMMCameraModel
)

if TYPE_CHECKING:
    from sunflare.config import DetectorModelInfo

class MyDetector({{ cookiecutter._plugin_base }}):
    def __init__(self, model_info: 'DetectorModelInfo'):
        super().__init__(model_info)