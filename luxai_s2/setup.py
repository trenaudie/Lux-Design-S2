import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
setup(
    name="luxai-s2",
    author="Lux AI Challenge",
    description="The Lux AI Challenge Season 2",
    license="MIT",
    keywords="reinforcement-learning machine-learning ai",
    url="https://github.com/Lux-AI-Challenge/Lux-Design-S2",
    long_description="Code for the Lux AI Challenge Season 2",
    packages=find_packages(exclude="kits"),
    entry_points={"console_scripts": ["luxai-s2 = luxai_runner.cli:main"]},
    version=get_version("luxai_s2/version.py"),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pygame",
        "termcolor",
        "matplotlib",
        "pettingzoo",
        # "vec_noise",
        "gymnasium",
        "scipy",
    ],
)
