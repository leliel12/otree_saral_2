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
    name_in_url = 'lie_adversion'
    players_per_group = None
    num_rounds = 1
    euros_per_toss = 5



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    tails = models.PositiveIntegerField(verbose_name="Number of tails", max=4)

    def set_payoff(self):
        self.payoff = self.tails * Constants.euros_per_toss
