"""
Experiment - uncertain outcome process
Event :  outcomes of an Experiment
> Elementry events :
    events thar cannot be decomposed or broken down into
    other events, denoted by lower case letters
suppose the experiment is to roll a die, elementry events for the experiment
rolling 1, 2 and so on, chances of indiviual number
group of event is not a elementry event like even number event

> Sample space :
    complete listing of all elementry events for an experiment is a sample
    space
    eg., exp rolling a dice ; sample space = {1,2,3 4,5 6,}

> Mutually exclusive events :
    cannot have both at same time
    - eg., Coin, getting head or tails at the same time both cannot happen.
    Head and Tail are mutually exculsive events.
    - totally two different events are mutually exculsive there is no union
    in any event happening,
    - like person is either alive or dead cant be both.
    - Addition Rule
    - Multiplication Rule : p(a П b) = p(a).p(b)
    - when not independed event : p(a П b) = p(a) . p(b | a)

> Independent event :
    totally different event of same or different experiment.
    does not affect occurence of other event.
    'coin' and 'die'
    'event of experiment A' and 'event of experiment B'
    'heads' or '4 on die'

> Complementry Events :
    complementry to each other,
    eg., a student is either pass or fail.
    p(a) = passinf probability
    p(b) = 1 = p(a)




1, 2, 3, 4, 5, 6
rolling dice is experiment


<FORMULA>
p = no of fav of outcome / total outcomes possible.

probability is idea of mathematical concept, that re  fers to chance of likelihood of
a particular event taking place, probability is way of quantifying how likely is some
things to happen

Types of Probability
> Theorotical Probability:
    when all outcomes are equally likely.
    for instance, probability of drawing a red car from a standard deck
    total = 52
    red only = 26 (fav outcome wanted)

    p = 26/52 = 0.5

> Experimental Probability :
    if you flip a coin 100 times and it lands on head 55 times
    55 / 100 =  55%  0.55

> Subjective probability :
    based on personal judgement or experience, this is not calculated. rather estimated
    based on knowledge or thought or gut feeling.

> Conditional Probability :
    provided that x and y are independent events,
    in CP we try to connect the events by creating dependency on each other,
    P(x | y) = p(x) ( X Happenig provided y has already occured.
    P(y | x ) = p(y)

    <FORMULA>
    P(A | B) = P( A and B) / P(B)

    DEFINATION : Probability of event happening and probability of other event happened.
        how the likelihood of 1 event changes based on the knowledge of another event.
        eg., 100 people parting 50 wearing glasses and 25 wearing glasses with hat.

        a = people w/ hat
        b = people w/ glasses

        p(a) = 50/ 100
        p(b) = 25 /100

        p(a | b) = 0.25 /  0.4 = 0.625

"""
#
total = 15

red = 5/ total
blue = 7 / total
green = 3 / total

print(f"red probablity is {red} \ngreen : {green} \nblue : {blue}")

print("\nApproach Pandas")
import pandas as pd

data = {'Color': ['Red', 'Blue', 'Green'],'Count': [5, 7, 3]}
df = pd.DataFrame(data)

total_balls = df['Count'].sum()

df['Probability'] = round((df['Count'] / total_balls), 1)

print(df)





