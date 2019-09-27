from subprocess import check_call
from htmlmin import minify
import logging
import os

logger = logging.getLogger(__name__)

"""
Minify HTML
"""

def minify_html(pelican):
    """Minify all HTML files.

    :param pelican: The Pelican instance.
    """
    options = pelican.settings.get('MINIFY', {})
    files_to_minify = []

    for dirpath, _, filenames in os.walk(pelican.settings['OUTPUT_PATH']):
        files_to_minify += [os.path.join(dirpath, name) for name in filenames if name.endswith('.html') or name.endswith('.htm')]

    for filepath in files_to_minify:
        create_minified_file(filepath, options)


def create_minified_file(filename, options):
    """Create a minified HTML file, overwriting the original.

    :param str filename: The file to minify.
    """
    uncompressed = open(filename).read()

    with open(filename, 'w') as f:
        try:
            logger.debug('Minifying: %s' % filename)
            compressed = minify(uncompressed, **options)
            f.write(compressed)
        except Exception as ex:
            logger.critical('HTML Minification failed: %s' % ex)
        finally:
            f.close()


def register():
    signals.finalized.connect(minify_html)
