from setuptools import setup, find_packages

setup(
    name='geovalidator',
    version='0.1.0',
    description='Geospatial Data Validator',
    author='daameya',
    author_email='1998ameya@gmail.com',
    packages=find_packages(),
    install_requires=[
        'geopandas',
        'shapely',
        'pyproj',
        'fiona',
    ],
)