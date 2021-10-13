# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:08:20 2021

@author: db_wi
"""


    
def euler054():
    def get_poker_hands(s):
        global vals
                
        r = [ (vals[x[0]],x[1]) for x in s.split(" ") ]
        if len(r) != 10:
            return None
        return (tuple(sorted(r[:5])),tuple(sorted(r[5:])))

    def get_poker_hand_value(hand):
        global vals
        global hand_names
        
        def get_same_values(hand):
            r = []
            c1 = 0
            while c1 < len(hand):
                c = [hand[c1]]
                finished = True
                for c2 in range(c1+1,len(hand)):
                    if hand[c1][0] == hand[c2][0]:
                        c.append(hand[c2])
                    else:
                        c1 = c2 - 1
                        finished = False
                        break
                if len(c) > 1:
                    r.append(c)
                if finished:
                    return r
                c1 += 1
            return r
        
        def is_flush(v):
            for i in range(1,len(v)):
                if v[i][1] != v[i-1][1]:
                    return False
            return True
        
        def is_straight(v):
            for i in range(1,len(v)):
                if v[i][0] != v[i-1][0] + 1:
                    return False
            return True
        
        pairs = get_same_values(hand)
        isf = is_flush(hand)
        iss = is_straight(hand)
        
        royal_flush = (9,)
        straight_flush = (8,)
        four_of_a_kind = (7,)
        full_house = (6,)
        flush = (5,)
        straight = (4,)
        three_of_a_kind = (3,)
        two_pairs = (2,)
        one_pair = (1,)
        high_card = (0,hand[-1][0])
        
        if isf:
            if iss:
                if hand[-1][0] == 14:
                    return royal_flush + (hand[-1][0],)
                return straight_flush + (hand[-1][0],)
            return flush + (hand[-1][0],)
        elif iss:
            return straight + (hand[-1][0],)
        elif pairs:
            if len(pairs) == 1:
                if len(pairs[0]) == 2:
                    return one_pair + (pairs[0][-1][0],)
                if len(pairs[0]) == 3:
                    return three_of_a_kind + (pairs[0][-1][0],)
                return four_of_a_kind + (pairs[0][-1][0],)
                
            
            if len(pairs[0]) == 3:
                return full_house + (pairs[0][-1][0],pairs[1][-1][0])
            if len(pairs[1]) == 3:
                return full_house + (pairs[1][-1][0],pairs[0][-1][0])
            else:
                return two_pairs + tuple(sorted( (p[-1][0] for p in pairs), reverse=True))
        return high_card

        # This isn't working?
        # if we have pairs, we cannot have a straight or flush
        if pairs:
            if len(pairs) == 1:
                if len(pairs[0]) == 2:
                    return one_pair + (pairs[0][-1][0],)
                if len(pairs[0]) == 3:
                    return three_of_a_kind + (pairs[0][-1][0],)
                return four_of_a_kind + (pairs[0][-1][0],)
                
            
            if len(pairs[0]) == 3:
                return full_house + (pairs[0][-1][0],pairs[1][-1][0])
            if len(pairs[1]) == 3:
                return full_house + (pairs[1][-1][0],pairs[0][-1][0])
            else:
                return two_pairs + tuple(sorted((p[-1][0] for p in pairs),reverse=True))
        elif isf:
            if iss:
                if hand[-1][0] == 14:
                    return royal_flush + (hand[-1][0],)
                return straight_flush + (hand[-1][0],)
            return flush + (hand[-1][0],)
        elif iss:
            return straight + (hand[-1][0],)
        return high_card
    
    
    global vals
    vals = dict()
    for v in range(2,10):
        vals[str(v)] = v
    vals["T"] = 10
    vals["J"] = 11
    vals["Q"] = 12
    vals["K"] = 13
    vals["A"] = 14
    vals["C"] = "clubs"
    vals["D"] = "diamonds"
    vals["H"] = "hearts"
    vals["S"] = "spades"
    global hand_names
    hand_names = [
        "high card",
        "one pair",
        "two pairs",
        "three of a kind",
        "straight",
        "flush",
        "full house",
        "four of a kind",
        "straight flush",
        "royal flush"
        ]

    def player_1_wins(p1,p2):
        p1v = get_poker_hand_value(p1)
        p2v = get_poker_hand_value(p2)
        #print(hand_names[p1v[0]],"vs",hand_names[p2v[0]])
        #print(p1v,"vs",p2v)
        for i in range(len(p1v)):
            if p1v[i] > p2v[i]:
                #print("WIN BY BETTER HAND")
                return True
            elif p1v[i] < p2v[i]:
                #print("LOSS BY BETTER HAND")
                return False
            
        # the bug was here and only affected *one* hand in the 1000-hand set
        # the range was not reversed! it was comparing the size of the lowest
        # cards rather than the highest
        for i in reversed(range(len(p1))):
            if p1[i][0] > p2[i][0]:
                #print("WIN BY HIGH CARD")
                #print(p1[i],p2[i])
                return True
            elif p1[i][0] < p2[i][0]:
                #print("LOSS BY HIGH CARD")
                #print(p1[i],p2[i])
                return False
        raise ValueError("Hand values were completely identical\n%s\n%s" % (p1v,p2v))
    testhands = [
        ("5H 5C 6S 7S KD 2C 3S 8S 8D TD",False),
        ("5D 8C 9S JS AC 2C 5C 7D 8S QH",True),
        ("2D 9C AS AH AC 3D 6D 7D TD QD",False),
        ("4D 6S 9H QH QC 3D 6D 7H QD QS",True),
        ("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D",True),
        ]
    for h in testhands:
        a,b = get_poker_hands(h[0])
        #print(a,"VERSUS",b)
        if player_1_wins(a,b) != h[1]:
            print("Calculation error:")
            return None
        
    with open("static/p054_poker.txt","r") as file:
        wins = 0
        ln = 0
        #stolen from some other nerd.... I got annoyed by a bug
        #winning_set = {2, 3, 6, 7, 10, 12, 13, 18, 20, 22, 27, 29, 30, 31, 32, 33, 35, 38, 40, 43, 44, 48, 50, 53, 57, 61, 65, 66, 67, 69, 71, 72, 76, 79, 80, 83, 85, 86, 87, 88, 91, 96, 101, 106, 110, 112, 113, 121, 122, 123, 127, 128, 130, 135, 136, 138, 140, 145, 147, 148, 150, 158, 161, 164, 167, 168, 172, 174, 175, 176, 177, 183, 189, 190, 191, 197, 199, 201, 204, 205, 212, 214, 219, 223, 230, 233, 235, 236, 237, 241, 242, 244, 247, 248, 250, 252, 255, 265, 267, 271, 272, 274, 279, 280, 281, 286, 287, 289, 290, 291, 293, 297, 305, 308, 310, 312, 315, 319, 321, 322, 323, 324, 327, 330, 333, 336, 339, 345, 348, 349, 354, 358, 360, 361, 365, 367, 368, 369, 375, 378, 381, 382, 384, 394, 398, 402, 404, 411, 412, 413, 415, 419, 423, 424, 426, 432, 433, 435, 437, 440, 442, 448, 449, 454, 455, 459, 460, 466, 467, 469, 470, 473, 475, 478, 480, 485, 489, 490, 492, 494, 495, 497, 498, 499, 500, 501, 504, 506, 512, 525, 526, 528, 529, 534, 538, 541, 550, 553, 556, 558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 571, 576, 579, 585, 590, 591, 598, 599, 602, 603, 604, 605, 609, 611, 624, 625, 633, 634, 640, 641, 642, 646, 650, 653, 656, 658, 659, 660, 663, 664, 668, 671, 672, 676, 677, 680, 682, 683, 684, 686, 690, 691, 692, 693, 696, 697, 698, 701, 702, 703, 704, 705, 706, 707, 709, 712, 718, 719, 720, 722, 725, 726, 732, 734, 737, 743, 745, 748, 750, 754, 758, 761, 762, 764, 772, 773, 774, 775, 776, 779, 785, 786, 787, 791, 794, 797, 799, 803, 804, 808, 810, 812, 814, 815, 819, 820, 822, 827, 830, 831, 834, 835, 836, 839, 840, 841, 844, 845, 849, 855, 857, 860, 863, 868, 869, 871, 872, 876, 884, 885, 886, 887, 888, 890, 892, 897, 905, 907, 908, 913, 915, 917, 919, 921, 923, 929, 931, 932, 933, 934, 939, 940, 941, 947, 948, 950, 951, 954, 955, 958, 960, 962, 966, 972, 973, 974, 976, 978, 981, 983, 984, 987, 989, 990, 993, 999, 1000}
        for line in file.readlines():
            ln += 1
            p1, p2 = get_poker_hands(line)
            try:
                if player_1_wins(p1,p2):
                    wins += 1
                    #if ln not in winning_set:
                        #print("ERRONEOUS WIN ON LINE %i:" % ln)
                        #print(
                        #    ', '.join("{}{}".format(a[0],a[1]) for a in p1),
                        #    "vs",
                        #    ', '.join("{}{}".format(b[0],b[1]) for b in p2),
                        #    )
                        #input()
                else:
                    pass
                    #if ln in winning_set:
                        #print("ERRONEOUS LOSS ON LINE %i:" % ln)
                        #print(
                        #    ', '.join("{}{}".format(a[0],a[1]) for a in p1),
                        #    "vs",
                        #    ', '.join("{}{}".format(b[0],b[1]) for b in p2),
                        #    )
                        #input()
            except ValueError as e:
                print(e)
                print(p1)
                print(p2)
                input()

        return wins