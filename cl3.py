
from tkinter import*

def button_bos(num):
    global equation_text
    equation_text=equation_text+str(num)
    print(equation_label.set(equation_text))
  
    
def equals():
    
    global equation_text
    try:    
        
        total= str(eval(equation_text))
        print(equation_label.set(total))
        equation_text=total
    
    except SyntaxError:
        print(equation_label.set("Yozilishda xatolik"))
        equation_text=''

    
    
    except ZeroDivisionError:
        print(equation_label.set("Nolga Bulish mumin emas"))
        equation_text=''

def clear():
    
    global equation_text
    equation_label.set('')
    equation_text=''



room=Tk()
print(room.title("kankulyatar yasash"))
print(room.geometry('450x500+500+400'))

equation_text=''
equation_label=StringVar()

label=Label(room,textvariable=equation_label,font=('consolas',20),width=24,height=2)
print(label.pack())

frame=Frame(room)
print(frame.pack())


button1=Button(frame,text=1,height=4,width=9,font=35,command=lambda:button_bos(1))
print(button1.pack())
print(button1.grid(row=0,column=0))

button2=Button(frame,text=2,height=4,width=9,font=35,command=lambda:button_bos(2))
print(button2.grid(row=0,column=1))

button3=Button(frame,text=3,height=4,width=9,font=35,command=lambda:button_bos(3))
print(button3.grid(row=0,column=2))

button4=Button(frame,text=4,height=4,width=9,font=35,command=lambda:button_bos(4))
print(button4.grid(row=1,column=0))

button5=Button(frame,text=5,height=4,width=9,font=35,command=lambda:button_bos(5))
print(button5.grid(row=1,column=1))

button6=Button(frame,text=6,height=4,width=9,font=35,command=lambda:button_bos(6))
print(button6.grid(row=1,column=2))

button7=Button(frame,text=7,height=4,width=9,font=35,command=lambda:button_bos(7))
print(button7.grid(row=2,column=0))

button8=Button(frame,text=8,height=4,width=9,font=35,command=lambda:button_bos(8))
print(button8.grid(row=2,column=1))

button9=Button(frame,text=6,height=4,width=9,font=35,command=lambda:button_bos(6))
print(button9.grid(row=2,column=2))

button0=Button(frame,text=0,height=4,width=9,font=35,command=lambda:button_bos(0))
print(button0.grid(row=3,column=0))

pls=Button(frame,text='+',height=4,width=9,font=35,command=lambda:button_bos('+'))
print(pls.grid(row=0,column=3))

minus=Button(frame,text='-',height=4,width=9,font=35,command=lambda:button_bos('-'))
print(minus.grid(row=1,column=3))

mult=Button(frame,text='*',height=4,width=9,font=35,command=lambda:button_bos('*'))
print(mult.grid(row=2,column=3))

div=Button(frame,text='/',height=4,width=9,font=35,command=lambda:button_bos('/'))
print(div.grid(row=3,column=3))

equal=Button(frame,text='=',height=4,width=9,font=35,command=equals)
print(equal.grid(row=3,column=2))

point=Button(frame,text='.',height=4,width=9,font=35,command=lambda:button_bos('.'))
print(point.grid(row=3,column=1))

clear=Button(room,text='clear',height=4,width=11,font=35,command=clear)
print(clear.pack())


print(room.mainloop())
        

