from setuptools import setup
import os

VERSION = "0.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-spotify-embed",
    description="Turn Spotify track links into iframe embeds in the Datasette interface",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Sergio Sánchez Zavala",
    url="https://github.com/chekos/datasette-spotify-embed",
    project_urls={
        "Issues": "https://github.com/chekos/datasette-spotify-embed/issues",
        "CI": "https://github.com/chekos/datasette-spotify-embed/actions",
        "Changelog": "https://github.com/chekos/datasette-spotify-embed/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_spotify_embed"],
    entry_points={"datasette": ["spotify_embed = datasette_spotify_embed"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "sqlite-utils"]},
    python_requires=">=3.7",
)
