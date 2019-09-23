from setuptools import find_packages, setup

setup(
    name='coding_challenge',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask==1.1.1',
        'rx==3.0.1',
    ],
    extras_require={
        "test": [
            "pytest==5.1.3",
            "coverage==4.5.4",
        ]
    },
)