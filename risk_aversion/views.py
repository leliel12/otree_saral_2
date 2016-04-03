# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from .libs import graph


class Screen1(Page):

    template_name = "risk_aversion/Question.html"

    form_model = models.Player
    form_fields = ['riskchoice1']
    loteries = Constants.loteries1

    def vars_for_template(self):
        return {
            "screen_number": 1,
            "graphs": {
                k: graph.render_fiftyfifty(*v) for k, v in self.loteries.items()}
        }


page_sequence = [
    Screen1,

]
