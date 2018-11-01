import os

from aleph.aleph_cli.utils.aleph_filesystem import exit_if_not_aleph_project
from aleph.aleph_cli.utils.aleph_filesystem import activate_project_environment
from aleph.aleph_cli.utils.generator_exception import GeneratorException

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
  for filename in datasets_filenames():
    print(filename)

def run_add(args):
  name = args.name

  if name in datasets_filenames():
    raise GeneratorException(f'Error: The dataset {name} already exists. Please give this dataset another name.')

  filepath = os.path.join(datasets_path(), f'{name}.py')
  open(filepath, 'a').close()

def run_remove(args):
  name = args.name

  if not name in datasets_filenames():
    raise GeneratorException(f'Error: The dataset {name} does not exist.')
  
  filepath = os.path.join(datasets_path(), f'{name}.py')
  os.remove(filepath)

# ====== Utilties ======

# TODO: move all path stuff to aleph_filesystem?

def datasets_path():
  root_path = os.getcwd()
  datasets_path = os.path.join(root_path, 'datasets')

  return datasets_path

def datasets_filenames():
  ds_path = datasets_path()
  filelist = os.listdir(ds_path)
  filenames = [os.path.splitext(f)[0] for f in filelist if os.path.isfile(os.path.join(ds_path, f)) and os.path.splitext(f)[1] == '.py']
  
  return filenames
  