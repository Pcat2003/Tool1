#Funtion AutoQuiz
import sqlite3
from DrissionPage import ChromiumPage
#MANIPULATE ANSWER DB
def manipulate(answers):
    answers = list(answers[0])
    answers_new = answers[0].split('\n')
    return answers_new

#Search answer in answerDB
def check_string_in_list(my_list, search_string):
     return any(search_string in s for s in my_list)

def AutoQuiz(tab,Mooc):
    conn = sqlite3.connect('AutoCoursera_DB.sqlite')
    cursor = conn.cursor()
    #Quiz part doesn't open a new tab, stay on that tab object
    tab.wait.ele_displayed('tag=button@data-test=action-button')
    tab.ele('tag=button@data-test=action-button').click()
    tab.wait.ele_displayed('#rc-FormPartsQuestion')
    listQuestionForm = tab.eles('@class=rc-FormPartsQuestion')
    i = 0 
    for parts in listQuestionForm:
        # print("_____________________________________________________-")
        i = i + 1
        # print(i,"\n")
        listQuestionForm_children = parts.children()
        rc_FormPartsQuestion_row = listQuestionForm_children[0]  #1
        rc_FormPartsQuestion_row_pii_hide = listQuestionForm_children[1] #2
        rc_FormPartsQuestion_row_1 = rc_FormPartsQuestion_row.child("@class=rc-FormPartsQuestion__contentCell") #3
        question_container = rc_FormPartsQuestion_row_1.child(1).child(1).child(1).child(1).child(1).child(1)
        # print(question_container.text) #Question
        question_Uncomplete = str(question_container.text)
        question_complete = question_Uncomplete.strip()
        # print(question_complete)
        cursor.execute("SELECT Answer FROM academic_writing WHERE Quests LIKE ? AND Mooc=?", ('%'+question_complete+'%',Mooc,))
        answers = cursor.fetchall()
        answerDB = manipulate(answers)
        # print("\n") 
        rc_FormPartsQuestion_row_pii_hide_1 = rc_FormPartsQuestion_row_pii_hide.child('@class=rc-FormPartsQuestion__contentCell') #4
        # print(rc_FormPartsQuestion_row_pii_hide_1)
        #Check if there are input box or multiple choice question
        questionClass = rc_FormPartsQuestion_row_pii_hide_1.child()
        questionClassType = questionClass.attr("class")
        # print("this answer type : ",questionClassType)   ---------Check_____Question_____Type------------
        if(questionClassType == "rc-TextInputBox"):
            print("Input_box")
            #Code to handle the input box
            #rc_group_answer may not appear with text input type
        elif(questionClassType == "rc-FormPartsMcq"):
            rc_group_answer =  questionClass  #5
            # print("multiple")
            rc_list_div_tag = rc_group_answer.children('tag=div') #6
            for divTag in rc_list_div_tag: 
                divTag_2nd_child = divTag.child(1).child(1) #7 Tag : lable
                InputTag = divTag_2nd_child.child('tag=input')
                # if(InputTag.attr('type')=='radio'):
                tagSpanContainAnswer = InputTag.next('tag=span') #8.2
                answer = tagSpanContainAnswer.child(1).child(1).child(1).child(1).child(1).child(1).text
                # print(answer)
                if(check_string_in_list(answerDB,answer)):
                    InputTag.click()
        elif(questionClassType==None):
            # print("this is multiple answers")
            # lableTag = divTag.child(1).child(1)
            rc_group_answer = questionClass.children('tag=div')
            for divTag in rc_group_answer:
                lableTag = divTag.child(1).child(1)
                InputTag = lableTag.child('tag=input@type=checkbox')
                # print(inputElement)
                answerContainer = InputTag.next('tag=span')
                answer = answerContainer.child(1).child(1).child(1).child(1).child(1).child(1).text
                # print(answer)
                if(check_string_in_list(answerDB,answer)):
                    InputTag.click()


        

            
        
        
        
    
    
    
