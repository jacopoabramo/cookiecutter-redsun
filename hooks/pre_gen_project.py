#!/usr/bin/env python
import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{cookiecutter.plugin_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The plugin slug (%s) is not a valid Python module name. '
          'Please do not use a - and use _ instead' % module_name)
    sys.exit(1)
