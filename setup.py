# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    data_files = [( '.', ['urls.txt']),],
    entry_points = {'scrapy': ['settings = crawl.settings']},
    install_requires = [
        "django==2.2.27",
        "fake-factory==0.4.2",
        "requests",
        "python-dateutils==2.2"
        ]
)
