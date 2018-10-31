from setuptools import setup

setup(
  name='aleph',
  version='0.0.1',
  description='Machine learning application builder',
  url='https://github.com/doc-ai/aleph',
  author='doc.ai',
  license='Apache 2',
  # packages=setuptools.find_packages(), #['aleph'],
  packages=[
    'aleph',
    'aleph.aleph_cli',
    'aleph.aleph_cli.init',
    'aleph.aleph_cli.activate',
    'aleph.aleph_cli.dataset',
    'aleph.aleph_cli.utils'
  ],
  zip_safe=False,
  install_requires=[
    'virtualenv'
  ],
  entry_points={
    'console_scripts': ['aleph=aleph.cli:main']
  }
)