import unittest
from language_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对单个答案会被妥善保存"""

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.stored_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.stored_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
