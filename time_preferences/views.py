# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Question(Page):
    form_model = models.Player
    form_fields = ['decision1', 'decision2', 'decision3', 'decision4', 'decision5', 'decision6', 'decision7', 'decision8', 'decision9', 'decision10']

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):

    def vars_for_template(self):
        option, option_desc, decision = self.player.get_decision()
        return {"option": option, "option_desc": option_desc, "desicion": decision}



page_sequence = [
    Instructions, Question, Results
]
