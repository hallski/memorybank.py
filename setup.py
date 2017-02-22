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
    'install_requires': [
        'nose',
        'urwid'
    ],
    'packages': ['memorybank'],
    'scripts': [],
    'name': 'MemoryBank',
    'entry_points': {
        'console_scripts': [
            'mb = memorybank.__main__:main'
        ]
    }
}

setup(**config)
