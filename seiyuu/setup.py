# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    data_files = [( '.', ['urls.txt']),],
    entry_points = {'scrapy': ['settings = crawl.settings']},
    install_requires = [
        "django==1.6.8",
        "fake-factory==0.4.2",
        "requests==2.4.3",
        "python-dateutils==2.2"
        ]
)