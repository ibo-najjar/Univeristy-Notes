
``` {.python}
from tkinter import *
```

``` {.python}
window = Tk()
window.title("Program loop")
window.mainloop()
```

## Buttons

``` {.python}
def changeColor():
    if btnCalculate["fg"] == "blue":
        btnCalculate["fg"] = "red"
    else:
        btnCalculate["fg"] = "blue"
```

``` {.python}
window = Tk()
window.title("Button")
btnCalculate = Button(window, text="calculate", bg ="light blue",command=changeColor)
btnCalculate.grid(padx=75, pady=15)
window.mainloop()
```

``` {.python}
window = Tk()
Principal = Label(window, text="Principal: ")
Principal.grid(padx = 100, pady=15)
window.mainloop()
```


``` {.python}
window = Tk()
window.title("Entry widget")
entName = Entry(window, width=20)
entName.grid(padx=100,pady=15)
window.mainloop()
```

``` {.python}
def convertToUpperCase():
    conOfentName.set(conOfentName.get().upper)

window = Tk()
conOfentName = StringVar()
entName= Entry(window,textvariable=conOfentName)
entName.grid(padx=100,pady=15)
entName.bind("<Button-3>", convertToUpperCase)
print(conOfentName)
window.mainloop()
```

``` {.python}
window=Tk()
window.title("Read Only Entry Widget")
conOFentOutput = StringVar()
entOutput = Entry(window,width=20,state="readonly", textvariable=conOFentOutput)
entOutput.grid(padx=100,pady=15)
conOFentOutput.set("HELLO WORLD!")
window.mainloop()
```

## List Box

``` {.python}
def changeBg(event):
    lstColors["bg"] = lstColors.get(lstColors.curselection())

window = Tk()
window.title("Listbox")
L = ["red","yellow", "light blue", "orange"]
conOFlstColors = StringVar()
lstColors = Listbox(window, width=10,height=5, listvariable=conOFlstColors)
lstColors.grid(padx=100,pady=15)
conOFlstColors.set(tuple(L))
lstColors.bind("<<ListboxSelect>>", changeBg)
window.mainloop()
```

## Scroll Bars

``` {.python}
window = Tk()
window.title("Scrollbar")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(padx=110,pady=15)
window.mainloop()
```
