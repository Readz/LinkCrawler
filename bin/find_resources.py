#!/usr/bin/env python
"""
NAME
    app.py

DESCRIPTION
    Given a file type(s) and a URL, crawl the given website and count the 
    amount of links of the given file type(s).  The URLs found will also be 
    provided.

ARGUMENTS
    

USAGE
    

AUTHOR(S)
    Derek Frank <derek at readz dot com>

"""


###############################################################################
# IMPORTS
###############################################################################

# Stdlib.
import sys
import os
import mimetypes
from urlparse import urlparse

# 3rd Party.
from twisted.internet import reactor
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from scrapy.cmdline import execute


###############################################################################
# GLOBALS
###############################################################################

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


###############################################################################
# HELPER FUNCTIONS
###############################################################################

def get_opts(**defaults):
    from argparse import ArgumentParser, Action, ArgumentError

    # Define argparse append action that will not include defaults when option 
    # is specified.
    class DefaultListAction(Action):
        def __init__(self, *args, **kwargs):
            self.called = 0
            super(DefaultListAction, self).__init__(*args, **kwargs)

        def __call__(self, parser, namespace, values, option_string=None):
            if values:
                if self.called:
                    # Append to non-defaults (unless defaults manually added).
                    arr = getattr(namespace, self.dest)
                    arr.append(values)
                else:
                    # Override defaults.
                    setattr(namespace, self.dest, [values])
            else:
                raise argparse.ArgumentError(self, 'expected one argument')
            self.called += 1

    # Build option parser.
    #usage = 'usage: python %prog [-h,--help] [options] URL ...'
    program = 'python %s' % sys.argv[0]
    desc = ('Crawl the given website(s) and find all of the links of the given'
                ' type(s).')
    parser = ArgumentParser(prog=program, description=desc)
    # Required arguments.
    parser.add_argument(dest='start_urls', metavar='START_URL',
            type=str, nargs='+',
            help='One or more URL(s) from where the spider will start'
                    ' crawling.')
    # Secondary arguments.
    parser.add_argument('-c', '-m', '-e', '--content-type', dest='content_types', metavar='CONTENT_TYPE',
            type=str, default=defaults.get('content_types'), action=DefaultListAction,
            help=('One or more content/MIME type(s) and/or file extension(s).'
                    '\n[Default: %(default)s]'
                    '\n[Example: "-c image -m application/pdf -e .xml"]'))
    # Crawling flags.
    parser.add_argument('--ignore-sitemap', 
            default=False, action='store_true',
            help=("Do not attempt to use a website's sitemap to aid in"
                    ' crawling all links.'))
    parser.add_argument('--follow-external',
            default=False, action='store_true',
            help=('Allow spider to crawl links external to the given start URL'
                    ' domain(s). This recursive operation may go too far.'))
    parser.add_argument('--dont-follow', 
            default=False, action='store_true',
            help=('Disallow spider to crawl/follow any links found.'
                    '\nOverrides --follow-external.'
                    '\nImplicitly sets --ignore-sitemap.'))
    # List available options and exit.
    parser.add_argument('--list-content-types',
            default=False, action='store_true',
            help=('List available valid content types that encompass a group of MIME types.'))
    parser.add_argument('--list-mime-types',
            default=False, action='store_true',
            help=('List available valid MIME types with associated file extensions.'))
    parser.add_argument('--list-extensions',
            default=False, action='store_true',
            help=('List available valid extensions with associated MIME type.'))
    # Printing and debug output.
    parser.add_argument('-d', '--debug',
            default=False, action='store_true',
            help=('Debug printing will include Scrapy log output.'))

    # Parse and return the arguments.
    return parser.parse_args()

def main():
    # Helpers
    def lenCmp(s):
        return len(s)
    def colPrint(left, right, maxchars=20):
        print ('%%%ds: %%s' % maxchars) % (left, right)

    # Project imports.
    sys.path.append(PROJ)
    from resourcecrawler.spiders.resourcespider import ResourceSpider, CONTENT_TYPES, MIME_TYPES, MIME_EXTENSIONS, DEFAULT_CONTENTTYPES

    # Environment.
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'resourcecrawler.settings'

    # Options.
    opts = get_opts(content_types=DEFAULT_CONTENTTYPES)

    # Build Scrapy execute arguments from options.
    args = ['scrapy', 'crawl', 'resourcespider']
    for name, val in vars(opts).iteritems():
        if name == 'debug':
            args.extend(['-s', 'LOG_ENABLED=%d' % val])
        elif val and name == 'list_extensions':
            k, v = 'EXTENSION', 'MIMETYPE'
            maxchars = len(max(max(MIME_EXTENSIONS.iterkeys(), key=lenCmp), k, key=lenCmp))
            colPrint(k, v, maxchars)
            for ext, mime in MIME_EXTENSIONS.iteritems():
                colPrint(ext, mime, maxchars)
            sys.exit()
        elif val and name == 'list_mime_types':
            k, v = 'MIMETYPE', 'EXTENSIONS'
            maxchars = len(max(max(MIME_TYPES, key=lenCmp), k, key=lenCmp))
            colPrint('MIMETYPE', 'EXTENSIONS', maxchars)
            for ct in sorted(MIME_TYPES):
                colPrint(ct, mimetypes.guess_all_extensions(ct), maxchars)
            sys.exit()
        elif val and name == 'list_content_types':
            k, v = 'CONTENT-TYPE', 'MIMETYPES'
            maxchars = len(max(max(CONTENT_TYPES, key=lenCmp), k, key=lenCmp))
            colPrint(k, v, maxchars)
            for ct, mimes in sorted(CONTENT_TYPES.iteritems()):
                colPrint(ct, list(mimes), maxchars)
            sys.exit()
        else:
            # Add as a string representation so that it may be evaluated to its 
            # proper value in another Python context.
            args.extend(['-a', '%s=%r' % (name, val)])

    # Crawl spider.
    execute(argv=args)

    ''' # The following failed:
    # http://doc.scrapy.org/en/latest/topics/practices.html?highlight=script#run-scrapy-from-a-script
    '''


###############################################################################
# MAIN
###############################################################################

if __name__ == '__main__':
    sys.exit(main())
