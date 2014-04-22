#! /usr/bin/env python
"""
Usage:
    build_docs.py

This script will build the docs files.
"""
from __future__ import print_function
import shutil
from docopt import docopt
import os.path as op
import os
from build import safe_call, get_git_tag


menpo_path = op.join(os.getcwd(), 'menpo')
docs_path = op.join(menpo_path, 'docs')
static_website_path = op.join(os.getcwd(), 'static_website_output')
base_output_path = op.join(static_website_path, 'docs')


def run(args=None):
    tag_version = get_git_tag(menpo_path)
    print('Found git tag version of: {}'.format(tag_version))
    version_output_path = op.join(base_output_path, tag_version)
    print('Output path is: {}'.format(version_output_path))

    if op.exists(version_output_path):
        print('Removing any existing docs files...')
        shutil.rmtree(version_output_path)

    os.makedirs(version_output_path)

    # Build the docs
    command = ['sphinx-build', '-a', '-E', '-b', 'html', docs_path,
               version_output_path]
    return_code = safe_call(command)
    if return_code != 0:
        print("ERROR: Sphinx-build failed to complete correctly!")
        print("Please run sphinx-build manually with: {}".format(
            ' '.join(command)))
    else:
        print('Deleting .doctrees cache')
        shutil.rmtree(op.join(version_output_path, '.doctrees'))
        print('Successfully built the documentation!')


if __name__ == '__main__':
    args = docopt(__doc__)
    run(args=args)
