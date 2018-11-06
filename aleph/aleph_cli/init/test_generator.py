import os
import shutil
import tempfile
import types
import unittest

from . import generator

class InitGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.debug = os.environ.get('DEBUG', '').lower()
        self.work_dir = tempfile.mkdtemp(prefix='aleph_tests_')
        print('Working directory:', self.work_dir)
        self.cwd = os.getcwd()
        os.chdir(self.work_dir)

    def tearDown(self):
        os.chdir(self.cwd)
        if self.debug != 'true':
            shutil.rmtree(self.work_dir)
        else:
            print('Saving directory for {}: {}'.format(self.__class__.__name__, self.work_dir))

    def test_generate_1(self):
        args = types.SimpleNamespace(name='test_project')
        generator.run(args)
        project_dir = os.path.join(self.work_dir, args.name)
        contents = os.scandir(project_dir)
        expected_subdirectories = {
            '.aleph',
            'datasets',
            'features',
            'labels',
            'models',
            'optimizers',
            '.{}-environment'.format(args.name)
        }
        actual_subdirectories = {
            entry.name for entry in contents if entry.is_dir(follow_symlinks=False)
        }

        self.assertSetEqual(actual_subdirectories, expected_subdirectories)

if __name__ == '__main__':
    unittest.main()