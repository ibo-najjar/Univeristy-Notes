<div class="cell code" data-execution_count="5">

``` python
from tkinter import *

def findLargest():
    L = [eval(conOFentNum1.get()),eval(conOFentNum3.get()),eval(conOFentNum3.get())]
    conOFentLargest.set(max(L))

window = Tk()
window.title("Largest Number")
Label(window, text="First number: ").grid(row=0,column=0,pady=5,sticky=E)
conOFentNum1 = StringVar()
ententNum1 = Entry(window,textvariable=conOFentNum1, width=8)
ententNum1.grid(row=0,column=1,sticky=W)
Label(window, text="Second number: ").grid(row=1,column=0,pady=5,sticky=E)
conOFentNum2 = StringVar()
ententNum2 = Entry(window,textvariable=conOFentNum2, width=8)
ententNum2.grid(row=1,column=1,sticky=W)
Label(window, text="Third number: ").grid(row=2,column=0,pady=5,sticky=E)
conOFentNum3 = StringVar()
ententNum3 = Entry(window,textvariable=conOFentNum3, width=8)
ententNum3.grid(row=2,column=1,sticky=W)
btnFind = Button(window, text="Find Largest", command=findLargest)
btnFind.grid(row=3,column=0,columnspan=2,padx=75)
Label(window, text="Largest number: ").grid(row=4,column=0,sticky=E)
conOFentLargest = StringVar()
entLargest = Entry(window, textvariable=conOFentLargest,state="readonly", width=8)
entLargest.grid(row=4,column=1,sticky=W)
window.mainloop()
```

</div>

<div class="cell code">

``` python
```

</div>
