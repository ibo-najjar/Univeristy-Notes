<div class="cell code" data-execution_count="2">

``` python
from tkinter import *
```

</div>

<div class="cell code" data-execution_count="4">

``` python
window = Tk()
entNumOfYears = Entry(window,width=2)
entNumOfYears.grid(row=2, column=1,padx=5,pady=5,sticky=W) # stciky = W moves to left

btnCalculate = Button(window, text="Claculate Monthly Payment")
btnCalculate.grid(row=3,column=0,columnspan=2,pady=5)
window.mainloop()
```

</div>

<div class="cell markdown">

    padx=r r pixels to left and right
    pady=r r pixels to up and bottom
    padx=(r,s) r pixel to the right and s to the left
    pady=(r,s) r pixel to the top and s to the bottom

</div>

<div class="cell markdown">

    Sticky = N | S | W | E
    NORTH(top), SOUTH(bottom), WEST(left), EAST(right)
    Stciky = NS stretch from north to south
    sticky = NSEW fill block

</div>

<div class="cell code" data-execution_count="11">

``` python
window = Tk()
window.title("attach scrollbar to list")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0, column=2, rowspan=4, padx=(0,100), pady=5)
nums = range(0,20)
conOFlst = IntVar()
lstNums = Listbox(window, width=5, height=4, listvariable=conOFlst, yscrollcommand=yscroll.set)
lstNums.grid(row=0,column=1,rowspan=4,padx=(100,0),pady=5,sticky=SW)
conOFlst.set(tuple(nums))
yscroll["command"] = lstNums.yview
window.mainloop()
```

</div>
