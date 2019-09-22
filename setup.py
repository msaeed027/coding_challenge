from setuptools import find_packages, setup

setup(
    name='coding_challenge',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'rx'
    ],
    extras_require={"test": ["pytest", "coverage"]},
)