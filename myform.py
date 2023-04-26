from asyncio.windows_events import NULL
import datetime
import re
from bottle import post, request
import pdb

@post('/home', method='post')
def my_form():
    questions = {}
    question = request.forms.get('QUEST')
    name = request.forms.get('USERNAME')
    mail = request.forms.get('ADRESS')
    nameStr = "%s" % name
    mailStr = "%s" % mail
    questionStr = "%s" % question
    questions["%s" % mail] = "%s" % question

    if len(questionStr) < 1:
        return '''
                <h3> Ask a Question </h3>
                <form action="/home" method="post">
                    <small> Enter your question </small>
                    <p><textarea style="resize:none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
                    <p><input type="text" size="50" name"USERNAME" placeholder="Your name"></p>
                    <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
                    <p><input type="submit" value="Send" class="btn btn-default"></p>
                </form>
               '''
    if len(nameStr) < 1:
        return '''
                <dialog id="no_message" open>    
                    Enter your name
                </dialog>
                <h3> Ask a Question </h3>
                <form action="/home" method="post">
                    <p><textarea style="resize:none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
                    <p><input type="text" size="50" name"USERNAME" placeholder="Your name"></p>
                    <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
                    <p><input type="submit" value="Send" class="btn btn-default"></p>
                </form>
               '''
    if len(mailStr) < 1:
        return '''
                <h3> Ask a Question </h3>
                <form action="/home" method="post">
                    <p><textarea style="resize:none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
                    <p><input type="text" size="50" name"USERNAME" placeholder="Your name"></p>
                    <small> Enter your e-mail </small>
                    <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
                    <p><input type="submit" value="Send" class="btn btn-default"></p>
                </form>
               '''
    regex = re.fullmatch(r'[a-z0-9]{2,25}@[a-z]{2,9}\.(com|ru)', mailStr)
    if len(nameStr) > 2:
        if regex:
            questions = {nameStr: questionStr}
            print(questions)
            pdb.set_trace()
            return "Thanks, " + nameStr + "! The answer will be sent to the mail " + mailStr + " (date: " + str(datetime.date.today()) + ")"
        return '''
                <h3> Ask a Question </h3>
                <form action="/home" method="post">
                    <p><textarea style="resize:none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
                    <p><input type="text" size="50" name"USERNAME" placeholder="Your name"></p>
                    <small> Incorrect e-mail </small>
                    <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
                    <p><input type="submit" value="Send" class="btn btn-default"></p>
                </form>
               '''
    return '''
            <dialog id="no_message" open>
                Short name
            </dialog>
            <h3> Ask a Question </h3>
            <form action="/home" method="post">
                <p><textarea style="resize:none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
                <p><input type="text" size="50" name"USERNAME" placeholder="Your name"></p>
                <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
                <p><input type="submit" value="Send" class="btn btn-default"></p>
            </form>
            '''

