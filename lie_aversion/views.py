# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Question(Page):

    form_model = models.Player
    form_fields = ['tails']

    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):
    pass


page_sequence = [
    Introduction,
    Question,
    Results
]
