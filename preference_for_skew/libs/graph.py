#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygal


def render(data, labels, title):
    pie_chart = pygal.Pie()
    pie_chart.title = title
    for label, serie in zip(labels, data):
        pie_chart.add(label, serie)
    return pie_chart.render(disable_xml_declaration=True)

