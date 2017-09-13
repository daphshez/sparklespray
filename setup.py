#!/usr/bin/env python

# need python3 or gcloud stores bad values into datastore
import sys
assert sys.version_info >= (3,)
import ast
import re
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s*=\s*(.*)')

with open('kubeque/__init__.py', 'rt') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read()).group(1)))

setup(name='kubeque',
      version=version,
      description='batch job submission front to kubernettes',
      author='Philip Montgomery',
      author_email='pmontgom@broadinstitute.org',
      install_requires=[
          'google-api-python-client',
          'google-cloud-storage==1.1.1',
          'google-cloud-datastore==1.0.0',
          'google-cloud-pubsub==0.25.0',
          'google-cloud-core==0.24.1',
          'pykube', 'attrs'
#          ,
#          "oauth2client==3.0.0" # if not specified pip will install v4+ which doesn't seem to be compatible with google-cloud
          ],
      packages=find_packages(),
      entry_points={'console_scripts': [
        "kubeque = kubeque.main:main",
        "kubeque-consume = kubeque.consume:main",
        "kubeque-reaper = kubeque.reaper:main"
        ]}
     )
