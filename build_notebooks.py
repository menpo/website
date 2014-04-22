#! /usr/bin/env python
"""
Usage:
    build_notebooks.py

This script will build the notebooks files.
"""
from __future__ import print_function
from docopt import docopt
import os.path as op
import os
from build import safe_call, get_git_tag
import shutil

menpo_notebooks_path = op.join(os.getcwd(), 'menpo-notebooks')
base_notebook_path = op.join(menpo_notebooks_path, 'notebooks')
base_output_html_path = op.join(os.getcwd(), 'static_website_output', 'notebooks')


def run(args=None):
    tag_version = get_git_tag(menpo_notebooks_path)
    print('Found git tag version of: {}'.format(tag_version))
    version_output_path = op.join(base_output_html_path, tag_version)
    print('Output path is: {}'.format(version_output_path))

    if op.exists(version_output_path):
        print('Removing any existing notebook HTML files...')
        shutil.rmtree(version_output_path)

    os.makedirs(version_output_path)

    print('Beginning to convert notebooks -> This may take a while...')
    for curr_path, dirs, files in os.walk(base_notebook_path):
        # Ignore hidden folders (in particular, the .ipynb_checkpoints folder)
        if op.basename(curr_path)[0] != '.':
            print('Converting all notebooks in {}'.format(curr_path))
            # Calculate the output folder we need to create by removing the
            # common prefix
            relative_path = op.relpath(curr_path, base_notebook_path)
            folder_output_path = op.join(version_output_path, relative_path)
            # Create the output folder
            if not op.exists(folder_output_path):
                os.makedirs(folder_output_path)

            # Use the nbconvert command to convert the notebooks
            os.chdir(folder_output_path)
            safe_call(['ipython', 'nbconvert', '--to', 'html',
                       op.join(curr_path, '*.ipynb')])
    print('Successfully converted all notebooks!')

if __name__ == '__main__':
    args = docopt(__doc__)
    run(args=args)
