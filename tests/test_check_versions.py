import yaml
import unittest
from models.check_versions import *


def test_setting_file():
    with open('tests/utils/settings.yaml', 'r') as file:
        settings = yaml.load(file)
    return settings


class TestRepositoryPackages(unittest.TestCase):

    def test_get_from_requirements_as_txt(self):

        check_versions = CheckVersions(test_setting_file())
        get_from_requirements = check_versions.get_from_requirements()
        expect_return = "flask\nrequests\npyyaml\nawesome-slugify\n"

        assert get_from_requirements == expect_return

    def test_get_from_requirements_as_json(self):
        mock_test_setting_file = test_setting_file()
        mock_test_setting_file["PROJECT"]["REQUIREMENTS_TYPE"] = "json"
        mock_test_setting_file["PROJECT"]["REQUIREMENTS_URL"] = mock_test_setting_file["PROJECT"]["REQUIREMENTS_URL"].replace(".txt", ".json")

        check_versions = CheckVersions(mock_test_setting_file)
        get_from_requirements = check_versions.get_from_requirements()

        expect_return = {
            "dependencias": {
                "flask": "0.0.1",
                "requests": "0.0.1",
                "pyyaml": "0.0.1",
                "awesome-slugify": "0.0.1"
            }
        }

        assert get_from_requirements == expect_return
