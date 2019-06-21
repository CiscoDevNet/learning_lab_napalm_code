from jinja2 import Environment, FileSystemLoader
import yaml

def template_config():
    config_data = yaml.load(open('loopback_template.yml'))
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('loopback_template.j2')

    return(template.render(config_data))
