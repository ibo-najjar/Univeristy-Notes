<div class="cell markdown">

# Random Values

</div>

<div class="cell markdown">

  - `random.choice(L)` random value from list L
  - `random.sample(L, n)` n random values from L
  - `random.shuffle(L)` random order to elemetns of L
  - `random.randint(m, n)` random int x where m \<= x \<= n

</div>

<div class="cell code" data-execution_count="10">

``` python
import random

L = ["earth", "air", "fire", "water"]
print(L)
print(random.choice(L))
print(random.sample(L,2))
print("elements after shuffle: ",end="")
random.shuffle(L)
print(L)
```

<div class="output stream stdout">

    ['earth', 'air', 'fire', 'water']
    water
    ['air', 'earth']
    elements after shuffle: ['water', 'earth', 'air', 'fire']

</div>

</div>



<div class="cell code" data-execution_count="19">

``` python
# american roulette wheels
def main():
    bankroll = int(input("enter the amount of the bankroll: "))
    (amount, timesPlayed) = playDoubleOrNothing(bankroll)
    print(f"ending bankroll: {amount} dollars")
    print(f"numbers of games played: {timesPlayed}")
def isOdd(n):
    d = True if (0 <= n <= 37) and (n%2) == 0 else False
    return d
def profit(n):
    d = 1 if isOdd(n) else -1
    return d
def playDoubleOrNothing(bankroll):
    amount = bankroll
    timesPlayed = 0
    while 0 < amount < 2 * bankroll: #stop when going broke or doubling
        # let 37 represent 00
        n = random.randint(0,37)
        timesPlayed += 1
        amount += profit(n)
    return(amount, timesPlayed)
main()
```

<div class="output stream stdout">

    ending bankroll: 4 dollars
    numbers of games played: 4

</div>

</div>

<div class="cell code" data-execution_count="34">

``` python
# fruit slot machine
def main():
    for i in range(3):
        outcome = spinWheel()
        if i == 2:
            print(outcome, end="")
        else:
            print(outcome, end="-")
def spinWheel():
    n = random.randint(1,20)
    if n > 15:
        return "cherries"
    elif n > 10:
        return "orange"
    elif n > 5:
        return "plum"
    elif n > 2:
        return "Melon"
    elif n > 1:
        return "Bell"
    else:
        return "Bar"
main()
```

<div class="output stream stdout">

    cherries-Bell-cherries

</div>

</div>
