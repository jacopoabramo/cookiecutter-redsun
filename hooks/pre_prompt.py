import json
import sys
from pathlib import Path
from cookiecutter.prompt import read_user_choice

intro = """
Welcome to the RedSun cookiecutter template.
Follow the prompts to create a new plugin project.
"""

def choose_type(data: dict[str, str]) -> dict[str, str]:
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