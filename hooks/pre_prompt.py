#!/usr/bin/env python
import json
import sys
from pathlib import Path
from cookiecutter.prompt import read_user_choice, read_user_yes_no
from typing import Any

intro = """
Welcome to the RedSun cookiecutter template.
Follow the prompts to create a new plugin project.
For reference on each choice, please refer to the RedSun documentation.
"""

def choose_type(data: dict[str, Any]) -> dict[str, Any]:
    """Select which type of plugin to create.
    
    Parameters
    ----------
    data : dict[str, str]
        The current data dictionary.
    
    Returns
    -------
    dict[str, str]
        The updated data dictionary.
    """

    prompts = {
        "plugin_type" : "What type of plugin do you want to create?"
    }
    type_choice: str = read_user_choice("plugin_type", options=["Model", "Controller"], prompts=prompts, prefix="[ExEngine] ")
    data["_plugin_type"] = type_choice

    if type_choice == "Model":
        prompts = {
            "plugin_model_type" : "What type of model do you want to create?"
        }
        model_type_choice: str = read_user_choice("plugin_model_type", options=["Detector", "Motor"], prompts=prompts, prefix="[ExEngine] ")
        data["_plugin_model_type"] = model_type_choice
        prompts = {
                "plugin_mm_support" : "Is your device supported by Micro-Manager?"
            }
        mm_support: bool = read_user_yes_no("plugin_mm_support", default_value=False, prompts=prompts, prefix="[ExEngine] ")
        # in exengine, there is a distinction between single-axis and double-axis motors;
        if model_type_choice == "Motor":
            data = choose_motor_type(data, mm_support)
        else:
            if mm_support:
                data["_plugin_base"] = "ExEngineMMCameraModel"
            else:
                data["_plugin_base"] = "ExEngineDetectorModel"
    else:
        prompts = {
            "plugin_controller_type" : "What type of controller do you want to create?"
        }
        controller_type_choice: str = read_user_choice("plugin_controller_type", options=["Computational", "Device"], prompts=prompts)
        data["_plugin_controller_type"] = controller_type_choice
    return data

def choose_motor_type(data: dict[str, Any], mm_support: bool) -> dict[str, Any]:
    """Select which type of motor to create.

    Currently this selection is limited to ExEngine motor models.

    Parameters
    ----------
    data : dict[str, str]
        The current data dictionary.
    mm_support : bool
        Whether the motor is supported by Micro-Manager.

    Returns
    -------
    dict[str, str]
        The updated data dictionary.    
    """
    prompts = {
        "plugin_motor_type" : "What type of motor do you want to create?"
    }
    motor_type_choice: str = read_user_choice("plugin_motor_type", options=["Single-axis", "Double-axis (X-Y)"], prompts=prompts, prefix="[ExEngine] ")
    if mm_support:
        if motor_type_choice == "Single-axis":
            data["_plugin_base"] = "ExEngineMMSingleMotorModel"
        else:
            data["_plugin_base"] = "ExEngineMMDoubleMotorModel"
    else:
        if motor_type_choice == "Single-axis":
            data["_plugin_base"] = "ExEngineSingleMotorModel"
        else:
            data["_plugin_base"] = "ExEngineDoubleMotorModel"
    return data

print(intro)

with Path("cookiecutter.json") as config:
    try:
        data = json.loads(config.read_text())

        # for now RedSun only supports
        # "exengine" as the acquisition engine;
        # if new engines will be supported,
        # this will be changed to a prompt
        data["_plugin_engine"] = "exengine"

        data = choose_type(data)
        config.write_text(json.dumps(data, indent=4))
    except KeyboardInterrupt:
        sys.exit(1)