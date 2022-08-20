# datasette-spotify-embed

[![PyPI](https://img.shields.io/pypi/v/datasette-spotify-embed.svg)](https://pypi.org/project/datasette-spotify-embed/)
[![Changelog](https://img.shields.io/github/v/release/chekos/datasette-spotify-embed?include_prereleases&label=changelog)](https://github.com/chekos/datasette-spotify-embed/releases)
[![Tests](https://github.com/chekos/datasette-spotify-embed/workflows/Test/badge.svg)](https://github.com/chekos/datasette-spotify-embed/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/chekos/datasette-spotify-embed/blob/main/LICENSE)

Turn Spotify track URIs into iframe embeds in the Datasette interface

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-spotify-embed

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-spotify-embed
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
