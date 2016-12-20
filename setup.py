from distutils.core import setup

setup(
    name='viridis-hex',
    version='0.1',
    packages=[''],
    url='https://github.com/lstmemery/viridis-hex',
    license='MIT',
    author='lstmemery',
    requires=['pytest', 'matplotlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    author_email='matthew.emery44@gmail.com',
    description='Get the Viridis Colormap in Hexcode'
)
