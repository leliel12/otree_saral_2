# -*- coding: utf-8 -*-
from __future__ import division

from collections import OrderedDict

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from .libs import graph


class AbstractScreen(object):

    def get_choices(self, squares):
        choices = []
        for cgroup in self.choices_groups:
            cdict = OrderedDict()
            for clabel, clist in sorted(cgroup.items()):
                cdict[clabel] = list(zip(squares, clist))
            choices.append(cdict)
        return choices


class Screen1(Page, AbstractScreen):

    template_name = "preference_for_skew/Question.html"

    form_model = models.Player
    form_fields = ['skewchoice1']
    choices_groups = (Constants.skewchoices1,)

    def vars_for_template(self):
        pie, squares = graph.render(title="Please Choose your most preferred gamble", **Constants.pie_conf)
        choices = self.get_choices(squares)
        return {
            "screen_number": 1,
            "subtitle": "Individuals makes a choice of wich lottery A-F",
            "graph": pie,
            "choices": choices}


class Screen2(Page, AbstractScreen):

    template_name = "preference_for_skew/Question.html"

    form_model = models.Player
    form_fields = ['skewchoice2']
    choices_groups = (Constants.skewchoices1, Constants.skewchoices2)

    def vars_for_template(self):
        pie, squares = graph.render(
            title="Below you can see the choice you mae previously, and Gamble Set 2. Please Choose your most preferred gamble",
            **Constants.pie_conf)
        choices = self.get_choices(squares)
        selected = [self.player.skewchoice1]
        return {
            "screen_number": 2,
            "subtitle": "Individual makes another choice of which lottery A-F, with new values. Can choose new lottery or keep original choice",
            "graph": pie,
            "choices": choices,
            "selected": selected}


class Screen3(Page, AbstractScreen):

    template_name = "preference_for_skew/Question.html"

    form_model = models.Player
    form_fields = ['skewchoice3']
    choices_groups = (Constants.skewchoices1, Constants.skewchoices2, Constants.skewchoices3)

    def vars_for_template(self):
        pie, squares = graph.render(
            title="Below you can see the choice you mae previously, and Gamble Set 3. Please Choose your most preferred gamble",
            **Constants.pie_conf)
        choices = self.get_choices(squares)
        selected = ["", self.player.skewchoice2] if self.player.skewchoice2 else [self.player.skewchoice1, ""]
        return {
            "screen_number": 3,
            "subtitle": "Individual makes another choice of which lottery A-F, with new values. Can choose new lottery or keep original choice",
            "graph": pie,
            "choices": choices,
            "selected": selected}

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):

    def vars_for_template(self):
        squares = graph.render_squares(Constants.pie_conf["colors"])
        snum, soption, choices = self.player.selected_skew()
        return {
            "snum": snum, "soption": soption,
            "landed": squares[self.player.winning_choice],
            "choices": list(zip(squares, choices))}


page_sequence = [
    Screen1, Screen2, Screen3,
    Results
]
