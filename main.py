from random import shuffle

cards=[" A"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q"," K"]
suits=["\u2660","\u2665","\u2663","\u2666"]

def prRed(skk): return ("\x1b[38;2;255;0;0m\x1b[48;2;255;255;255m{}\033[00m" .format(skk))

def prBlk(skk): return ("\x1b[38;2;0;0;0m\x1b[48;2;255;255;255m{}\033[00m" .format(skk))

def card(hand):
    card =  hand//4
    suit =  hand%4
    color = hand%2
    if color:
        return prRed(" "+cards[card]+suits[suit]+" ")
    else:
        return prBlk(" "+cards[card]+suits[suit]+" ")

def printCards(hands):
    ret=""
    for x in hands:
        ret+=card(x)
    return ret

def handVal(hand):
    newHand=[]
    for x in hand:
        chk=x//4+1
        if chk>10: chk=10
        if chk==1: chk=11
        newHand.append(chk)
    val=sum(newHand)
    for x in newHand:
        if val>21:
            if x==11:
                val-=10
    return val

def hit(shoe,hand):hand.append(shoe.pop())

deck = [x for x in range(52)]
shuffle(deck)

dealer=[]
hit(deck,dealer)
hit(deck,dealer)

player=[]
hit(deck,player)
hit(deck,player)

while 1:
    print(printCards(player))
    print(handVal(player))
    put=input("hit/stay")
    if put=="hit":
        hit(deck,player)
    else:
        break
    if handVal(player)>21:
        print(printCards(player))
        print(handVal(player))
        print("YOU BUSTED")
        break

while 1:
    print(printCards(dealer))
    print(handVal(dealer))
    if handVal(dealer)>=17: 
        if handVal(dealer)>21:print("BUST")
        else: print("Stand")
        break
    dealer.append(deck.pop())

if (handVal(dealer)>21 and handVal(player)<=21) or handVal(dealer)<handVal(player):
    print("win")
elif (handVal(player)>21 and handVal(dealer)<=21) or handVal(player)<handVal(dealer):
    print("loss")
elif (handVal(dealer)>21 and handVal(player)>21) or handVal(dealer)==handVal(player):
    print("tie")