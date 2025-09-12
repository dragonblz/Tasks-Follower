from setuptools import setup, find_packages

setup(
    name="tasks-follower",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tasks-follower=tasks_follower.__main__:main"
        ]
    },
    install_requires=[],
    python_requires=">=3.7",
    author="dragonblz",
    description="A CLI to-do manager with SQLite",
)