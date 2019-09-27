from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'pelican_minify',
    version = '1.1',
    py_modules = ('pelican_minify',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['htmlmin>=0.1.5', 'pelican>=4.0.0' ],

    # Metadata for PyPI:
    author = 'Luke Hollins',
    author_email = 'luke@farcry.ca',
    license = 'AGPL',
    url = 'https://github.com/lwh/pelican_minify',
    keywords = 'pelican blog static minify html minification',
    description = ('An HTML minification plugin for Pelican, the static '
            'site generator.'),
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
