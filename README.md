# Python Programming Assignment

[![python version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)](https://www.python.org/downloads/)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The ht-python-assignment repo contains the solution requested.

## 📃 Table of Contents

- [🛠️ Install](#🛠️-install)
  - [📖 Prerequisites](#📖-prerequisites)
  - [🖥️ Local installation](#🖥️-local-installation)
- [🔬 Usage](#🔬-usage)
- [👨‍💻 Run](#👨‍💻-run)
- [🧪 Test](#🧪-test)

## 🛠️ Install

### 📖 Prerequisites

- [Python](https://www.python.org/): I recommend using the official binaries provided by the Python Software Foundation.

### 🖥️ Local installation

There are no dependencies, so you don't need to pip install anything.

## 🔬 Usage

Running the python script with at least two arguments:

- The first argument is a random pattern consisting only of characters S and T. For example 'STTTS'.
- The following arguments are N (N >= 1) number of integers. For example 1 5 8. Each integer is separated from previous one with a space.

Character mapping to text:

    S = Soft
    T = Tough

## 👨‍💻 Run

```shell
# Run script
./program.py SST 5 2
```

```shell
# Output
Soft, Soft, Tough, Soft and Soft.
Soft and Soft.
```

## 🧪 Test

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

```shell
# Run all tests
pytest -xv test.py
```

#### Results

![Test Results](/IMG/test_result.JPG?raw=true)
