#import

from tkinter import *
#function
expression = "" #varibel kosong

def press(num): 
    global expression #ekspresi bisa dalam bentuk apapun
    
    expression = expression + str(num)
    
    equation.set(expression)#masukan ke data
    
def equalpress():#bekerja ketika kita pencet tombol equal
    
    try:#coba
        global expression
        total = str(eval(expression))#untuk memproses
        
        equation.set(total)#untuk memapilkan hasil proses
        
        expression=""
        
    except:#kecuali
        
        equation.set("error")
        expression = ""
        
def clear():
    global expression
    expression = ""
    equation.set("")
#-----

a = Tk()

#tampilan
a.geometry("300x300")
a.title("kalkulator")

equation = StringVar()#tipe data

expression_field = Entry(a,textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

#button---------------
b1 = Button(a,text='1',command= lambda: press(1))
b1.grid(column=0, row=2)
b2 = Button(a,text='2',command= lambda: press(2))
b2.grid(column=1, row=2)
b3 = Button(a,text='3',command= lambda: press(3))
b3.grid(column=2, row=2)
b4 = Button(a,text='4',command= lambda: press(4))
b4.grid(column=0, row=3)
b5 = Button(a,text='5',command= lambda: press(5))
b5.grid(column=1, row=3)
b6 = Button(a,text='6',command= lambda: press(6))
b6.grid(column=2, row=3)
b7 = Button(a,text='7',command= lambda: press(7))
b7.grid(column=0, row=4)
b8 = Button(a,text='8',command= lambda: press(8))
b8.grid(column=1, row=4)
b9 = Button(a,text='9',command= lambda: press(9))
b9.grid(column=2, row=4)
b0 = Button(a,text='0',command= lambda: press(0))
b0.grid(column=0, row=5)

plus= Button(a,text="+",command= lambda: press('+'))
plus.grid(column=1, row=5)
minus= Button(a,text="-",command= lambda: press('-'))
minus.grid(column=2, row=5)
kali= Button(a,text="*",command= lambda: press('*'))
kali.grid(column=0, row=6)
bagi= Button(a,text="/",command= lambda: press('/'))
bagi.grid(column=1, row=6)

equal = Button(a,text="=",command=equalpress)
equal.grid(column=2,row=6)
clear = Button(a,text="clear",command=clear)
clear.grid(column=3,row=6)

#finish---------------
a.mainloop()