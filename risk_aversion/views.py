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
                k: graph.render_fiftyfifty(*map(c, v)) for k, v in self.loteries.items()}
        }


class Screen2(Page):

    template_name = "risk_aversion/Question.html"

    form_model = models.Player
    form_fields = ['riskchoice2']
    loteries = Constants.loteries2

    def vars_for_template(self):
        return {
            "screen_number": 2,
            "graphs": {
                k: graph.render_fiftyfifty(*map(c, v)) for k, v in self.loteries.items()}
        }


class Screen3(Page):

    template_name = "risk_aversion/Question.html"

    form_model = models.Player
    form_fields = ['riskchoice3']
    loteries = Constants.loteries3

    def vars_for_template(self):
        return {
            "screen_number": 3,
            "graphs": {
                k: graph.render_unknow("?", *map(c, v)) for k, v in self.loteries.items()}
        }


class Screen4(Page):

    template_name = "risk_aversion/Question.html"

    form_model = models.Player
    form_fields = ['riskchoice4']
    loteries = Constants.loteries4

    def vars_for_template(self):
        return {
            "screen_number": 4,
            "graphs": {
                k: graph.render_unknow("?", *map(c, v)) for k, v in self.loteries.items()}
        }

    def before_next_page(self):
        self.player.set_payoff()


class Result(Page):

    def vars_for_template(self):
        sp, choice, loteries, wrange, initial_payoff = self.player.get_selected_puzzle()
        return {
            "selected_puzzle": sp, "choice": choice,
            "graphs": {k: graph.render_unknow("?", *map(c, v)) for k, v in loteries.items()},
            "lotery": loteries[choice],
            "wrange": wrange, "initial_payoff": initial_payoff}



page_sequence = [
    Screen1, Screen2, Screen3, Screen4, Result
]
