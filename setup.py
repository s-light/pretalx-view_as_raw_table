import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(
        os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8'
    ) as f:
        long_description = f.read()
except Exception:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1, interactive=False)
        build.run(self)


cmdclass = {'build': CustomBuild}


setup(
    name='pretalx-view_as_raw_table',
    version='0.0.0',
    description="pretalx plugin to view submissions / talks as real raw tabular data (copy and paste friendly ;-) )",
    long_description=long_description,
    url='git@github.com:s-light/pretalx-view_as_raw_table.git',
    author='Stefan Krüger',
    author_email='git@s-light.eu',
    license='Apache Software License',
    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretalx.plugin]
pretalx_view_as_raw_table=pretalx_view_as_raw_table:PretalxPluginMeta
""",
)
