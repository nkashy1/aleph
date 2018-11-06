from setuptools import setup

setup(
  name='aleph',
  version='0.0.1',
  description='Machine learning application builder',
  url='https://github.com/doc-ai/aleph',
  author='doc.ai',
  license='Apache 2',
  packages=[
    'aleph',
    'aleph.aleph_cli',
    'aleph.aleph_cli.init',
    'aleph.aleph_cli.init.templates',
    'aleph.aleph_cli.datasets',
    'aleph.aleph_cli.datasets.templates',
    'aleph.aleph_cli.features',
    'aleph.aleph_cli.features.templates',
    'aleph.aleph_cli.labels',
    'aleph.aleph_cli.labels.templates',
    'aleph.aleph_cli.models',
    'aleph.aleph_cli.models.templates',
    'aleph.aleph_cli.optimizers',
    'aleph.aleph_cli.optimizers.templates',
    'aleph.aleph_cli.train',
    'aleph.aleph_cli.utils',
  ],
  package_data={
    '': ['*.jinja2']
  },
  zip_safe=False,
  install_requires=[
    'virtualenv',
    'termcolor'
  ],
  entry_points={
    'console_scripts': ['aleph=aleph.cli:main']
  }
)