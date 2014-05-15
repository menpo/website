import requests


def get_releases(user, repo, include_prerelease=True):
    releases_str = 'https://api.github.com/repos/{}/{}/releases'.format(user,
                                                                        repo)
    r = requests.get(releases_str)
    response = r.json()
    # Only include release tags

    # For if we want to filter prereleases
    if not include_prerelease:
        response = filter(lambda x: not x.prerelease, response)
    return response


def get_menpo_releases():
    releases = get_releases('menpo', 'menpo')
    releases = filter(lambda x: x['tag_name'][0] == 'v', releases)
    return releases