# vidtoolz-apply-greenscreen

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-apply-greenscreen.svg)](https://pypi.org/project/vidtoolz-apply-greenscreen/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-apply-greenscreen?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-apply-greenscreen/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-apply-greenscreen/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-apply-greenscreen/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-apply-greenscreen/blob/main/LICENSE)

Apply greenscreen video on top of a video

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-apply-greenscreen
```
## Usage

type ``vidtoolz-apply-greenscreen --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-apply-greenscreen
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
