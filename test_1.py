import sqlite3
from DrissionPage import ChromiumPage
conn = sqlite3.connect('AutoCoursera_DB.sqlite')
cursor = conn.cursor()
question_complete = "Which of the following are learning objectives for this MOOC?"
cursor.execute("SELECT Answer FROM academic_writing WHERE Quests LIKE ?", ('%'+question_complete+'%',))
answers = cursor.fetchall()
# print("THIS IS THE ANSWER")
# print(answers)
answers = list(answers[0])
answers_new = [line[3:] for line in answers[0].split('\n')]
print(answers_new)


#Tim kiem 1 string lieu co ton tai trong 1 phan tu trong list
my_list = ['apple', 'banana putaas', 'orange']
search_string = 'banana'


if any(search_string in s for s in my_list):
    print("Chuỗi '{}' tồn tại trong danh sách.".format(search_string))
else:
    print("Chuỗi '{}' không tồn tại trong danh sách.".format(search_string))