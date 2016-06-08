# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

from time_preferences.models import Constants as tp_constants

from risk_aversion.libs import graph as ra_graph

from preference_for_skew.libs import graph as pfs_graph
from preference_for_skew.models import Constants as pfs_constants


class Results_task1(Page):

    def vars_for_template(self):
        tp_player = self.player.participant.time_preferences_player.first()
        option, option_desc, decision = tp_player.get_decision()
        return {"option": option, "option_desc": option_desc,
                "decision": decision, "tp_player": tp_player,
                "tp_constants": tp_constants}


class Results_task2(Page):

    def vars_for_template(self):
        ra_player = self.player.participant.risk_aversion_player.first()
        sp, choice, loteries, wrange, initial_payoff = ra_player.get_selected_puzzle()
        return {
            "selected_puzzle": sp, "choice": choice,
            "graphs": {k: ra_graph.render_unknow("?", *map(c, v)) for k, v in loteries.items()},
            "lotery": loteries[choice], "ra_player": ra_player,
            "wrange": wrange, "initial_payoff": initial_payoff}


class Results_task3(Page):

    def vars_for_template(self):
        pfs_player = self.player.participant.preference_for_skew_player.first()
        squares = pfs_graph.render_squares(pfs_constants.pie_conf["colors"])
        snum, soption, choices = pfs_player.selected_skew()
        return {
            "snum": snum, "soption": soption, "pfs_player": pfs_player,
            "landed": squares[pfs_player.winning_choice],
            "choices": list(zip(squares, choices))}


class final_payoff(Page):

    def vars_for_template(self):
        tp_player = self.player.participant.time_preferences_player.first()
        ra_player = self.player.participant.risk_aversion_player.first()
        pfs_player = self.player.participant.preference_for_skew_player.first()
        la_player = self.player.participant.lie_aversion_player.first()
        final_payoff = (
            (tp_player.payoff/5) + ra_player.payoff +
            pfs_player.payoff + la_player.payoff)
        return {"final_payoff": final_payoff}



page_sequence = [Results_task1, Results_task2, Results_task3, final_payoff]
