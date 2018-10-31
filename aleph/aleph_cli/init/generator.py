import os

from aleph.aleph_cli.utils.generator_exception import GeneratorException

PATHS = {
  'ALEPH': '.aleph',
  'DATASETS': 'datasets',
  'FEATURES': 'features',
  'LABELS': 'labels',
  'MODELS': 'models',
  'OPTIMIZERS': 'optimizers'
}

def run(args):

  # root project directory and error checking

  if args.name is not None:
    root_path = os.path.join(os.getcwd(), args.name)
    name = args.name
    
    if os.path.exists(root_path):
      raise GeneratorException(f'File or directory already exists at {root_path}. Please specify another name.')
    
    os.mkdir(root_path)

  else: 
    root_path = os.getcwd()
    name = os.basename(root_path)

    if os.path.exist(os.path.join(root_path, PATHS['ALEPH'])):
      raise GeneratorException(f'This directory already contains an aleph project. Please initialize your project in another directory.')

  # top level sub-directories

  for k,v in PATHS.items():
    path = os.path.join(root_path, v)
    os.mkdir(path)

  # status

  print(f'Created aleph project {name}')