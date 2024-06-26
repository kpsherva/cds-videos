# -*- coding: utf-8 -*-
#
# This file is part of CERN Document Server.
# Copyright (C) 2015, 2016, 2017, 2018, 2019, 2020 CERN.
#
# CERN Document Server is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Document Server is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Document Server; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""CDS, Access articles, reports and multimedia content in HEP.

Links
-----
* `website <http://cds.cern.ch/>`_
* `development version <https://github.com/CERNDocumentServer/cds-videos>`_
"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'mock>=1.3.0',
    'pydocstyle>=1.0.0',
    'pytest-cov>=1.8.0',
    'pytest-flask>=0.10.0<1.2.0',
    'pytest-pep8>=1.0.6',
    'pytest-runner>=2.7.0',
    'pytest>=5.2,<6.0',
    'pluggy>=0.7.0',
    'selenium>=2.53.6',
    'simplejson>=3.10',
    'six>=1.10.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.3',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    extras_require['all'].extend(reqs)

# Do not include in all requirement
extras_require['xrootd'] = [
    'invenio-xrootd>=1.0.0a4',
    'xrootdpyfs>=0.1.5',
]

setup_requires = [
    'Babel>=2.4.0',
    'Flask-BabelEx>=0.9.3',
]

install_requires = [
    'invenio[base,auth,metadata,files,postgresql,elasticsearch2]==3.2.1',  # 3.2.2 removes support for Python 2.7
    # pin some invenio 3.2.x packages because of versions conflicts
    'invenio-db[postgresql,versioning]==1.0.4',  # 1.0.5 dropped Python 2
    'invenio-base==1.2.3',
    'invenio-oauth2server==1.0.4',
    # extras
    'arrow>=0.7.0,<1.0.0',
    'CairoSVG>=1.0.20,<2.0.0',
    'datacite==1.0.1',
    'dcxml==0.1.1',
    'dictdiffer<0.9.0',
    'Flask>=1.0.4,<2.0',
    'Flask-Breadcrumbs<0.5.0',
    'flask-caching<1.8.0',
    'flask-debugtoolbar>0.10.1',
    'Flask-Login>=0.3.0,<0.5.0',
    'flask-sqlalchemy<2.5.0',
    'idutils==0.2.3',
    'invenio-formatter[badges]>=1.0.2,<1.1.0',
    'invenio-opendefinition==1.0.0a8',
    'invenio-pages==1.0.0a4',
    'invenio-sequencegenerator==1.0.0a2',
    'jsonresolver>=0.2.1,<0.3.0',
    'raven>=6.6.0',
    'redis>=2.10.0,<3.0.0',
    'requests-toolbelt>=0.9.1',
    'SQLAlchemy>=1.0,<1.4.0',
    'urllib3[secure]>=1.24.2,<2.0.0',    # urllib3 doesn't install pyOpenSSl by default and thus the [secure] extra is needed
    'WTForms-Alchemy<0.17.0',
    "python-ldap>=3.4.0,<3.5.0",
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("cds", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name='CDS',
    version=version,
    description='Access articles, reports and multimedia content in HEP',
    long_description=readme + '\n\n' + history,
    license='GPLv3',
    author='CERN',
    author_email='cds.support@cern.ch',
    url='http://cds.cern.ch/',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'cds = invenio_app.cli:cli',
        ],
        'flask.commands': [
            'subformats = cds.modules.maintenance.cli:subformats',
            'videos = cds.modules.maintenance.cli:videos',
        ],
        'invenio_admin.views': [
            'cds_admin = '
            'cds.modules.announcements.admin:announcements_adminview',
            'invenio_flows_flow = cds.modules.flows.admin:flow_model_view',
            'invenio_flows_task = cds.modules.flows.admin:task_model_view',
        ],
        'invenio_assets.bundles': [
            'cds_deposit_jquery_js = cds.modules.deposit.bundles:js_jquery',
            'cds_deposit_js = cds.modules.deposit.bundles:js_deposit',
            'cds_deposit_common_js = '
            'cds.modules.deposit.bundles:js_deposit_common',
            'cds_previewer_video_css = '
            'cds.modules.previewer.bundles:video_css',
            'cds_record_js = cds.modules.records.bundles:js',
            'cds_search_ui_js = cds.modules.search_ui.bundles:js',
            'cds_theme_css = cds.modules.theme.bundles:css',
            'cds_theme_js = cds.modules.theme.bundles:js',
            'cds_record_stats_js = cds.modules.records.bundles:stats_js',
            'cds_record_stats_css = cds.modules.records.bundles:stats_css',
        ],
        'invenio_base.api_apps': [
            'cds_deposit = cds.modules.deposit.ext:CDSDepositApp',
            'cds_files_rest = cds.modules.files.ext:CDSFilesRestApp',
            'cds_xrootd = cds.modules.xrootd:CDSXRootD',
        ],
        'invenio_base.api_blueprints': [
            'cds_records = cds.modules.records.views:blueprint',
            'cds_stats = cds.modules.stats.views:blueprint',
            'cds_redirector = cds.modules.redirector.views:api_blueprint',
            'cds_announcements = '
            'cds.modules.announcements.views:api_blueprint',
            'cds_flows = cds.modules.flows.views:blueprint',
            'cds_ldap = cds.modules.ldap.views:blueprint',
        ],
        'invenio_base.apps': [
            'cds_deposit = cds.modules.deposit.ext:CDSDepositApp',
            'cds_main_fixtures = cds.modules.fixtures:CDSFixtures',
            'cds_xrootd = cds.modules.xrootd:CDSXRootD',
        ],
        'invenio_base.blueprints': [
            'cds_deposit = cds.modules.deposit.views:blueprint',
            'cds_home = cds.modules.home.views:blueprint',
            'cds_previewer = cds.modules.previewer.views:blueprint',
            'cds_records = cds.modules.records.views:blueprint',
            'cds_search_ui = cds.modules.search_ui.views:blueprint',
            'cds_theme = cds.modules.theme.views:blueprint',
            'cds_redirector = cds.modules.redirector.views:blueprint',
            'cern_oauth = cds.modules.oauthclient.cern_openid:cern_openid_blueprint',
        ],
        'invenio_config.module': [
            'cds = cds.config',
        ],
        'invenio_db.alembic': [
            'cds_announcements = cds.modules.announcements:alembic',
            'invenio_flows = cds.modules.flows:alembic',
        ],
        'invenio_jsonschemas.schemas': [
            'deposit = cds.modules.deposit.schemas',
            'record = cds.modules.records.schemas',
        ],
        'invenio_pidstore.fetchers': [
            'cds_recid = cds.modules.records.fetchers:recid_fetcher',
            'cds_catid = cds.modules.records.fetchers:catid_fetcher',
            'cds_kwid = cds.modules.records.fetchers:kwid_fetcher',
        ],
        'invenio_pidstore.minters': [
            'cds_catid = cds.modules.records.minters:catid_minter',
            'cds_kwid = cds.modules.records.minters:kwid_minter',
            'cds_report_number = '
            'cds.modules.records.minters:report_number_minter',
            'cds_recid = cds.modules.records.minters:cds_record_minter',
        ],
        'invenio_search.mappings': [
            'records = cds.modules.records.mappings',
            'deposits = cds.modules.deposit.mappings',
            'categories = cds.modules.records.mappings',
            'keywords = cds.modules.records.mappings',
        ],
        'invenio_celery.tasks': [
            'cds_celery_tasks = cds.modules.flows.tasks',
            'cds_deposit_tasks = cds.modules.deposit',
            'cds_opencast_tasks = cds.modules.opencast.tasks',
            'cds_records_tasks = cds.modules.records',
            'cds_maintenance = cds.modules.maintenance.tasks',
        ],
        'invenio_previewer.previewers': [
            'cds_video = cds.modules.previewer.extensions.video:video',
            'cds_embed_video = '
            'cds.modules.previewer.extensions.video:embed_video',
            'cds_deposit_video = '
            'cds.modules.previewer.extensions.video:deposit_video',
            'cds_default = cds.modules.previewer.extensions.default',
        ],
        'invenio_records.jsonresolver': [
            'keywords = cds.modules.records.jsonresolver.keywords',
            'records = cds.modules.records.jsonresolver.records',
            'deposits = cds.modules.deposit.jsonresolver',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 2 - Pre-Alpha',
    ],
)
