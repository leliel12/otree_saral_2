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
    name_in_url = 'Task 3'
    players_per_group = None
    num_rounds = 1
    pie_data = [50, 49, 1]
    pie_conf = {
        "data": pie_data,
        "labels": ["{}%".format(d) for d in pie_data],
        "colors": ['#EE9095', '#90EE90', '#AB90EE']
    }
    skew_choices = ["A", "B", "C", "D", "E", "F"]

    skewchoices1 = {
        'A': [1.0, 1.0, 1.0],
        'B': [0.6, 1.8, 1.8],
        'C': [0.2, 2.6, 2.6],
        'D': [-0.2, 3.4, 3.4],
        'E': [-0.6, 4.2, 4.2],
        'F': [-1.2, 4.8, 4.8]
    }

    skewchoices2 = {
        'A': [1., 1., 1.,],
        'B': [0.65, 1.71, 4.07],
        'C': [0.3, 2.41, 7.15],
        'D': [-0.06, 3.12, 10.22],
        'E': [-0.41, 3.82, 13.29],
        'F': [-0.96, 4.33, 16.17]
    }

    skewchoices3 = {
        'A': [1.0, 1.0, 1.0],
        'B': [0.69, 1.65, 4.77],
        'C': [0.37, 2.30, 8.54],
        'D': [0.06, 2.96, 12.31],
        'E': [-0.26, 3.61, 16.08],
        'F': [-0.77, 4.06, 19.65]
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    skewchoice1 = models.CharField(max_length=50, choices=sorted(Constants.skewchoices1), widget=widgets.RadioSelectHorizontal())
    skewchoice2 = models.CharField(max_length=50, choices=sorted(Constants.skewchoices2), widget=widgets.RadioSelectHorizontal(), null=True, blank=True)
    skewchoice3 = models.CharField(max_length=50, choices=sorted(Constants.skewchoices3), widget=widgets.RadioSelectHorizontal(), null=True, blank=True)

    winning_choice = models.IntegerField()

    def selected_skew(self):
        if self.skewchoice3:
            return 3, self.skewchoice3, Constants.skewchoices3[self.skewchoice3]
        if self.skewchoice2:
            return 2, self.skewchoice2, Constants.skewchoices2[self.skewchoice2]
        return 1, self.skewchoice1, Constants.skewchoices1[self.skewchoice1]

    def set_payoff(self):
        snum, soption, choices = self.selected_skew()

        sample = []
        for idx, e in enumerate(Constants.pie_data):
            sample.extend([idx] * e)

        self.winning_choice = random.choice(sample)
        self.payoff = choices[self.winning_choice]
