# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# Hello!
# -

def fun():
    print("fun()")
fun()

var = 7

# +
# How to kill an errant notebook server:
# first, run `jupyter notebook list` to get jupyter used port-number.
# then, run `lsof -n -i4TCP:[port-number]` to get PID (second field in the output).
# finally, run kill -9 [PID] to kill this process.
