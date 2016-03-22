# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from .libs import graph


class Screen1(Page):

    form_model = models.Player
    form_fields = ['skewchoice1']

    def vars_for_template(self):
        return {"graph": graph.render(**Constants.pie_conf)}


page_sequence = [
    Screen1,
    #~ Results
]
