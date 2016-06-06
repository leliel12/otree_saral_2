# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_aversion'
    players_per_group = None
    num_rounds = 1

    loteries_choices = ["A", "B", "C", "D", "E", "F"]

    loteries1 = {
        "A": [0.5, 17.5],
        "B": [7, 7],
        "C": [6, 9],
        "D": [5, 11],
        "E": [4, 13],
        "F": [3, 15]
    }

    loteries2 = {
        "A": [-9.5, 7.5],
        "B": [-3, -3],
        "C": [-4, -1],
        "D": [-5, 1],
        "E": [-6, 3],
        "F": [-7, 5]
    }

    loteries3 = {
        "A": [0.5, 17.5],
        "B": [7, 7],
        "C": [6, 9],
        "D": [5, 11],
        "E": [4.5, 13],
        "F": [3, 15]
    }

    loteries4 = {
        "A": [-9.5, 7.5],
        "B": [-3, -3],
        "C": [-4, -1],
        "D": [-5, 1],
        "E": [-6, 3],
        "F": [-7, 5]
    }

    random_ranges = [
        [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    riskchoice1 = models.CharField(max_length=50, choices=sorted(Constants.loteries1), widget=widgets.RadioSelectHorizontal())
    riskchoice2 = models.CharField(max_length=50, choices=sorted(Constants.loteries2), widget=widgets.RadioSelectHorizontal())
    riskchoice3 = models.CharField(max_length=50, choices=sorted(Constants.loteries3), widget=widgets.RadioSelectHorizontal())
    riskchoice4 = models.CharField(max_length=50, choices=sorted(Constants.loteries4), widget=widgets.RadioSelectHorizontal())

    selected_puzzle = models.IntegerField(choices=[1, 2, 3, 4])
    wining_range = models.JSONField(default=None)
    roll = models.IntegerField()

    def get_wining_range(self):
        if not self.wining_range:
            if self.selected_puzzle in (1, 2):
                self.wining_range = [1, 5]
            elif self.selected_puzzle in (3, 4):
                self.wining_range = random.choice(Constants.random_ranges)
        return self.wining_range

    def get_selected_puzzle(self):
        initial_payoff = 0 if self.selected_puzzle in (1, 3) else 10
        if self.selected_puzzle == 1:
            return 1, self.riskchoice1, Constants.loteries1, self.get_wining_range(), initial_payoff
        if self.selected_puzzle == 2:
            return 2, self.riskchoice2, Constants.loteries2, self.get_wining_range(), initial_payoff
        if self.selected_puzzle == 3:
            return 3, self.riskchoice3, Constants.loteries3, self.get_wining_range(), initial_payoff
        return 4, self.riskchoice4, Constants.loteries4, self.get_wining_range(), initial_payoff

    def set_payoff(self):
        self.selected_puzzle = random.randint(1, 4)
        sp, choice, loteries, wrange, initial_payoff = self.get_selected_puzzle()
        lotery = loteries[choice]
        self.roll = random.randint(1, 10)
        if self.roll <= wrange[-1]:
            self.payoff = initial_payoff + lotery[0]
        else:
            self.payoff = initial_payoff + lotery[1]


