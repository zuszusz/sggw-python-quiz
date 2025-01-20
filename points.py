def checkAnswers(questions):
    points=0
    for question in questions:
        areAnswersOk=True
        if(len(question.correctAnswers)!=len(question.userAnswers)):
            areAnswersOk=False
        else:
            for i in range(0,len(question.correctAnswers)):
                corerctAnswer=question.correctAnswers[i].value
                if(not corerctAnswer in question.userAnswers):
                    areAnswersOk=False
                    break
        if(areAnswersOk):
            points+=1

    return points