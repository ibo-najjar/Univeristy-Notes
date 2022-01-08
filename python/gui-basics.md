---
jupyter:
  interpreter:
    hash: 034a2ff1ce7a220551fa18f5e7125a21115135e98a83fcfdf6ff670c353a13c9
  kernelspec:
    display_name: "Python 3.8.5 64-bit (\\'condaenv\\': conda)"
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.8.5
  nbformat: 4
  nbformat_minor: 2
  orig_nbformat: 4
---

::: {.cell .code execution_count="9"}
``` {.python}
from tkinter import *
```
:::

::: {.cell .code}
``` {.python}
window = Tk()
window.title("Program loop")
window.mainloop()
```
:::

::: {.cell .markdown}
## Buttons
:::

::: {.cell .code execution_count="15"}
``` {.python}
def changeColor():
    if btnCalculate["fg"] == "blue":
        btnCalculate["fg"] = "red"
    else:
        btnCalculate["fg"] = "blue"
```
:::

::: {.cell .code execution_count="17"}
``` {.python}
window = Tk()
window.title("Button")
btnCalculate = Button(window, text="calculate", bg ="light blue",command=changeColor)
btnCalculate.grid(padx=75, pady=15)
window.mainloop()
```
:::

::: {.cell .code execution_count="18"}
``` {.python}
window = Tk()
Principal = Label(window, text="Principal: ")
Principal.grid(padx = 100, pady=15)
window.mainloop()
```
:::

::: {.cell .markdown}
## Entry Widgets
:::

::: {.cell .code execution_count="19"}
``` {.python}
window = Tk()
window.title("Entry widget")
entName = Entry(window, width=20)
entName.grid(padx=100,pady=15)
window.mainloop()
```
:::

::: {.cell .code}
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
:::

::: {.cell .code execution_count="26"}
``` {.python}
window=Tk()
window.title("Read Only Entry Widget")
conOFentOutput = StringVar()
entOutput = Entry(window,width=20,state="readonly", textvariable=conOFentOutput)
entOutput.grid(padx=100,pady=15)
conOFentOutput.set("HELLO WORLD!")
window.mainloop()
```
:::

::: {.cell .markdown}
## List Box
:::

::: {.cell .code execution_count="30"}
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
:::

::: {.cell .markdown}
## Scroll Bars
:::

::: {.cell .code execution_count="31"}
``` {.python}
window = Tk()
window.title("Scrollbar")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(padx=110,pady=15)
window.mainloop()
```
:::
