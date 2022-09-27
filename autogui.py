
import tkinter


win = tkinter.Tk()

import time
import pyautogui
import os, sys, subprocess
import glob
import natsort
import shutil
from tkinter import N, filedialog


def button2():
    time.sleep(2)
    pp = pyautogui.position()
    ent5.delete(0 , 'end')
    ent5.insert(0 , pp)


def button():

    if getattr(sys, 'frozen', False):
   
        program_directory = os.path.dirname(os.path.abspath(sys.executable))
    else:
        program_directory = os.path.dirname(os.path.abspath(__file__))

    os.chdir(program_directory)
    
    f = open("patch.txt", 'w')

    def open_file(filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
    data = txt3.get(1.0 , 'end')
    a = []
    a.append(data)
    model = data.split()
    mouse = ent5.get()
    mouse = mouse.split()

    for i in range (1 , int(ent4.get()) + 1):
        if 10 > i:
            result = ent.get() + ent2.get() + '00'+str(i)+ent3.get()+'-'+str(model[i])
            if model[i] == '--':
                result = ent.get() + ent2.get() + '00'+str(i)+ent3.get()

        if 10 <= i:
            result = ent.get() + ent2.get() + '0'+str(i)+ent3.get()+'-'+str(model[i])
            if model[i] == '--':
                result = ent.get() + ent2.get() + '0'+str(i)+ent3.get()

  
        f.write(result+'-'+'악기이름'+'.patch'+'\n')

        open_file('/Applications/Logic Pro X.app')
        time.sleep(0.3)
        pyautogui.press('right') 
        pyautogui.keyDown('shift' , 0.5)
        pyautogui.press('right')
        pyautogui.keyUp('shift' , 0.5)
        pyautogui.keyDown('command')
        pyautogui.keyDown('option')
        pyautogui.keyDown('e')
        pyautogui.keyUp('command')
        pyautogui.keyUp('option')
        pyautogui.keyUp('e')
        time.sleep(0.1)
        pyautogui.moveTo(int(mouse[0]),int(mouse[1]))
        pyautogui.doubleClick()
        time.sleep(0.3)
        pyautogui.keyDown('command')
        pyautogui.press('a')
        pyautogui.keyUp('command')
        pyautogui.press('delete')
        pyautogui.write(str(i))
        pyautogui.press('enter')
    
    for png in glob.glob('*shift.png'):
        os.remove(png)



    f.close()

def button3():
    dir = filedialog.askdirectory()
    ent6.delete(0 , 'end')
    ent6.insert(0 , dir)

def test ():

    data = txt3.get(1.0 , 'end')
    a = []
    a.append(data)
    model = data.split()
    result2 = []
    for i in range (1 , int(ent4.get()) + 1):
        if 10 > i:
            result = ent.get() + ent2.get() + '00'+str(i)+ent3.get()+'-'+str(model[i])
            if model[i] == '--':
                result = ent.get() + ent2.get() + '00'+str(i)+ent3.get()

        if 10 <= i:
            result = ent.get() + ent2.get() + '0'+str(i)+ent3.get()+'-'+str(model[i])
            if model[i] == '--':
                result = ent.get() + ent2.get() + '0'+str(i)+ent3.get()
        result2.append(result)


    loc = ent6.get()
    path_file = str(loc)
    fileEx = r'.mid'
    file = os.listdir(path_file)
    file = [s for s in file if s.endswith(fileEx)]
    file_sort = natsort.natsorted(file)

    n = 0
    for s in file_sort:
        old_name = os.path.join(path_file , s)
        name = result2[n] + '.mid'
        new_name = os.path.join(path_file , name)
        os.rename(old_name , new_name)
        n += 1

ent = tkinter.Entry(win)
ent.insert(0, "작곡가 번호")
ent.pack()


ent2 = tkinter.Entry(win)
ent2.insert(0, "프로젝트 번호")
ent2.pack()

ent3 = tkinter.Entry(win)
ent3.insert(0, "가이드번호")
ent3.pack()

ent4 = tkinter.Entry(win)
ent4.insert(0, "샘플갯수")
ent4.pack()

ent5 = tkinter.Entry(win)
ent5.insert(0, "마우스포지션")
ent5.pack()


ent6 = tkinter.Entry()
ent6.insert(0, '파일경로')
ent6.pack()


txt3 = tkinter.Text(win)
txt3.config(width=30, height=30)
txt3.insert(tkinter.INSERT , '--------빈칸---------')
txt3.pack()



btn = tkinter.Button(win
                    ,text = 'run')
btn.config(height = 5 , width =5)
btn.config(command = button)
btn.pack()

btn2 = tkinter.Button(win
                    ,text = 'position')
btn2.config(height = 2 , width =5)
btn2.config(command = button2)
btn2.pack()

btn3 = tkinter.Button(win,
            text='파일경로')
btn3.config(height = 2 , width =5)
btn3.config(command=button3)
btn3.pack()

btn4 = tkinter.Button(win,text='파일이름바꾸기')
btn4.config(height = 2 , width =5)
btn4.config(command=test)
btn4.pack()

win.mainloop()