<div class="cell code" data-execution_count="9">

``` python
from tkinter import *
```

</div>

<div class="cell code">

``` python
window = Tk()
window.title("Program loop")
window.mainloop()
```

</div>

<div class="cell markdown">

## Buttons

</div>

<div class="cell code" data-execution_count="15">

``` python
def changeColor():
    if btnCalculate["fg"] == "blue":
        btnCalculate["fg"] = "red"
    else:
        btnCalculate["fg"] = "blue"
```

</div>

<div class="cell code" data-execution_count="17">

``` python
window = Tk()
window.title("Button")
btnCalculate = Button(window, text="calculate", bg ="light blue",command=changeColor)
btnCalculate.grid(padx=75, pady=15)
window.mainloop()
```

</div>

<div class="cell code" data-execution_count="18">

``` python
window = Tk()
Principal = Label(window, text="Principal: ")
Principal.grid(padx = 100, pady=15)
window.mainloop()
```

</div>

<div class="cell markdown">

## Entry Widgets

</div>

<div class="cell code" data-execution_count="19">

``` python
window = Tk()
window.title("Entry widget")
entName = Entry(window, width=20)
entName.grid(padx=100,pady=15)
window.mainloop()
```

</div>

<div class="cell code">

``` python
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

</div>

<div class="cell code" data-execution_count="26">

``` python
window=Tk()
window.title("Read Only Entry Widget")
conOFentOutput = StringVar()
entOutput = Entry(window,width=20,state="readonly", textvariable=conOFentOutput)
entOutput.grid(padx=100,pady=15)
conOFentOutput.set("HELLO WORLD!")
window.mainloop()
```

</div>

<div class="cell markdown">

## List Box

</div>

<div class="cell code" data-execution_count="30">

``` python
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

</div>

<div class="cell markdown">

## Scroll Bars

</div>

<div class="cell code" data-execution_count="31">

``` python
window = Tk()
window.title("Scrollbar")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(padx=110,pady=15)
window.mainloop()
```

</div>
