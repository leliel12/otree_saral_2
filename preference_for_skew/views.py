# -*- coding: utf-8 -*-
from __future__ import division

from collections import OrderedDict

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from .libs import graph

class Intro(Page):
    pass

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
        pie, squares = graph.render(title="With 50 percent chance the pink payoff will be selected, "
                       "with 49 percent chance the green, and with 1 percent chance the purple.", **Constants.pie_conf)
        choices = self.get_choices(squares)
        return {
            "screen_number": 1,
            "subtitle":"Please choose a lottery from the choices (A-F) below. Your selection will play out with a random draw to select the color for payment.",
            "graph": pie,
            "choices": choices}


class Screen2(Page, AbstractScreen):

    template_name = "preference_for_skew/Question.html"

    form_model = models.Player
    form_fields = ['skewchoice2']
    choices_groups = (Constants.skewchoices1, Constants.skewchoices2)

    def vars_for_template(self):
        pie, squares = graph.render(
            title="With 50 percent chance the pink payoff will be selected, "
                       "with 49 percent chance the green, and with 1 percent chance the purple.",
            **Constants.pie_conf)
        choices = self.get_choices(squares)
        selected = [self.player.skewchoice1]
        return {
            "screen_number": 2,
            "subtitle": "Before we play out the lottery - you will see your previous choice highlighted below (first row) and a new set of lotteries (second row). You can keep your previous choice or select a new lottery to play. If you want to keep your previous choice, press the Next button. Otherwise, select a new lottery and press Next.",
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
            title="With 50 percent chance the pink payoff will be selected, "
                       "with 49 percent chance the green, and with 1 percent chance the purple.",
            **Constants.pie_conf)
        choices = self.get_choices(squares)
        selected = ["", self.player.skewchoice2] if self.player.skewchoice2 else [self.player.skewchoice1, ""]
        return {
            "screen_number": 3,
            "subtitle": "One final decision before we play out the lottery. Below you will see your previous choice highlighted and a new (final) lottery set. You can keep your previous choice or select a new lottery to play. If you want to keep your previous choice, press the Next button. Otherwise, select a new lottery and press Next.",
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
    Intro, Screen1, Screen2, Screen3, Results
]
