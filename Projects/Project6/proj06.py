################################################
#Project 6
#Simplified Texas Hold'em Pker
#cards class module was used
#community cards with 5
#2 players: each plaer get two cards
#repeats if continues to play
#if not, halt
################################################
import cards #impor cards class to be used

def less_than(c1,c2):
    '''Return True if c1 is smaller in rank, 
       True if ranks are equal and c1 has a 'smaller' suit
       False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    suits = [[],[],[],[],[]]# empty lists inside the list to add on
    H = cannonical(H)#needs to be added for ordering
    for c in H:  
        suits[c.suit()-1].append(c) #suit# from 1-4, counting from 0 so -1
        if len(suits[0]) >=5:# only counting first five
            return suits[0][:5]
        if len(suits[1]) >=5:
            return suits[1][:5]
        if len(suits[2]) >=5:
            return suits[2][:5]
        if len(suits[3]) >=5:
            return suits[3][:5]
    return False # returns false if all ifs don't apply
        
    

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    srt_list = []# create a list to be appended
    l = cannonical(H)# ordering
    l = dict_rank_suit(l)# put it in a function to get dictionary output
    for k in l:
        srt_list.append(k)# get rank only in lists
    
    if len(srt_list) == 7:# if all distinct ranks
        if srt_list[4]-srt_list[0] == 4:# first 5
            return l[srt_list[0]]+l[srt_list[1]]+l[srt_list[2]]+l[srt_list[3]]\
        +l[srt_list[4]]
        elif srt_list[5]-srt_list[1] == 4:#5 from second
                return l[srt_list[1]]+l[srt_list[2]]+l[srt_list[3]]+\
            l[srt_list[4]]+l[srt_list[5]]
        elif srt_list[6]-srt_list[2] == 4:# 5 from third
                return l[srt_list[2]]+l[srt_list[3]]+l[srt_list[4]]+\
            l[srt_list[5]]+l[srt_list[6]]
    if len(srt_list) ==6:# if only 6 distinct ranks
        if srt_list[4]-srt_list[0] ==4:# first 5
            return l[srt_list[0]]+l[srt_list[1]]+l[srt_list[2]]+\
        l[srt_list[3]]+l[srt_list[4]]
        elif srt_list[5]-srt_list[1] == 4:# 5 from second
            return l[srt_list[1]]+l[srt_list[2]]+l[srt_list[3]]+\
        l[srt_list[4]]+l[srt_list[5]]
    if len(srt_list) ==5:# only 5 distinct ranks
        if srt_list[4]-srt_list[0] ==4:# first five
            return l[srt_list[0]]+l[srt_list[1]]+l[srt_list[2]]+\
        l[srt_list[3]]+l[srt_list[4]]
        
    
    return False # all ifs don't apply, return False
        
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    a = straight_7(H)# run straight function
    if a:
        b = flush_7(a)# run flush function afer it
        return b# returns straiht flush!
    return False # if not, return False
    
def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    H = cannonical(H)# ordering
    l = dict_rank_suit(H)# making a dictionary
    for keys in l:
        
        if len(l[keys]) ==4: # if they have 4 same ranks
            return l[keys]#rerturn those elements
    
    return False# if not return False
       
    

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
       
    if four_7(H) !=False: #like doc string describes
        return False
    H = cannonical(H)
    h= dict_rank_suit(H)
    
    for keys in h: 
        if len(h[keys]) ==3:# if there are 3 same ranks
            return h[keys] # print it out
    return False# if not, return False
        
        
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    
    if four_7(H) != False:# like docstring describes
        return False
    if three_7(H) != False:
        return False
    t = dict_rank_suit(H)
    two_pair = []
    H = cannonical(H)
    for keys in t:
        if len(t[keys]) ==2:# two same ranks!
            two_pair = two_pair+t[keys]
    if len(two_pair) ==4:# 2 sets of same ranks, stil two pair
        return two_pair  
    if len(two_pair) ==6:# 3 sets of same ranks,still two pair
        return two_pair[:4]
    else: 
        return False
       
    

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    if four_7(H) != False:# like doc string descirbes
        return False
    if three_7(H) != False:
        return False
    if two_pair_7(H) != False:
        return False
    H = cannonical(H)
    o = dict_rank_suit(H)
    
    for keys in o:
        if len(o[keys]) == 2:# with one matching pair
            return o[keys]
    return False# if not print False
    
       
   

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.  '''
    if four_7(H) != False:# like doctstring descirbes
        return False
    H = cannonical(H)
    f = dict_rank_suit(H)
    full =[]
    for keys in f:            
        if len(f[keys]) ==2 or len(f[keys]) ==3:# account 2 or 3 same ranks 
            full = full+f[keys]# if so, append that in empty list
    if len(full) == 5: #after having that, if they have exact 3,2 same ranks
            return full#return that full house pair
    if len(full) ==7:# if they have 3,2,2 same ranks,
            return full[:5]# print only first one pair and 3
    else:
        return False #if not reurn false
      


