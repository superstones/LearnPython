import unittest
import sys

# sys.path.append("D:\LearnPython\week3\chapter11\test_def\language_survey.py")
from language_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对单个答案会被妥善保存"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin', ]

    def test_store_single_response(self):
        self.my_survey.stored_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.stored_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
