#! /usr/bin/env python
"""
Usage:
    build_pelican.py

This script will build the pelican files.
"""
from __future__ import print_function
import os.path as op
import os

from docopt import docopt
from jinja2 import Environment, FileSystemLoader

from build import safe_call, get_releases


content_path = op.join(os.getcwd(), 'content')
pages_path = op.join(content_path, 'pages')
static_website_path = op.join(os.getcwd(), 'static_website_output')
pelican_path = op.join(os.getcwd(), 'pelican')
menpo_notebooks_path = op.join(os.getcwd(), 'menpo-notebooks')

nb_all_tmplt_path = 'all_notebooks_landing.md'

env = Environment(loader=FileSystemLoader(op.join(content_path, 'templates')),
                  trim_blocks=True, lstrip_blocks=True)


def build_pelican():
    # Call pelican externally in order to build the HTML
    os.chdir(pelican_path)
    command = ['pelican', content_path, '-o', static_website_path,
               '-s', op.join(pelican_path, 'pelicanconf.py')]
    return_code = safe_call(command)
    if return_code != 0:
        print("ERROR: Pelican failed to complete correctly!")
        print("Please run pelican manually with: {}".format(' '.join(command)))
    else:
        print('Successfully built the HTML files!')


def build_notebooks_markdown():
    # Get a list of all treleases from github
    notebooks_releases = get_releases()
    notebooks_versions = [release['tag_name'] for release in notebooks_releases]

    # For every folder we found, walk through it and build a landing page
    # for all the notebooks in that version
    for version in notebooks_versions:
        print('Found a version of the notebooks at: {}'.format(version))

    # Build the landing page for ALL the versions (so you can choose a version
    # to view)
    # Get the most recent tag
    latest_version = notebooks_versions.pop(0)

    all_landing_tmplt = env.get_template(nb_all_tmplt_path)
    all_landing_output = all_landing_tmplt.render(
        previous_versions=notebooks_versions,
        latest_version=latest_version)
    with open(op.join(pages_path, 'notebooks.md'), 'w') as f:
        f.write(all_landing_output)


def run(args=None):
    build_notebooks_markdown()
    build_pelican()


if __name__ == '__main__':
    args = docopt(__doc__)
    run(args=args)
