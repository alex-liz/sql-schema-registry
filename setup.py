from setuptools import find_packages, setup
setup(
    name='sql_schema_registry',
    packages=find_packages(include=['sql_schema_registry']),
    version='0.1.1',
    description='Schema registry',
    author='Alejandro Liz',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)