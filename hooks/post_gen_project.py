#!/usr/bin/env python
import pathlib
import os


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        pathlib.Path('LICENSE').unlink()

    if '{{ cookiecutter._plugin_model_type }}' == 'Motor':
        to_delete = '_model_detector.py'
        to_keep = '_model_motor.py'
    else: # 'Detector'
        to_delete = '_model_motor.py'
        to_keep = '_model_detector.py'
    # TODO: add support for other model types
    path_to_keep = os.path.join(
            "src",
            "{{ cookiecutter.plugin_slug }}",
            "engine",
            "{{ cookiecutter._plugin_engine }}",
            to_keep
        )
    path_to_delete = os.path.join(
            "src",
            "{{ cookiecutter.plugin_slug }}",
            "engine",
            "{{ cookiecutter._plugin_engine }}",
            to_delete
        )
    os.remove(
        os.path.join(
            "src",
            "{{ cookiecutter.plugin_slug }}",
            "engine",
            "{{ cookiecutter._plugin_engine }}",
            to_delete
        )
    )
    os.rename(
        os.path.join(
            "src",
            "{{ cookiecutter.plugin_slug }}",
            "engine",
            "{{ cookiecutter._plugin_engine }}",
            to_keep
        ),
        os.path.join(
            "src",
            "{{ cookiecutter.plugin_slug }}",
            "engine",
            "{{ cookiecutter._plugin_engine }}",
            "model.py"
        )
    )
