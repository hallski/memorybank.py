try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Persistent memory storage',
    'author': 'Mikael Hallendal',
    'url': 'http://hallski.org/',
    'download_url': 'http://hallski.org',
    'author_email': 'hallski@hallski.org',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['memorybank'],
    'scripts': [],
    'name': 'MemoryBank'
}

setup(**config)
