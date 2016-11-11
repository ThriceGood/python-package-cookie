from setuptools import setup, find_packages
import os.path

def read_requirements(pathname):
    with open(pathname) as f:
        return [line for line in (x.strip() for x in f) if not line.startswith('#')]

def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='{{cookiecutter.package_name}}',
    version='0.1.0',

    install_requires=read_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt')),

    test_suite='nose.collector',

    entry_points={
        'console_scripts': [
        ],
    },
    url='',
    author='{{cookiecutter.package_author}}',
    author_email='',
    classifiers=["Programming Language :: Python :: {{cookiecutter.python_version}}"],
    description=__doc__,
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
            'README.md',
            )),
    zip_safe=False,
    include_package_data=True,
    packages=find_packages()
    )
