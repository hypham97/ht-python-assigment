#!/usr/bin/env python
import os
from subprocess import getoutput

prg = "program.py"

# -------------------------------------------------


def testExists():
    assert os.path.isfile(prg)

# ------------------------------------------------


def test_one():
    numbers = 1
    pattern = "SST"
    expected = "Soft."
    out = getoutput(f'python {prg} {pattern} {numbers}')
    assert out.strip() == expected


def test_two():
    numbers = 2
    pattern = "SST"
    expected = "Soft and Soft."
    out = getoutput(f'python {prg} {pattern} {numbers}')
    assert out.strip() == expected


def test_more_than_two():
    numbers = 5
    pattern = "SST"
    expected = "Soft, Soft, Tough, Soft and Soft."
    out = getoutput(f'python {prg} {pattern} {numbers}')
    assert out.strip() == expected


def test_invalid_number():
    numbers = -1
    pattern = "SST"
    try:
        out = getoutput(f'python {prg} {pattern} {numbers}')
        assert False
    except Exception:
        assert True


def test_invalid_pattern():
    numbers = 1
    pattern = "ab"
    try:
        out = getoutput(f'python {prg} {pattern} {numbers}')
        assert False
    except Exception:
        assert True


def test_lower_pattern():
    numbers = 1
    pattern = "st"
    try:
        out = getoutput(f'python {prg} {pattern} {numbers}')
        assert False
    except Exception:
        assert True
