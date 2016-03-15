# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Example(Page):
    template_name = 'eyes_mind/Question.html'

    form_model = models.Player
    form_fields = ['response_example']

    def vars_for_template(self):
        return {
            "is_practice": True,
            "options": Constants.example["options"],
            "image": "/".join(["eyes_mind", Constants.example["fname"]])}

    def is_displayed(self):
        return self.subsession.round_number == 1


class ResultExample(Page):
    template_name = 'eyes_mind/Results.html'

    def vars_for_template(self):
        correct_answer = Constants.example["options"][Constants.example["answer"]]
        player_answer = self.player.response_example
        is_correct = (player_answer == correct_answer)
        return {
            "is_practice": True,
            "options": Constants.example["options"],
            "correct_answer": correct_answer,
            "answer_idx": Constants.example["answer"],
            "player_answer": player_answer,
            "is_correct": is_correct,
            "image": "/".join(["eyes_mind", Constants.example["fname"]])}

    def is_displayed(self):
        return self.subsession.round_number == 1


class Question(Page):
    template_name = 'eyes_mind/Question.html'

    form_model = models.Player

    def get_question_data(self):
        round_number = self.subsession.round_number
        question = Constants.questions[round_number-1]
        field_name = "response_q{}".format(round_number)
        response = getattr(self.player, field_name)
        return round_number, question, field_name, response

    def get_form_fields(self):
        return [self.get_question_data()[2]]

    def vars_for_template(self):
        round_number, question, field_name, response = self.get_question_data()
        return {
            "is_practice": False,
            "options": question["options"],
            "image": "/".join(["eyes_mind", question["fname"]])}

    def before_next_page(self):
        round_number, question, field_name, response = self.get_question_data()
        if question["options"][question["answer"]] == response:
            self.player.responses_correct += 1


class Result(Page):
    template_name = 'eyes_mind/Results.html'

    def get_question_data(self):
        round_number = self.subsession.round_number
        question = Constants.questions[round_number-1]
        field_name = "response_q{}".format(round_number)
        response = getattr(self.player, field_name)
        return round_number, question, field_name, response

    def vars_for_template(self):
        round_number, question, field_name, response = self.get_question_data()
        correct_answer = question["options"][question["answer"]]
        player_answer = response
        is_correct = (player_answer == correct_answer)
        return {
            "is_practice": False,
            "options": question["options"],
            "correct_answer": correct_answer,
            "answer_idx": question["answer"],
            "player_answer": player_answer,
            "is_correct": is_correct,
            "image": "/".join(["eyes_mind", question["fname"]])}


class Resume(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds




page_sequence = [
    Example, ResultExample,
    Question, Result, Resume
]
