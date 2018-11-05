import os
import sys

from aleph.aleph_cli.utils.generator_exception import GeneratorException

def exit_if_not_aleph_project():
  """
  Checks to see if we are executing the aleph command within an aleph project
  and raises an exception if we are not
  """

  root_path = os.getcwd()
  if not os.path.isdir(os.path.join(root_path, '.aleph')):
    raise GeneratorException(f'Error: This is not an aleph project directory. Aleph commands must be run in an aleph project directory.')

def activate_project_environment():
  """
  If the aleph command is not being run in the project's virtual environment, then
  activate the project's virtual environment
  """

  root_path = os.getcwd()
  name = os.path.basename(root_path)
  env_path = os.path.join(root_path, f'.{name}-environment')

  if not env_path in sys.prefix:
    activate_this_path = os.path.join(os.path.join(env_path, 'bin'), 'activate_this.py')
    execfile(activate_this_path)

def execfile(filepath, globals=None, locals=None):
  """
  A python3 replacement for execfile, allowing us to set the active virtual environment rather than
  a subprocess's virtual environment
  """

  if globals is None:
    globals = {}

  globals.update({
    "__file__": filepath,
    "__name__": "__main__",
  })

  with open(filepath, 'rb') as file:
    exec(compile(file.read(), filepath, 'exec'), globals, locals)