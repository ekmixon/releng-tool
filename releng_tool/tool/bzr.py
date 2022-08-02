# -*- coding: utf-8 -*-
# Copyright 2018-2021 releng-tool

from releng_tool.tool import RelengTool
import sys

#: executable used to run bzr commands
BZR_COMMAND = 'bzr'

#: list of environment keys to filter from a environment dictionary
BZR_SANITIZE_ENV_KEYS = [
    # prevent debugger from loading
    'BZR_PDB',
    # misc
    'BZR_REMOTE_PATH',
    'BZR_TEXTUI_INPUT',
]

#: dictionary of environment entries append to the environment dictionary
BZR_EXTEND_ENV = {
    'BZR_PROGRESS_BAR': 'text',
    'BZR_LOG': '/dev/null' if sys.platform != 'win32' else 'NUL',
}


#: bzr host tool helper
BZR = RelengTool(BZR_COMMAND,
    env_sanitize=BZR_SANITIZE_ENV_KEYS, env_include=BZR_EXTEND_ENV)
