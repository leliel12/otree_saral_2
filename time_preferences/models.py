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
    name_in_url = 'time_preferences'
    players_per_group = None
    num_rounds = 1

    options = {"A": "1 month", "B": "13 months"}

    decisions = [
        {"A": 100, "B": 105.09, "air": 05, "aeir": 5.09},
        {"A": 100, "B": 110.38, "air": 10, "aeir": 10.38},
        {"A": 100, "B": 115.87, "air": 15, "aeir": 15.87},
        {"A": 100, "B": 121.55, "air": 20, "aeir": 21.55},
        {"A": 100, "B": 127.44, "air": 25, "aeir": 27.44},
        {"A": 100, "B": 133.55, "air": 30, "aeir": 33.55},
        {"A": 100, "B": 139.87, "air": 35, "aeir": 39.87},
        {"A": 100, "B": 146.41, "air": 40, "aeir": 46.41},
        {"A": 100, "B": 153.18, "air": 45, "aeir": 53.18},
        {"A": 100, "B": 160.18, "air": 50, "aeir": 60.18},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    decision1 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision2 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision3 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision4 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision5 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision6 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision7 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision8 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision9 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())
    decision10 = models.CharField(max_length=50, choices=sorted(Constants.options), widget=widgets.RadioSelectHorizontal())

    selected_decision = models.IntegerField()

    def get_decision(self):
        option = getattr(self, "decision{}".format(self.selected_decision))
        return option, Constants.options[option], Constants.decisions[self.selected_decision-1]

    def set_payoff(self):
        self.selected_decision = random.randint(1, 10)
        option, option_desc, decision = self.get_decision()
        self.payoff = decision[option]

    def fields_iterator(self):
        for idx in range(1, 11):
            yield getattr(self, "decision{}".format(idx))
