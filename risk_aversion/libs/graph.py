#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string


PATH = os.path.abspath(os.path.dirname(__file__))

UNKNOW_TEMPLATE = string.Template(
    open(os.path.join(PATH, "unknow.svg")).read())

FIFTY_FIFTY_TEMPLATE = string.Template(
    open(os.path.join(PATH, "fiftyfifty.svg")).read())


def render_fiftyfifty(left, right):
    return FIFTY_FIFTY_TEMPLATE.substitute(left=left, right=right)


def render_unknow(up, left, right):
    return UNKNOW_TEMPLATE.substitute(up=up, left=left, right=right)
