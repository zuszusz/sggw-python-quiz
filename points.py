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


def checkMark(points, maxPoints):
    if points >= maxPoints * 0.91:
        return "5"
    elif points >= maxPoints * 0.81:
        return "4.5"
    elif points >= maxPoints * 0.71:
        return "4"
    elif points >= maxPoints * 0.61:
        return "3.5"
    elif points >= maxPoints * 0.51:
        return "3"
    else:
        return "2"
