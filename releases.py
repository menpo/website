import requests


def get_releases(user, repo, include_prerelease=False):
    releases_str = 'https://api.github.com/repos/{}/{}/releases'.format(user,
                                                                        repo)
    r = requests.get(releases_str)
    response = r.json()
    # Only include release tags

    # For if we want to filter prereleases
    if not include_prerelease:
        response = [x for x in response if not x['prerelease']]
    return response


def get_menpo_releases():
    releases = get_releases('menpo', 'menpo')
    releases = filter(lambda x: x['tag_name'][0] == 'v', releases)
    return releases


def get_menpofit_releases():
    releases = get_releases('menpo', 'menpofit', include_prerelease=True)
    releases = filter(lambda x: x['tag_name'][0] == 'v', releases)
    return releases


def get_menpo3d_releases():
    releases = get_releases('menpo', 'menpo3d', include_prerelease=True)
    releases = filter(lambda x: x['tag_name'][0] == 'v', releases)
    return releases


def get_menpodetect_releases():
    releases = get_releases('menpo', 'menpodetect', include_prerelease=True)
    releases = filter(lambda x: x['tag_name'][0] == 'v', releases)
    return releases
