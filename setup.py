try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'FreeSpeech',
    version = '0.2',
    author = 'Rui Lima',
    author_email = 'ruirochalima1@gmail.com',
    license = 'GPLv2',
    description = 'It creates random speach.',
    url = 'https://github.com/equidna/FreeSpeech',
    download_url = 'https://github.com/equidna/FreeSpeech/tarball/0.2',
    keywords = ['fake', 'content', 'creation'],
    packages = ['FreeSpeech'],
    install_requires = ['fake-factory'],
    classifiers=['Environment :: Console', 'Development Status :: 4 - Beta',
                    'Intended Audience :: Science/Research',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2.7',],
)
