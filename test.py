# input_string = '3. Critically evaluate the reliability of sources for an academic context.\n4. Filter, manage and organize information from a wide variety of sources for use in academic study.\n5. Demonstrate awareness of ethical issues related to academic integrity surrounding the access and use of information.'

# Split the input string by line breaks
# lines = input_string.split('\n')

# Initialize an empty list to store cleaned lines
# cleaned_lines = []

# Iterate through each line and only take characters after the first two characters
# for line in lines:
#     cleaned_line = line[2:]
#     cleaned_lines.append(cleaned_line.strip())

# print(cleaned_lines)
import sqlite3
from DrissionPage import ChromiumPage
#Connect to Database
conn = sqlite3.connect('AutoCoursera_DB.sqlite')
print(conn)
# Create a cursor object
cursor = conn.cursor()
#DATABASE HANDLE
# cursor.execute('DROP TABLE IF EXISTS academic_writing')
# cursor.execute('CREATE TABLE academic_writing (Quests TEXT,Answer TEXT,Mooc INTEGER)')
page = ChromiumPage()
mooc = 2
page.get('https://quizlet.com/vn/555164948/fptu-ssl101-mooc-2-flash-cards/')
allQuesContainer = page.ele('tag=section@class=SetPageTerms-termsList') #1
ContainerChilds = allQuesContainer.children("tag=div@class=SetPageTerms-term") #2
# print(ContainerChilds)
i = 0
for childs in ContainerChilds:
    i = i + 1
    print(i)
    parent_Of_QA_side = childs.child(1).child(1)
    # print(parent_Of_QA_side)
    QA_container = parent_Of_QA_side.child('tag=div')
    # print(QA_container)
    QA_container_2 = QA_container.child('tag=div')
    # print(QA_container_2)
    listQASide = QA_container_2.children('tag=div@data-testid=set-page-card-side') #3
    # print(listQASide)
    listQA = []
    for sides in listQASide:
        print("++++++++++++++++++++++++++++++++++++++++")
        QuestAns_text = sides.child(1).child(1).child(1).text
        print(QuestAns_text)
        listQA.append(QuestAns_text)
        #listQAside[0] la question || listQAside[1] la answers. 
    cursor.execute('INSERT INTO academic_writing (Quests,Answer,Mooc) VALUES (?,?,?)',(listQA[0],listQA[1],mooc))  
    conn.commit()
    print("NEXT--------------------------------------------------------")

