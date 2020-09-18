import mysql.connector
from tkinter import*
import webbrowser
from tkinter import messagebox 
conn = mysql.connector.connect(user='root', password='1203', host='127.0.0.1', database='code_forces_api_re' )
cursor = conn.cursor()
sql = 'select name,tags,id from code_forces_api_re.prob_set;'
cursor.execute(sql)
result = cursor.fetchall()
len_res = len(result)

# print(result)
name, tag = [], set()
for i in range(len_res):
    # name.append(result[i][0])
    if type(result[i][1]) == set(): 
        tag = tag | result[i][1]
    if type(result[i][1]) == type(set()):
        tag = tag | result[i][1]
    # names= set(name) 

def res():

    trans = word.get()
    conn = mysql.connector.connect(user='root', password='1203', host='127.0.0.1', database='code_forces_api_re' )
    cursor = conn.cursor()
    sql = 'select name,tags,id from code_forces_api_re.prob_set;'
    cursor.execute(sql)
    result = cursor.fetchall()
    len_res = len(result)


    name, tag = [], set()
    for i in range(len_res):
        # name.append(result[i][0])
        if type(result[i][1]) == set(): 
            tag = tag | result[i][1]
        if type(result[i][1]) == type(set()):
            tag = tag | result[i][1]
        # names= set(name) 
    test = []
    mylist.delete(0,len_res)
    if trans in tag:
        for i in range(len_res): 
            num = str(result[i][1]).find(trans)
            if num != -1:
                test.append(result[i][0])
        for i in range(len(test)):
            mylist.insert(END,test[i])
    else:
        mylist.insert(END,'검색결과가 없습니다.')

def con():
    link = words.get()
    for a in range(len_res):
        if result[a][0] == link:
            webbrowser.open('https://codeforces.com/problemset/problem/{0}'.format(result[a][2]))
            break
        elif a == len_res -1 :
            messagebox.showinfo('오류','찾는 검색어가 없습니다.')
            break

def tt():
    try:
        entry1.delete(0,1000)
        a = list2.curselection()
        tts = list2.get(a[0])
        entry1.insert(0,tts)
    except Exception as e:
        messagebox.showwarning('미입력','태그를 입력하지 않았습니다.')
        print(e)  
def bb():
    try:
        entry2.delete(0,1000)
        a = mylist.curselection()
        tts = mylist.get(a[0])
        entry2.insert(0,tts)
    except Exception as e:
        messagebox.showwarning('미입력','문제를 입력하지 않았습니다.')
        print(e)  
    
    

win = Tk()
win.title('codeforces_search')
win.geometry('400x300')

word = StringVar()
words = StringVar()


frame = Frame(win)
frame.pack(side = 'left')
frame2 = Frame(win)
frame2.pack(side= 'top',anchor = 'e')
frame3 = Frame(win)
frame3.pack(side = 'right')



# for line in range(100):
#     mylist.insert(END,'this is line'+str(line))
scrollbar = Scrollbar(frame3)
scrollbar.pack(side = RIGHT, fill = Y)
mylist = Listbox(frame3,yscrollcommand = scrollbar.set)

mylist.pack(side = RIGHT,expand = True)

scrollbar2 = Scrollbar(frame)
scrollbar2.pack(side = RIGHT,fill = Y)
list2 = Listbox(frame, yscrollcommand = scrollbar2.set)
a = 0
for i in tag:
    list2.insert(a,i)
    a+=1

list2.pack(side = 'top')

label1 = Label(frame2, text ='태그 검색')
label1.pack()



entry1 = Entry(frame2, textvariable = word)
entry1.pack()
button1 = Button(frame2,text = '입력',command = res)
button1.pack()

button3 = Button(frame, text ='태그 선택', command = tt)
button3.pack()


entry2 = Entry(frame2, textvariable = words)
entry2.pack()
button2 = Button(frame2,text = '사이트 연결',command = con)
button2.pack()

scrollbar.config(command = mylist.yview)
scrollbar2.config(command = list2.yview)


button4 = Button(frame3, text = '문제 선택', command = bb)
button4.pack(side = BOTTOM)

win.mainloop()

conn.close()
