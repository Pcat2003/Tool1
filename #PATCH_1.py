#Complete project PATCH1
from DrissionPage import ChromiumPage
from DrissionPage.common import Settings 
from DrissionPage import ChromiumOptions
from AutoQuiz_1 import AutoQuiz
import AutoQuiz_1
import sqlite3
import math
def videoSkip(pages):
    pages.ele('tag:em',timeout=1).click()
    pages.wait(0.5)
    clickConer = pages.ele('.hitbox').rect.size
    X_axis = float(math.trunc(clickConer[0])-0.05)
    Y_axis = float(math.trunc(clickConer[1])-0.05)
    # print(X_axis,"||",Y_axis)
    pages.ele('@class=hitbox').click.at(X_axis,Y_axis)
    # pages.wait.ele_loaded('tag:span@class=current-time-display')
    pages.wait(1)
    


Settings.singleton_tab_obj = False
page = ChromiumPage()
mooc = input("Enter the mooc number: ")
page.get(input("Enter the url of the first week to start: "))
page.set.window.max()
weekCollection = page.ele('tag=li@data-test=rc-WeekCollectionNavigationItem').child(1).child(1).child(1).child(1).next().child(1).child(1).child(1).child(1).child(1).children('tag=li')
print(weekCollection)
for week in range(0,len(weekCollection)):
    getLinkAtag = weekCollection[week].child()
    # print(getLinkAtag.link)
    page.new_tab(getLinkAtag.link)
    tab_Week = page.get_tab(page.latest_tab)
    page.wait.new_tab()
    eleLesson1 = tab_Week.ele('tag=ul@data-testid=named-item-list-list')
    firstLinkTag = eleLesson1.child(1).child(1).child(1)
    link = firstLinkTag.link
    page.new_tab(link)
    tabFirstWeekLesson = page.get_tab(page.latest_tab)
    page.wait.new_tab()
    #Get all lessontitle to open
    lesson_title = tabFirstWeekLesson.eles('tag:button@class=nostyle link-button')
    #Open each lesson part to expand
    #@class=nostyle link-button <===> all lesson part 
    for i in range(1,len(tabFirstWeekLesson.eles('tag:button@class=nostyle link-button'))):
        lesson_title[i].click()
    #tag:ul@class=rc-LessonItems nostyle <====> Lesson title
    lessonItemPerTitle = tabFirstWeekLesson.eles("tag:ul@class=rc-LessonItems nostyle")
    #Get into each lesson part and run into each item
    
    for parts in lessonItemPerTitle:
        a = parts.children()
        listLink  = []
        for li in a:
            a = li.child('tag:a')
            if(a != None):
                listLink.append(a.link)
        for i in range(0,len(listLink),1):
            page.new_tab(listLink[i])
            page.wait.new_tab()
            tabopened_1 = page.get_tab(page.latest_tab)
            print(tabopened_1.title)
            tabopened_1.wait.ele_deleted('text=Loading...',timeout=5)
            
            if(tabopened_1('@id=main').ele('tag=h3@aria-label=Reading completed',timeout=1)):
                # tabopened_1.ele('tag:button@data-testid=next-item').click()
                page.close_tabs(tabopened_1)
            elif(tabopened_1('@id=main').ele('tag=div@data-testid=reading-complete-container',timeout=2)):
                tabopened_1.ele('tag:button@data-testid=mark-complete',timeout=1.3).click()
                page.close_tabs(tabopened_1)
            elif(tabopened_1('@id=main-container').ele('@id=video-item-outermost-container',timeout=4)):
                videoSkip(tabopened_1)
                page.close_tabs(tabopened_1)
            elif(tabopened_1('@id=main-container').ele('tag=button@@type=button@@aria-labelledby=Start assignment')):
                AutoQuiz(tabopened_1,mooc)
            else:
                print("This item may not done "+listLink[i])
                page.close_tabs(tabopened_1)
    page.close_tabs(tab_Week)
        