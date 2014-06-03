# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages


version = __import__('admin_model_report').__version__


LONG_DESCRIPTION = """
django-admin-model-report
===================

django admin reports integrated with highcharts

    $ git clone git@github.com:verdanmahmood/django-admin-model-report.git
"""


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-admin-model-report',
      version=version,
      author='juanpex',
      author_email='jpma55@gmail.com',
      description='Django reports integrated with highcharts.',
      license='BSD',
      keywords='django, model, django admin, report, reports, highcharts, chart, charts',
      url='https://github.com/juanpex/django-model-report',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      long_description=long_description(),
      install_requires=[
        'django>=1.5.5',
        'reportlab',
        'html5lib',
        'BeautifulSoup',
        'xhtml2pdf',
        'xlwt==0.7.4',
      ],
      classifiers=['Framework :: Django',
                   'Development Status :: 3 - Alpha',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7'])
