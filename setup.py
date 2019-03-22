"""
    Pivot Security Python API is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    Pivot Security Python API is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pyrest.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

setup(
    name='pcspython',
    version='0.1.0',
    author='Pivot Security',
    author_email='github@pivotsecurity.com',
    maintainer='Pivot Security',
    maintainer_email='github@pivotsecurity.com',
    url='https://github.com/Pivotsecurity/pivotsecurity-python',
    description='Pivot Security Python API for Pivot Security',
    long_description=(
        """
        Pivot Security Python API Wrapper to sit between your API Resources
        and your own package API Wrapper
        """
    ),
    download_url='https://github.com/Pivotsecurity/pivotsecurity-python/archive/master.zip',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Package',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    py_modules=['api'],
)
