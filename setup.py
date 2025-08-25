from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI_travel_agent",
    version="0.1",
    author="Reeshma Ram Prasad",
    packages=find_packages(),
    install_requires=requirements,
)
