import logging
import yaml
from jinja2 import Environment, FileSystemLoader
import glob
import config
import os

mappings_dir = config.mappings_dir


class PayloadAdapter:
    def __init__(self, mapping):
        self.mapping = mapping

    def convert_payload(self, payload):
        template = _get_template(self.mapping)
        rendered = template.render(load=payload)
        logging.debug(f"rendered template:\n {rendered}")
        data = yaml.safe_load(rendered)
        logging.debug(data)
        return data


def _get_template(mapping):
    matches = glob.glob(f"{mappings_dir}/{mapping}.*")
    if len(matches) == 0:
        raise FileNotFoundError(f"No such mapping: {mapping}\n")
    template_file_path = matches[0]
    template_file_name = os.path.basename(template_file_path)
    return jinja_env.get_template(template_file_name)


def _escape_quotes(value):
    if type(value) is str:
        return value.replace('"', '\\"')
    else:
        return value


jinja_env = Environment(loader=FileSystemLoader(mappings_dir),
                        finalize=_escape_quotes)
