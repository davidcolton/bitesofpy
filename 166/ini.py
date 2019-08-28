import configparser
import re


class ToxIniParser:
    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.parser = configparser.ConfigParser()
        self.parser.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.parser.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        env_list = sorted(
            [
                env.strip()
                for env in re.split(
                    r"\s*,\s*|\n", self.parser.get("tox", "envlist").strip()
                )
                if env.strip() != ""
            ]
        )
        return env_list

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_python_values = set()
        for section_name in self.parser.sections():
            for name, value in self.parser.items(section_name):
                if name == "basepython":
                    base_python_values.add(value)
        return list(base_python_values)
