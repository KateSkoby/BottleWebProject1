from os.path import exists
from asyncio.windows_events import NULL
import datetime
import re
from bottle import post, request
import pdb
import json

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
            questions = {}
            #print(questions)
            #pdb.set_trace()
            #{"katesko@yandex.ru": ["Kate", "hello"]}
            if exists('data.txt'):
                with open('data.txt', 'r') as read_json:
                    questions = json.load(read_json)
                with open('data.txt', 'w') as write_json:
                    if mail in questions:
                        if name not in questions[mail]:
                            questions[mail][0] = name;
                            if question in questions[mail]:
                                i = 0
                            else:
                                questions[mail].append(question) 
                        elif question in questions[mail]:
                            i = 0
                        else:
                            questions[mail].append(question) 
                    else:
                        questions[mail] = [name, question]
                    json.dump(questions, write_json)
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

def isCorrectEmail(email: str):
    regex = re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
    if regex:
        return True
    else:
        return False

