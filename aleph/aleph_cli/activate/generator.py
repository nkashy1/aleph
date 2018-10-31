from aleph.aleph_cli.utils.aleph_filesystem import exit_if_not_aleph_project
from aleph.aleph_cli.utils.aleph_filesystem import activate_project_environment

# Present only for testing at the moment
# We won't actually be requiring the user to explicitly activate or deactivate the environment
# because we cannot set the environment in the superprocess anyway, so we'll always call
# ```
# exit_if_not_aleph_project()
# activate_project_environment()
# ```
# before running any command and place our import statements after them
# for actual project python files that get run by commands, it shouldn't matter where the import statements go
# because we'll already have activated the environment

def run(args):

  exit_if_not_aleph_project()
  activate_project_environment()

  if args.command == 'activate':
    run_activate()
  if args.command == 'deactivate':
    run_deactivate()

def run_activate():
  print('activating')

def run_deactivate():
  print('deactivating')