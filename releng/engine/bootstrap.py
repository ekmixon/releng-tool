#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 releng-tool

from ..util.io import interimWorkingDirectory
from ..util.io import run_script
from ..util.log import *
import os
import sys

#: filename of the script to execute the bootstrapping operation (if any)
BOOTSTRAP_SCRIPT = 'bootstrap'

def stage(engine, pkg, script_env):
    """
    handles the bootstrapping stage for a package

    With a provided engine and package instance, the bootstrapping stage will
    be processed. This stage is typically not advertised and is for advanced
    cases where a developer wishes to manipulate their build environment before
    package has started its configuration+ phases.

    Args:
        engine: the engine
        pkg: the package being built
        script_env: script environment information

    Returns:
        ``True`` if the bootstrapping stage is completed; ``False`` otherwise
    """

    verbose('bootstrapping {}...'.format(pkg.name))
    sys.stdout.flush()

    bootstrap_script_filename = '{}-{}'.format(pkg.name, BOOTSTRAP_SCRIPT)
    bootstrap_script = os.path.join(pkg.def_dir, bootstrap_script_filename)
    if not os.path.isfile(bootstrap_script):
        bootstrap_script += '.releng'
        if not os.path.isfile(bootstrap_script):
            return True

    if pkg.build_subdir:
        build_dir = pkg.build_subdir
    else:
        build_dir = pkg.build_dir

    with interimWorkingDirectory(build_dir):
        if not run_script(bootstrap_script, script_env, subject='bootstrap'):
            return False

    verbose('bootstrap script executed: ' + bootstrap_script)
    return True
