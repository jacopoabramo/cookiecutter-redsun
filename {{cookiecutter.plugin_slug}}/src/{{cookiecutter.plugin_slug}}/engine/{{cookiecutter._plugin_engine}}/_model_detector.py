from typing import TYPE_CHECKING

from sunflare.engine.exengine import (
    {{ cookiecutter._plugin_base }}
)

if TYPE_CHECKING:
    from sunflare.config import DetectorModelInfo
    from sunflare.config import PixelPhotometricTypes

    from typing import Union, Optional, Tuple


class MyDetector({{ cookiecutter._plugin_base }}):
    def __init__(self, name: str, model_info: 'DetectorModelInfo') -> None:

        # in this function, initialize your detector API via
        # whatever python package it uses; after initializing a detector,
        # define the initial exposure time for your detector
        exposure: "Union[int, float]" = 100 # dummy value

        # you can also define the following parameters, or delete them and use
        # the default values of the DetectorModel class
        pixel_photometric: "list[PixelPhotometricTypes]" = [PixelPhotometricTypes.GRAY]
        bits_per_pixel: "Optional[set[int]]" = {8}
        binning: "Optional[list[int]]" = [1]
        offset: "Optional[Tuple[int, int]]" = (0, 0)
        shape: "Optional[Tuple[int, int]]" = None

        super().__init__(name, model_info, exposure, pixel_photometric, bits_per_pixel, binning, offset, shape)
    
    def arm(self, frame_count: "Optional[int]" = None) -> None:  # noqa: D102
        # implement
        {% if cookiecutter._plugin_mm_support -%}
        super().arm(frame_count)
        {% else -%}
        ...
        {% endif -%}

    def start(self) -> None:  # noqa: D102
        # implement
        {% if cookiecutter._plugin_mm_support -%}
        super().start()
        {% else -%}
        ...
        {% endif -%}

    def stop(self) -> None:  # noqa: D102
        # implement
        {% if cookiecutter._plugin_mm_support -%}
        super().stop()
        {% else -%}
        ...
        {% endif -%}

    def is_stopped(self) -> bool:  # noqa: D102
        # implement
        {% if cookiecutter._plugin_mm_support -%}
        return super().is_stopped()
        {% else -%}
        ...
        {% endif -%}

    def pop_data(  # noqa: D102
        self, timeout: Optional[float] = None
    ) -> "Tuple[npt.NDArray[Any], dict[str, Any]]": 
        # implement
        # implement
        {% if cookiecutter._plugin_mm_support -%}
        return super().pop_data()
        {% else -%}
        ...
        {% endif -%}