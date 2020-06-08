#!/usr/bin/env python
"""Run notebooks.

"""
import subprocess as sp
import glob
import os


def run_notebook(notebook):
    cmd = " jupyter nbconvert --execute {}  --ExecutePreprocessor.timeout=-1".format(
        notebook
    )
    sp.check_call(cmd, shell=True)


if __name__ == "__main__":

    for fname in glob.glob("*.ipynb"):
        print(f"\n {os.getcwd().split('/')[-1]}\n")
        run_notebook(fname)
