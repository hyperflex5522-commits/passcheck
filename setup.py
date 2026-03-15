from setuptools import setup, find_packages

setup(
    name="passcheck",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "passcheck=passcheck.main:main"
        ]
    },
)
