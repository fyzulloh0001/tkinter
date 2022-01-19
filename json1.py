
import requests
import json
import pandas  as pd
from tkinter import*

a=requests.get("http://www.floatrates.com/daily/usd.json")
df=a.json()
df1=df['uzs']
df2=df['cny']
df3=df['eur']
# 
#{'code': 'UZS', 'alphaCode': 'UZS', 'numericCode': '860', 
# 'name': 'Uzbekistan Sum', 'rate': 10857.409250512, 
# 'date': 'Wed, 19 Jan 2022 11:55:01 GMT', 'inverseRate': 9.2103003297296e-05}

"""
{'code': 'RUB', 'alphaCode': 'RUB', 'numericCode': '643',
 'name': 'Russian Rouble', 'rate': 76.615984494162, 
 'date': 'Wed, 19 Jan 2022 11:55:01 GMT', 'inverseRate': 0.0130521066407}
 """
def pul():
    
    son1=int(krtsh1.get())
    sum=son1*df1['rate']
    return label1.configure(text=str(sum))

def pul1():
    son2=int(krtsh2.get())
    sum2=son2*df2['rate']
    return label2.configure(text=str(sum2))

  
def pul2():
    son3=int(krtsh3.get())
    sum3=son3*df3['rate']
    return label3.configure(text=str(sum3))

 
    
    
root=Tk()
root.title("Uzbekiston USD narxi")
root.geometry('450x4500+500+500')

e_l=StringVar()
################################################
"""
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
my_dict={'NAME':['Infant','Child','Young','Old'],'Nos':[30,40,50,50]}
df = pd.DataFrame(data=my_dict)
lbl=['Infant','Child','Young','Old']
fig1=df.plot.pie(title="Population",y='Nos',
        figsize=(3,3)).get_figure();


plot1 = FigureCanvasTkAgg(fig1, root)
plot1.get_tk_widget().grid(row=10,column=2,padx=5,pady=5)
root.mainloop()
"""

################################################
label=Label(text=f'{df1["name"]}',fg='black',font=('Times New Roman',15),cursor='dot')
label.grid(row=0,column=0)

label=Label(text=f'{df1["date"]}',fg='black',font=('Times New Roman',15),cursor='dot')
label.grid(row=0,column=1)

button1=Button(text='summ Natija-->',font=('Times New Roman',15),)
button1.grid(row=2,column=0)

label1=Label(text='_______________',fg='blue',font=('Times New Roman',15))
label1.grid(row=2,column=1)

button=Button(text=f'1 USD, {df1["rate"]}',command=pul)
button.grid(row=1,column=0)

krtsh1=Entry()
krtsh1.grid(row=1,column=1)

################################################
label=Label(text=f'{df2["name"]}',fg='black',font=('Times New Roman',15),cursor='dot')
label.grid(row=3,column=0)

label=Label(text=f'{df2["date"]}',fg='black',font=('Times New Roman',15),cursor='dot')
label.grid(row=3,column=1)

button2=Button(text='summ Natija-->',font=('Times New Roman',15),)
button2.grid(row=5,column=0)

label2=Label(text='_______________',fg='blue',font=('Times New Roman',15))
label2.grid(row=5,column=1)

button3=Button(text=f"1 CNY, {df2['rate']}",command=pul1)
button3.grid(row=4,column=0)

krtsh2=Entry()
krtsh2.grid(row=4,column=1)

################################################
label=Label(text=f'{df3["name"]}',fg='black',font=('Times New Roman',15),cursor='dot')
label.grid(row=6,column=0)

label=Label(text=f'{df3["date"]}',fg='black',font=('Times New Roman',15),cursor='dot')
label.grid(row=6,column=1)


button4=Button(text='summ Natija-->',font=('Times New Roman',15),)
button4.grid(row=8,column=0)

label3=Label(text='_______________',fg='blue',font=('Times New Roman',15))
label3.grid(row=8,column=1)

button5=Button(text=f"1 EUR, {df3['rate']}",command=pul2)
button5.grid(row=7,column=0)

krtsh3=Entry()
krtsh3.grid(row=7,column=1)



root.mainloop()