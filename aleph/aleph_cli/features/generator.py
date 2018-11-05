import os
import inspect

from aleph.aleph_cli.utils.aleph_filesystem import exit_if_not_aleph_project
from aleph.aleph_cli.utils.aleph_filesystem import activate_project_environment
from aleph.aleph_cli.utils.generator_exception import GeneratorException

from jinja2 import Template

def run(args):
  exit_if_not_aleph_project()
  activate_project_environment()
  
  if args.subcommand == 'list':
    run_list(args)
  if args.subcommand == 'add':
    run_add(args)
  if args.subcommand == 'remove':
    run_remove(args)

# ====== Subcommands ======

def run_list(args):  
  for filename in features_filenames():
    print(filename)

def run_add(args):
  name = args.name

  if name in features_filenames():
    raise GeneratorException(f'Error: The feature {name} already exists. Please give this feature another name.')

  filepath = os.path.join(features_path(), f'{name}.py')
  
  with open(feature_template_path()) as f:
    template = Template(f.read())

  with open(filepath, 'w') as f:
    f.write(template.render(vars(args)))

def run_remove(args):
  name = args.name

  if not name in features_filenames():
    raise GeneratorException(f'Error: The feature {name} does not exist.')
  
  filepath = os.path.join(features_path(), f'{name}.py')
  os.remove(filepath)

# ====== Utilties ======

# TODO: move all path stuff to aleph_filesystem?

# package paths

def templates_path():
  import aleph.aleph_cli.features.templates
  return os.path.dirname(inspect.getfile(aleph.aleph_cli.features.templates))

def feature_template_path():
  return os.path.join(templates_path(), 'feature.py.jinja2')

# project paths

def features_path():
  root_path = os.getcwd()
  datasets_path = os.path.join(root_path, 'features')

  return datasets_path

def features_filenames():
  ds_path = features_path()
  filelist = os.listdir(ds_path)
  filenames = [os.path.splitext(f)[0] for f in filelist if os.path.isfile(os.path.join(ds_path, f)) and os.path.splitext(f)[1] == '.py']
  
  return filenames
  