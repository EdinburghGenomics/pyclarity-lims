from setuptools import setup, find_packages
import sys, os
import subprocess
import glob

# Fetch version from git tags.
# if git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'genologics', 'version.py')



version = subprocess.Popen(["git", "describe", "--abbrev=0"],stdout=subprocess.PIPE).communicate()[0].rstrip()
if not version:
    #This set the __version__
    with open(version_py) as f:
        code = compile(f.read(), version_py, 'exec')
        exec(code)
    version = __version__


setup(name='genologics',
      version=version,
      description="Python interface to the GenoLogics LIMS (Laboratory Information Management System) server via its REST API.",
      long_description="""A basic module for interacting with the GenoLogics LIMS server via its REST API.
                          The goal is to provide simple access to the most common entities and their attributes in a reasonably Pythonic fashion.""",
      classifiers=[
	"Development Status :: 4 - Beta",
	"Environment :: Console",
	"Intended Audience :: Developers",
	"Intended Audience :: Healthcare Industry",
	"Intended Audience :: Science/Research",
	"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
	"Operating System :: POSIX :: Linux",
	"Programming Language :: Python",
	"Topic :: Scientific/Engineering :: Medical Science Apps."
	],
      keywords='genologics api rest',
      author='Per Kraulis',
      author_email='per.kraulis@scilifelab.se',
      maintainer='Denis Moreno',
      maintainer_email='denis.moreno@scilifelab.se',
      url='https://github.com/scilifelab/genologics',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      #scripts=glob.glob("scripts/*.py"),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "requests"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
