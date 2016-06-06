# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


class Question(Page):

    form_model = models.Player
    form_fields = ["name", "email"]


page_sequence = [Question]
