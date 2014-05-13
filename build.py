#! /usr/bin/env python
"""
Usage:
    build.py pelican
    build.py --version
    build.py -h | --help

Options:
   -h, --help   Show this help text
   --version    Show Version
"""
from __future__ import print_function
from docopt import docopt
import os


def safe_call(args_list):
    from subprocess import call
    # Avoid output deadlock!
    # http://stackoverflow.com/questions/2561902/python-execute-process-block-till-it-exits-supress-output
    null_device = open(os.devnull, 'w')
    return call(args_list, bufsize=4096, stdout=null_device, stderr=null_device)


def get_git_latest_tag(repo_path):
    import subprocess
    # Change the working directory to the repository path
    os.chdir(repo_path)
    try:
        p = subprocess.Popen(["git", "describe",
                              "--tags", "--dirty", "--always"],
                             stdout=subprocess.PIPE)
    except EnvironmentError:
        raise EnvironmentError('Failed to run git')

    stdout = p.communicate()[0]
    if p.returncode != 0:
        raise EnvironmentError('Executing git returned a non-zero '
                               'return code of {}'.format(p.returncode))

    return stdout.strip()


def get_git_all_tags(repo_path):
    import subprocess
    # Change the working directory to the repository path
    os.chdir(repo_path)
    try:
        p = subprocess.Popen(["git", "tag", "-l"],
                             stdout=subprocess.PIPE)
    except EnvironmentError:
        raise EnvironmentError('Failed to run git')

    stdout = p.communicate()[0]
    if p.returncode != 0:
        raise EnvironmentError('Executing git returned a non-zero '
                               'return code of {}'.format(p.returncode))

    return stdout.split()


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')

    if args['pelican']:
        import build_pelican
        exit(build_pelican.run())
    else:
        exit(print(docopt(__doc__, argv='--help')))