def dict_rank_suit(lists):
    '''
    inputting the givien 7 elements of a list, and returns a dictionary,
    rank being the key and each element with rank and value be value
    '''
   
    dict_rank = {}# empty dictioonary creation
    for ranks in lists:# go through each element
        if ranks.rank() == 1:# if rank is 1
            dict_rank.setdefault(1, []).append(ranks)#append that in new dict
        elif ranks.rank() == 2: # if rank is 2
            dict_rank.setdefault(2, []).append(ranks)#append that in new dict
        elif ranks.rank() == 3:# if rank is 3
            dict_rank.setdefault(3, []).append(ranks)#append that in new dict
        elif ranks.rank() == 4:# if rank is 4
            dict_rank.setdefault(4, []).append(ranks)#append that in new dict
        elif ranks.rank() == 5:# if rank is 5
            dict_rank.setdefault(5, []).append(ranks)#append that in new dict
        elif ranks.rank() == 6:# if rank is 5
            dict_rank.setdefault(6, []).append(ranks)#append that in new dict
        elif ranks.rank() == 7:# if rank is 6
            dict_rank.setdefault(7, []).append(ranks)#append that in new dict
        elif ranks.rank() == 8:# if rank is 7
            dict_rank.setdefault(8, []).append(ranks)#append that in new dict
        elif ranks.rank() == 9:# if rank is 8
            dict_rank.setdefault(9, []).append(ranks)#append that in new dict
        elif ranks.rank() == 10:# if rank is 9
            dict_rank.setdefault(10, []).append(ranks)#append that in new dict
        elif ranks.rank() == 11:# if rank is 11
            dict_rank.setdefault(11, []).append(ranks)#append that in new dict
        elif ranks.rank() == 12:# if rank is 12
            dict_rank.setdefault(12, []).append(ranks)#append that in new dict
        elif ranks.rank() == 13:# if rank is 13
            dict_rank.setdefault(13, []).append(ranks)#append that in new dict
    return dict_rank
        


