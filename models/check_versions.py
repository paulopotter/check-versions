import requests


class CheckVersions:
    def __init__(self, settings):
        self.settings = settings

    def check_packages(self):
        self.get_from_requirements()
        return self.settings

    def get_from_requirements(self):
        settings = self.settings['PROJECT']
        url = settings['REQUIREMENTS_URL']

        try:
            request = requests.get(url)

            if request.status_code == 200:
                if settings['REQUIREMENTS_TYPE'] == 'txt':
                    return request.text
                else:
                    return request.json()
            else:
                return 'ERROR'
        except Exception as e:
            return e
