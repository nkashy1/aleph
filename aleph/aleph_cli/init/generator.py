import os
import subprocess
import inspect

from aleph.aleph_cli.utils.generator_exception import GeneratorException
from aleph.aleph_cli.utils.aleph_filesystem import execfile

# TODO: move all this path stuff to the aleph_filesystem

PATHS = {
  'ALEPH': '.aleph',
  'DATASETS': 'datasets',
  'FEATURES': 'features',
  'LABELS': 'labels',
  'MODELS': 'models',
  'OPTIMIZERS': 'optimizers'
}

REQUIREMENTS = [
  'numpy',
  'tensorflow',
  'tensorflow_hub',
  'Jinja2'
  #aleph
]

def run(args):

  # root project directory and error checking

  if args.name is not None:
    root_path = os.path.join(os.getcwd(), args.name)
    name = args.name

    if os.path.isdir(root_path):
      raise GeneratorException(f'Error: File or directory already exists at {root_path}. Please specify another name.')

    os.mkdir(root_path)

  else:
    root_path = os.getcwd()
    name = os.path.basename(root_path)

    if os.path.isdir(os.path.join(root_path, PATHS['ALEPH'])):
      raise GeneratorException(f'Error: This directory already contains an aleph project. Please initialize your project in another directory.')

  # virtual env

  env_path = os.path.join(root_path, f'.{name}-environment')
  activate_this_path = os.path.join(os.path.join(env_path, 'bin'), 'activate_this.py')
  packages = ' '.join(REQUIREMENTS)

  subprocess.call(f'virtualenv --python python3 {env_path}', shell=True)
  execfile(activate_this_path)
  subprocess.call(f'pip install {packages}', shell=True)

  # top level sub-directories

  for _,v in PATHS.items():
    path = os.path.join(root_path, v)
    os.mkdir(path)

  # top level files

  from jinja2 import Template



  # status

  print(f'Created aleph project {name}')
