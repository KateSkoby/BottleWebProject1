from asyncio.windows_events import NULL
import datetime
import re
from bottle import post, request

@post('/home', method='post')
def my_form():
    question = request.forms.get('QUEST')
    name = request.forms.get('USERNAME')
    mail = request.forms.get('ADRESS')
    nameStr = "%s" % name
    mailStr = "%s" % mail

    if len("%s" % question) < 1:
        return "Enter your question"
    if "%s" % name == None:
        return "Enter your name"
    if len("%s" % mail) < 1:
        return "Enter your e-mail"

    regex = re.fullmatch(r'[a-z0-9]{2,25}@[a-z]{2,9}\.(com|ru)',"%s" % mail)
    if len("%s" % name) > 2:
        if regex:
            return "Thanks, " + nameStr + "! The answer will be sent to the mail " + mailStr + " (date: " + str(datetime.date.today()) + ")"
        return "Incorrect e-mail"
    return "Short name"
