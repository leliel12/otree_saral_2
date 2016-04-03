#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string

from otree.common import Currency as c

PATH = os.path.abspath(os.path.dirname(__file__))

UNKNOW_TEMPLATE = string.Template(
    open(os.path.join(PATH, "unknow.svg")).read())

FIFTY_FIFTY_TEMPLATE = string.Template(
    open(os.path.join(PATH, "fiftyfifty.svg")).read())


def render_fiftyfifty(left, right):
    src = FIFTY_FIFTY_TEMPLATE.safe_substitute(left=c(left), right=c(right))
    return src


def render_unknow(up, left, right):
    return UNKNOW_TEMPLATE.substitute(up=up, left=left, right=right)
