try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'name': 'ResourceCrawler'
    'version': '0.1',
    'author': 'Derek Frank',
    'author_email': 'derek at readz dot com',
    'description': ('Crawl specified website(s) and gather resource information '
                        'filtered by file extension.'),
    'license': 'MIT',
    'keywords': 'webcrawler spider crawl resources',
    'url': 'https://github.com/Readz/LinkCrawler',
    'download_url': 'https://github.com/Readz/LinkCrawler.git',
    'install_requires': [
        'setuptools', 
        'nose', 
        'service-identity', 
        'pyOpenSSL', 
        'twisted', 
        'Scrapy',
    ],
    'packages': ['resourcecrawler', 'tests'],
    'long_description': read('README.md'),
    'scripts': ['bin/find_resources'],
}

setup(**config)
