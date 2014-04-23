#! /usr/bin/env python
"""
Usage:
    build_pelican.py

This script will build the pelican files.
"""
from __future__ import print_function
from docopt import docopt
import os.path as op
import os
from build import safe_call
from jinja2 import Environment, FileSystemLoader


content_path = op.join(os.getcwd(), 'content')
pages_path = op.join(content_path, 'pages')
static_website_path = op.join(os.getcwd(), 'static_website_output')
built_notebooks_path = op.join(static_website_path, 'notebooks')
built_documentation_path = op.join(static_website_path, 'docs')
pelican_path = op.join(os.getcwd(), 'pelican')

nb_all_tmplt_path = 'all_notebooks_landing.md'
docs_all_tmplt_path = 'all_docs_landing.md'
nb_ver_tmplt_path = 'version_notebooks_landing.md'

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
    notebooks_landing_versions = []

    # Get a list of all the folders in the built notebooks path
    # Should be one folder per version (only return the folders!)
    notebooks_versions_paths = [op.join(built_notebooks_path, p) for p
                                in os.listdir(built_notebooks_path)]
    notebooks_versions_paths = filter(op.isdir, notebooks_versions_paths)

    # For every folder we found, walk through it and build a landing page
    # for all the notebooks in that version
    for version_path in notebooks_versions_paths:
        print('Found a version of the notebooks at: {}'.format(version_path))
        # Record this version for the main landing page
        version = op.basename(version_path)
        notebooks_landing_versions.append(version)

        # Walk through every folder in the notebooks and build a seperate
        # header per folder within the landing page
        notebooks_folders = []
        for curr_path, dirs, files in os.walk(version_path):
            dirname = op.basename(curr_path)

            # The root is a special case! Ensure the folder name is in the
            # form of a title (capitalized words)
            header = 'Root' if dirname == version else dirname.title()
            folder_info = {'header': header, 'notebooks': []}
            # For each notebook in the folder generate a link
            for f in files:
                nbook_path = op.relpath(op.join(curr_path, f), version_path)
                nbook_name = op.splitext(f)[0]
                folder_info['notebooks'].append({'text': nbook_name,
                                                 'url': nbook_path})
            # Save the folder information
            notebooks_folders.append(folder_info)

        # Build the landing page!
        ver_landing_tmplt = env.get_template(nb_ver_tmplt_path)
        ver_landing_output = ver_landing_tmplt.render(
            notebooks=notebooks_folders, version=version)

        output_md_path = op.join(pages_path, 'notebook_versions',
                                 version + '.md')
        with open(output_md_path, 'w') as f:
            f.write(ver_landing_output)

    # Build the landing page for ALL the versions (so you can choose a version
    # to view)
    all_landing_tmplt = env.get_template(nb_all_tmplt_path)
    all_landing_output = all_landing_tmplt.render(
        versions=notebooks_landing_versions)
    with open(op.join(pages_path, 'notebooks.md'), 'w') as f:
        f.write(all_landing_output)


def build_documentation_markdown():
    # Get all built version from the built documentation,
    # so only return directories
    docs_versions_paths = [op.join(built_documentation_path, p) for p
                           in os.listdir(built_documentation_path)]
    docs_versions_paths = filter(op.isdir, docs_versions_paths)
    for d in docs_versions_paths:
        print('Found a version of the docs at: {}'.format(d))

    # Get a list of every version
    docs_versions = [op.basename(d) for d in docs_versions_paths]


    # Build the landing page for ALL the versions (so you can choose a version
    # to view)
    all_landing_tmplt = env.get_template(docs_all_tmplt_path)
    all_landing_output = all_landing_tmplt.render(
        versions=docs_versions)
    with open(op.join(pages_path, 'documentation.md'), 'w') as f:
        f.write(all_landing_output)


def run(args=None):
    build_notebooks_markdown()
    build_documentation_markdown()
    build_pelican()


if __name__ == '__main__':
    args = docopt(__doc__)
    run(args=args)
