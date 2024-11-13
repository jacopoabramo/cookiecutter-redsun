import json
import sys
from pathlib import Path
from cookiecutter.prompt import read_user_choice
from typing import Any

intro = """
Welcome to the RedSun cookiecutter template.
Follow the prompts to create a new plugin project.
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
    type_choice : str = read_user_choice("plugin_type", options=["Model", "Controller"], prompts=prompts)
    data["_plugin_type"] = type_choice.lower()

    if type_choice == "Model":
        data["plugin_model_type"] = ["Detector", "Motor"]
        data["__prompts__"]["plugin_model_type"] = "What type of model do you want to create?"
    else:
        data["plugin_controller_type"] = ["Computational", "Device"]
        data["__prompts__"]["plugin_controller_type"] = "What type of controller do you want to create?"
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