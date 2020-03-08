# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from .models import Question, UserQuiz, Answer, User
import csv

from django.shortcuts import render

# Create your views here.

# Get Quiz form to get the quiz details to be shown for the user.
def getQuizForm(request):
    try:
        questions_list = Question(user = request.user, quiz = request.quiz)
        if questions_list != null:
            output = ', '.join([q.question_text for q in latest_question_list])
        else:
            output = 'No questions found'
    except:
        logging.error('Error occured while retriving the questions for user.')
    return HttpResponse(output)
    
# Save quiz answers and redirect to success page
def submitQuiz(request):
    # Process the recieved inputs and validate it.
    #if validation success calculate the score and save the results.
    # Get correct answer for given question.
    try:
        answer = Answer.objects.get(question=request.question)
        if(answer.isCorrect)
            score = 100
        else:
            score = 0
        quizScore = UserQuiz(user = request.user, score = score, quiz = request.quiz)
        quizScore.save
    except:
        logging.error('Error occured while retriving the answers and saving for user.')
        return(HttpResponse(status = 400)
    
    
# API to get all the test results from UserQuiz table to display the score of each induvidual users.
def getQuizResults(request):
    try:
        queryset = UserQuiz.objects.all()
        if queryset != null:
            return HttpResponse(queryset)
        else:
            return(HttpResponse(status = 404)
    except:
        logging.error('Error occured while retriving the Quiz results for user.')
        return(HttpResponse(status = 400)
        
        
# API to get all the test results from UserQuiz table to display the score of each induvidual users.
def exportUserScoreAsCSV(request):
    try:
        # Export to csv
        queryset = UserQuiz.objects.all()
        if queryset == None:
            return(HttpResponse(status = 404)
        response = HttpResponse(content_type='text/csv')  
        response['Content-Disposition'] = 'attachment; filename="file.csv"'
        writer = csv.write(response)
        
    except:
        logging.error('Error occured while Exporting results')
        return(HttpResponse(status = 400)
        
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
        

    
