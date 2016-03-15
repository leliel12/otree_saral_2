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
    name_in_url = 'eyes_mind'
    players_per_group = None

    example = {'answer': 1, 'options': [u'aloux', u'paniqu\xe9', u'arrogant', u'haineux'], 'fname': u'eyes-example.jpg'}

    questions = [
        {'answer': 0, 'options': [u'joueur', u'r\xe9confortant', u'irrit\xe9', u's\u2019ennuyant'], 'fname': u'eyes-001.jpg'},
        {'answer': 1, 'options': [u'terrifi\xe9', u'boulevers\xe9', u'arrogant', u'agac\xe9'], 'fname': u'eyes-002.jpg'},
        {'answer': 2, 'options': [u'blagueur', u'angoiss\xe9', u'd\xe9sir', u'convaincu'], 'fname': u'eyes-003.jpg'},
        {'answer': 1, 'options': [u'blagueur', u'insistant', u'amus\xe9', u'd\xe9tendu'], 'fname': u'eyes-004.jpg'},
        {'answer': 2, 'options': [u'irrit\xe9', u'sarcastique', u'inquiet', u'amical'], 'fname': u'eyes-005.jpg'},
        {'answer': 1, 'options': [u'effondr\xe9', u'r\xeaveur', u'impatient', u'alarm\xe9'], 'fname': u'eyes-006.jpg'},
        {'answer': 2, 'options': [u's\u2019excusant', u'amical', u'mal \xe0 l\u2019aise', u'd\xe9moralis\xe9'], 'fname': u'eyes-007.jpg'},
        {'answer': 0, 'options': [u'd\xe9courag\xe9', u'soulag\xe9', u'timide', u'excit\xe9'], 'fname': u'eyes-008.jpg'},
        {'answer': 3, 'options': [u'agac\xe9', u'hostile', u'horrifi\xe9', u'pr\xe9occup\xe9'], 'fname': u'eyes-009.jpg'},
        {'answer': 0, 'options': [u'prudent', u'insistant', u's\u2019ennuyant', u'effondr\xe9'], 'fname': u'eyes-010.jpg'},
        {'answer': 2, 'options': [u'terrifi\xe9', u'amus\xe9', u'plein de regrets', u'charmeur'], 'fname': u'eyes-011.jpg'},
        {'answer': 2, 'options': [u'indiff\xe9rent', u'embarrass\xe9', u'sceptique', u'd\xe9moralis\xe9'], 'fname': u'eyes-012.jpg'},
        {'answer': 1, 'options': [u'd\xe9termin\xe9', u'pr\xe9voyant', u'mena\xe7ant', u'timide'], 'fname': u'eyes-013.jpg'},
        {'answer': 3, 'options': [u'irrit\xe9', u'd\xe9\xe7u', u'd\xe9prim\xe9', u'accusateur'], 'fname': u'eyes-014.jpg'},
        {'answer': 0, 'options': [u'contemplatif', u'angoiss\xe9', u'encourageant', u'amus\xe9'], 'fname': u'eyes-015.jpg'},
        {'answer': 1, 'options': [u'irrit\xe9', u'songeur', u'encourageant', u'compatissant'], 'fname': u'eyes-016.jpg'},
        {'answer': 0, 'options': [u'dubitatif', u'affectueux', u'joueur', u'effondr\xe9'], 'fname': u'eyes-017.jpg'},
        {'answer': 0, 'options': [u'd\xe9termin\xe9', u'amus\xe9', u'effondr\xe9', u's\u2019ennuyant'], 'fname': u'eyes-018.jpg'},
        {'answer': 3, 'options': [u'arrogant', u'reconnaissant', u'sarcastique', u'h\xe9sitant'], 'fname': u'eyes-019.jpg'},
        {'answer': 1, 'options': [u'dominant', u'amical', u'coupable', u'horrifi\xe9'], 'fname': u'eyes-020.jpg'},
        {'answer': 1, 'options': [u'embarrass\xe9', u'r\xeaveur', u'confus', u'paniqu\xe9'], 'fname': u'eyes-021.jpg'},
        {'answer': 0, 'options': [u'pr\xe9occup\xe9', u'reconnaissant', u'insistant', u'suppliant'], 'fname': u'eyes-022.jpg'},
        {'answer': 2, 'options': [u'content', u's\u2019excusant', u'provoquant', u'curieux'], 'fname': u'eyes-023.jpg'},
        {'answer': 0, 'options': [u'pensif', u'irrit\xe9', u'excit\xe9', u'hostile'], 'fname': u'eyes-024.jpg'},
        {'answer': 3, 'options': [u'paniqu\xe9', u'incr\xe9dule', u'd\xe9courag\xe9', u'int\xe9ress\xe9'], 'fname': u'eyes-025.jpg'},
        {'answer': 2, 'options': [u'alarm\xe9', u'timide', u'hostile', u'anxieux'], 'fname': u'eyes-026.jpg'},
        {'answer': 1, 'options': [u'blagueur', u'prudent', u'arrogant', u'rassurant'], 'fname': u'eyes-027.jpg'},
        {'answer': 0, 'options': [u'int\xe9ress\xe9', u'blagueur', u'affectueux', u'content'], 'fname': u'eyes-028.jpg'},
        {'answer': 3, 'options': [u'impatient', u'effondr\xe9', u'irrit\xe9', u'r\xe9fl\xe9chi'], 'fname': u'eyes-029.jpg'},
        {'answer': 1, 'options': [u'reconnaissant', u'charmeur', u'hostile', u'd\xe9\xe7u'], 'fname': u'eyes-030.jpg'},
        {'answer': 1, 'options': [u'honteux', u'confiant', u'blagueur', u'd\xe9moralis\xe9'], 'fname': u'eyes-031.jpg'},
        {'answer': 0, 'options': [u's\xe9rieux', u'honteux', u'bouche-b\xe9e', u'alarm\xe9'], 'fname': u'eyes-032.jpg'},
        {'answer': 3, 'options': [u'embarrass\xe9', u'coupable', u'r\xeaveur', u'soucieux'], 'fname': u'eyes-033.jpg'},
        {'answer': 2, 'options': [u'effondr\xe9', u'd\xe9rout\xe9', u'm\xe9fiant', u'terrifi\xe9'], 'fname': u'eyes-034.jpg'},
        {'answer': 1, 'options': [u'perplexe', u'nerveux', u'insistant', u'contemplatif'], 'fname': u'eyes-035.jpg'},
        {'answer': 2, 'options': [u'honteux', u'nerveux', u'suspicieux', u'ind\xe9cis'], 'fname': u'eyes-036.jpg'}
    ]

    num_rounds = len(questions)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    response_example = models.CharField(max_length=255, choices=Constants.example["options"], widget=widgets.RadioSelectHorizontal())

    response_q1 = models.CharField(max_length=255, choices=Constants.questions[0]["options"], widget=widgets.RadioSelectHorizontal())
    response_q2 = models.CharField(max_length=255, choices=Constants.questions[1]["options"], widget=widgets.RadioSelectHorizontal())
    response_q3 = models.CharField(max_length=255, choices=Constants.questions[2]["options"], widget=widgets.RadioSelectHorizontal())
    response_q4 = models.CharField(max_length=255, choices=Constants.questions[3]["options"], widget=widgets.RadioSelectHorizontal())
    response_q5 = models.CharField(max_length=255, choices=Constants.questions[4]["options"], widget=widgets.RadioSelectHorizontal())
    response_q6 = models.CharField(max_length=255, choices=Constants.questions[5]["options"], widget=widgets.RadioSelectHorizontal())
    response_q7 = models.CharField(max_length=255, choices=Constants.questions[6]["options"], widget=widgets.RadioSelectHorizontal())
    response_q8 = models.CharField(max_length=255, choices=Constants.questions[7]["options"], widget=widgets.RadioSelectHorizontal())
    response_q9 = models.CharField(max_length=255, choices=Constants.questions[8]["options"], widget=widgets.RadioSelectHorizontal())
    response_q10 = models.CharField(max_length=255, choices=Constants.questions[9]["options"], widget=widgets.RadioSelectHorizontal())
    response_q11 = models.CharField(max_length=255, choices=Constants.questions[10]["options"], widget=widgets.RadioSelectHorizontal())
    response_q12 = models.CharField(max_length=255, choices=Constants.questions[11]["options"], widget=widgets.RadioSelectHorizontal())
    response_q13 = models.CharField(max_length=255, choices=Constants.questions[12]["options"], widget=widgets.RadioSelectHorizontal())
    response_q14 = models.CharField(max_length=255, choices=Constants.questions[13]["options"], widget=widgets.RadioSelectHorizontal())
    response_q15 = models.CharField(max_length=255, choices=Constants.questions[14]["options"], widget=widgets.RadioSelectHorizontal())
    response_q16 = models.CharField(max_length=255, choices=Constants.questions[15]["options"], widget=widgets.RadioSelectHorizontal())
    response_q17 = models.CharField(max_length=255, choices=Constants.questions[16]["options"], widget=widgets.RadioSelectHorizontal())
    response_q18 = models.CharField(max_length=255, choices=Constants.questions[17]["options"], widget=widgets.RadioSelectHorizontal())
    response_q19 = models.CharField(max_length=255, choices=Constants.questions[18]["options"], widget=widgets.RadioSelectHorizontal())
    response_q20 = models.CharField(max_length=255, choices=Constants.questions[19]["options"], widget=widgets.RadioSelectHorizontal())
    response_q21 = models.CharField(max_length=255, choices=Constants.questions[20]["options"], widget=widgets.RadioSelectHorizontal())
    response_q22 = models.CharField(max_length=255, choices=Constants.questions[21]["options"], widget=widgets.RadioSelectHorizontal())
    response_q23 = models.CharField(max_length=255, choices=Constants.questions[22]["options"], widget=widgets.RadioSelectHorizontal())
    response_q24 = models.CharField(max_length=255, choices=Constants.questions[23]["options"], widget=widgets.RadioSelectHorizontal())
    response_q25 = models.CharField(max_length=255, choices=Constants.questions[24]["options"], widget=widgets.RadioSelectHorizontal())
    response_q26 = models.CharField(max_length=255, choices=Constants.questions[25]["options"], widget=widgets.RadioSelectHorizontal())
    response_q27 = models.CharField(max_length=255, choices=Constants.questions[26]["options"], widget=widgets.RadioSelectHorizontal())
    response_q28 = models.CharField(max_length=255, choices=Constants.questions[27]["options"], widget=widgets.RadioSelectHorizontal())
    response_q29 = models.CharField(max_length=255, choices=Constants.questions[28]["options"], widget=widgets.RadioSelectHorizontal())
    response_q30 = models.CharField(max_length=255, choices=Constants.questions[29]["options"], widget=widgets.RadioSelectHorizontal())
    response_q31 = models.CharField(max_length=255, choices=Constants.questions[30]["options"], widget=widgets.RadioSelectHorizontal())
    response_q32 = models.CharField(max_length=255, choices=Constants.questions[31]["options"], widget=widgets.RadioSelectHorizontal())
    response_q33 = models.CharField(max_length=255, choices=Constants.questions[32]["options"], widget=widgets.RadioSelectHorizontal())
    response_q34 = models.CharField(max_length=255, choices=Constants.questions[33]["options"], widget=widgets.RadioSelectHorizontal())
    response_q35 = models.CharField(max_length=255, choices=Constants.questions[34]["options"], widget=widgets.RadioSelectHorizontal())
    response_q36 = models.CharField(max_length=255, choices=Constants.questions[35]["options"], widget=widgets.RadioSelectHorizontal())

    responses_correct = models.IntegerField(default=0)

