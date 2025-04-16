import pytest
from app.trivia import Question, Quiz

def test_question_is_correct():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4") is True 
    assert question.is_correct("1") is False

def test_quiz_scoring():
    quiz = Quiz()
    question =  Question("What is 2 + 2?", ["1", "2", "3", "4"])
    quiz.add_question(question)

    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1

    question = quiz.get_next_question()
    assert question.description == "What is 2 + 2?"