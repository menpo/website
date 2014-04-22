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
from glob import glob

main_notebooks_header = """Title: {}

"""

landing_page_header = """Title: {0}
url: notebooks/{1}
save_as: notebooks/{1}/index.html
"""

content_path = op.join(os.getcwd(), 'content')
pages_path = op.join(content_path, 'pages')
static_website_path = op.join(os.getcwd(), 'static_website_output')
built_notebooks_path = op.join(static_website_path, 'notebooks')
built_documentation_path = op.join(static_website_path, 'docs')
pelican_path = op.join(os.getcwd(), 'pelican')

link_template = '[{}]({})'
pages_link_template = '[{}]({{filename}}/pages/{})'


def build_pelican():
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
    import itertools

    notebooks_versions_paths = [op.join(built_notebooks_path, p) for p
                                in os.listdir(built_notebooks_path)]
    # Create the main notebook page
    with open(op.join(pages_path, 'notebooks.md'), 'w') as f:
        # Write head
        f.write(main_notebooks_header.format('Notebooks', 'notebooks'))

        # Write each tag
        for version_path in notebooks_versions_paths:
            tag_name = op.basename(version_path)
            notebook_landing_filename = '{}-notebooks.md'.format(tag_name)
            link = pages_link_template.format(tag_name,
                                              notebook_landing_filename)
            f.write('  - {}'.format(link))
            f.write('\n')

    # Create a landing page for each version
    for version_path in notebooks_versions_paths:
        tag_name = op.basename(version_path)
        notebook_landing_basename = '{}-notebooks.md'.format(tag_name)
        notebooks_paths = [[op.relpath(op.join(top, f),
                                       static_website_path) for f in files]
                           for top, _, files in os.walk(version_path)]
        # Flatten lists
        notebooks_paths = list(itertools.chain(*notebooks_paths))

        # Write a landing page for each set of
        notebook_landing_path = op.join(pages_path,
                                        notebook_landing_basename)
        with open(notebook_landing_path, 'w') as f:
            f.write(landing_page_header.format('Notebooks ' + tag_name, tag_name))
            for p in notebooks_paths:
                base_name = op.basename(p)
                notebook_name = op.splitext(base_name)[0]
                link = link_template.format(notebook_name, base_name)
                f.write('  - {}'.format(link))
                f.write('\n')


def build_documentation_markdown():
    docs_versions_paths = [op.join(built_documentation_path, p) for p
                           in os.listdir(built_documentation_path)]
    # Create the main notebook page
    with open(op.join(pages_path, 'documentation.md'), 'w') as f:
        # Write head
        f.write(main_notebooks_header.format('Documentation'))

        # Write each tag
        for version_path in docs_versions_paths:
            tag_name = op.basename(version_path)
            docs_path = op.join('docs', tag_name)
            link = link_template.format(tag_name, docs_path)
            f.write('  - {}'.format(link))
            f.write('\n')


def run(args=None):
    build_notebooks_markdown()
    build_documentation_markdown()
    build_pelican()


if __name__ == '__main__':
    args = docopt(__doc__)
    run(args=args)
