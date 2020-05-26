#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="pipelinewise-tap-google-analytics",
    version="1.1.0",
    description="Singer.io tap for extracting data from the Google Analytics Reporting API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Meltano Team & Contributors',
    url="https://gitlab.com/transferwise/pipelinewise-tap-google-analytics",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_google_analytics"],
    install_requires=[
        "pipelinewise-singer-python==1.*",
        "google-api-python-client==1.7.9",
        "oauth2client==4.1.3",
        "backoff==1.3.2"
    ],
    entry_points="""
        [console_scripts]
        tap-google-analytics=tap_google_analytics:main
    """,
    packages=["tap_google_analytics"],
    package_data = {
      'tap_google_analytics/defaults': [
        "default_report_definition.json",
      ],
    },
    include_package_data=True,
)