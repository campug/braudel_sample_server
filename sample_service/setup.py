from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='sample_service',
      version=version,
      description="Sample Win32 Service",
      long_description="""\
Sample package to deploy a twisted-xmlrpc server as a win32 service""",
      classifiers=[], 
      keywords='',
      author='B Maqueira',
      author_email='braudel@ferrarihaines.com',
      url='http://codelab.ferrarihaines.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'pywin32', 'wmi', 'twisted', 'zope.interface'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      scripts=[
        'scripts/proclist_service.py'
      ],
      )
