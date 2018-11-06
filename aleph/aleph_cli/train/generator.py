import os

from aleph.aleph_cli.utils.aleph_filesystem import exit_if_not_aleph_project
from aleph.aleph_cli.utils.aleph_filesystem import activate_project_environment
from aleph.aleph_cli.utils.generator_exception import GeneratorException

def run(args):
  exit_if_not_aleph_project()
  activate_project_environment()

  model = args.model
  optimizer = args.optimizer
  tfhub_module = args.module

  if model not in models_filenames():
    raise GeneratorException(f'Error: The model {model} could not be found. Please try another model.') 

  if optimizer not in optimizers_filenames():
    raise GeneratorException(f'Error: The optimnizer {optimizer} could not be found. Please try another optimizer.') 

  if tfhub_module is not None:
    pass

  pass

# TODO: move to aleph_filesystem? These are being duplicated in their respective submodules

def models_path():
  root_path = os.getcwd()
  datasets_path = os.path.join(root_path, 'models')

  return datasets_path

def models_filenames():
  ds_path = models_path()
  filelist = os.listdir(ds_path)
  filenames = [os.path.splitext(f)[0] for f in filelist if os.path.isfile(os.path.join(ds_path, f)) and os.path.splitext(f)[1] == '.py']
  
  return filenames
  
def optimizers_path():
  root_path = os.getcwd()
  datasets_path = os.path.join(root_path, 'optimizers')

  return datasets_path

def optimizers_filenames():
  ds_path = optimizers_path()
  filelist = os.listdir(ds_path)
  filenames = [os.path.splitext(f)[0] for f in filelist if os.path.isfile(os.path.join(ds_path, f)) and os.path.splitext(f)[1] == '.py']
  
  return filenames
  