def main():
    '''
    main part of the function that assigns the hand 1 and 2, and the commnuity
    cards. each part then runs each hierchitic function, from straight-flush
    to one-pair, counting that high ordering does not need a function
    determines the winter and if the left over cards is less than 9, halts
    '''
    D = cards.Deck()# Decks in cards class; puttig cards on top
    D.shuffle()# shuffle the cards
    my_deck = cards.Deck()# defining the cards
    '''   
    c1= cards.Card(9,4)
    c2= cards.Card(7,2)
    c3= cards.Card(6,2)
    c4= cards.Card(6,3)
    c5= cards.Card(4,4)
    
    community_list = [c1,c2,c3,c4,c5]
    
    c6= cards.Card(4,3)
    c7= cards.Card(7,3)
    c8=cards.Card(10,4)
    c9 =cards.Card(10,3)
    hand_1_list = [c6,c7]
    hand_2_list = [c8,c9]   
    '''
    #F = flush_7(hand_1_list+community_list)
    #print(F)
    
    #H = straight_7(hand_1_list+community_list)
    #print(H)
    
    #dicts = dict_rank_suit(hand_1_list+community_list)
    #print(dicts)
    
    #H = cannonical(hand_1_list+community_list)
    #print(H)
    
   # L = min_in_list(hand_1_list+community_list)
    #print(L)'''
    z =0 # first entry for asking for input
    while True:
        if len(my_deck) <9: # if left over cards less than 9, stops
            print("Deck has too few cards so game is done.")
            break
        if z==1:# after first entry, start asking after rounds
            print()
            inputs = input("Do you wish to play another hand?(Y or N)") 
            if inputs.lower() !='y':# if not y, halts
                break
        
        community_list =[]#create community cards
        for i in range(5):
            community_list.append(my_deck.deal())#assigning the cards
        
        hand_1_list=[]#create Player 1 hand
        hand_2_list=[]#create Player 2 hand

        for i in range(2):
            hand_1_list.append(my_deck.deal()) # assinging the cards
        for i in range(2):
            hand_2_list.append(my_deck.deal()) # assinging the cards  
        
        print(" "+"-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        a = straight_flush_7(hand_1_list+community_list)
        b= straight_flush_7(hand_2_list+community_list)
        if a:# if straight flush in 1, and b tie
            if b:
                print("TIE with a straight flsuh:",a)
                z=1
                continue
            else:# if only a is straight flush, 1 wins
                print("Player 1 wins with a straight flsuh:",a)
                z=1
                continue
        if b:# if hand2 is straight flush, 2 wins
            print("Player 2 wins with a straight flush:",b)
            z=1
            continue
                
        
        c = four_7(hand_1_list+community_list)
        d = four_7(hand_2_list+community_list)
        if c:# if c is four of a kind, and d too, tie
            if d:
                print("TIE with four of a kind:",c)
                z=1
                continue
            else:# other wise, c wins
                print("Player 1 wins with four of a kind:",c)
                z=1
                continue
        if d:# if d is only four of a kind, 2 wins
            print("Player 2 wins with four of a kind:",d)
            z=1
            continue
        
        e = full_house_7(hand_1_list+community_list)
        f = full_house_7(hand_2_list+community_list)
        
        if e:# if 1 is a fulll house and also 2, tie
            if f:
                print("TIE with a full House:",e)
                z=1
                continue
            else:# otherwise, 1 wins
                print("Player 1 wins with a full house:",e)
                z=1
                continue
        if f:# if only 2 has full house, 2 wins
            print("Player 1 wins with a full house:",f)
            
            z=1
            continue
        g =flush_7(hand_1_list+community_list)
        h = flush_7(hand_2_list+community_list)
        
        if g: # g and h both have flush, tie
            if h:
                print("TIE with a flush:",g)
                z=1
                continue
            else: # 1 only, 1 wins
                print("Player 1 wins with a flush:",g)
                z=1
                continue
        if h:# 2 only, 2 wins
            print("Playr 2 wins with a flush:",h)
            z=1
            continue
            
        i =straight_7(hand_1_list+community_list)
        j = straight_7(hand_2_list+community_list)
        if i:# if  1 is striahgt and and also 2, tie
            if j:
                print("TIE with straight:",i)
                z=1
                continue
            else:# only 1 with starihgt, 1 wins
                print("Player 1 wins with straighth:",i)
                z=1
                continue
        if j:# if only 2, 2 wins
            print("Player 2 wins with straighth:",j)
            z=1
            continue
            
        k = three_7(hand_1_list+community_list)
        l = three_7(hand_2_list+community_list)
        if k:
                if l:# both three of a kind, tie
                    print("TIE with three of a kind:",k)
                    z=1
                    continue
                else:# 1 only, 1 wins 
                    print("Player 1 wins with three of a kind:",k)
                    z=1
                    continue
                    
        if l:# 2 only, 2 wins
                print("Player 2 wins with three of a kind:",l)
                z=1
                continue
        m= two_pair_7(hand_1_list+community_list)
        n = two_pair_7(hand_2_list+community_list)
        
        if m:# same as above
            if n:
                print("TIE with two pairs:",m)
                z=1
                continue
            else:
                print("Player 1 wins with two Pairs:",m)
                z=1
                continue
        if n:# same as above
            print("Player 2 wins with two Pairs:",n)
            z=1
            continue
        
        o=one_pair_7(hand_1_list+community_list)
        p=one_pair_7(hand_2_list+community_list)
        
        if o:# same as above
            if p:
                print("TIE with one pair:",o)
                z=1
                continue
            else:
                print("Player 1 with one Pair:",o)
                z=1
                continue
        if p:# same as above
            print("Player 1 wins with one pair:",p)
            z=1
            continue
            
            
if __name__ == "__main__":
    main()