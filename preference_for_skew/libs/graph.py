#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string

import pygal
from pygal.style import Style


PATH = os.path.abspath(os.path.dirname(__file__))

SQUARE_PATH = os.path.join(PATH, "square.svg")

SQUARE_TEMPLATE = string.Template(open(SQUARE_PATH).read())


def render(data, labels, title, colors):
    custom_style = Style(colors=colors)

    pie_chart = pygal.Pie(style=custom_style)
    pie_chart.title = title
    for label, serie in zip(labels, data):
        pie_chart.add(label, serie)

    squares = [SQUARE_TEMPLATE.substitute(color=color) for color in colors]

    return pie_chart.render(disable_xml_declaration=True), squares




