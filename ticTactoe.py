# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:28:16 2019

@author: Sushant Lenka
"""

def print_table(b):
    print('{} | {} | {}'.format(b[0],b[1],b[2]))
    print('{} | {} | {}'.format(b[3],b[4],b[5]))
    print('{} | {} | {}'.format(b[6],b[7],b[8]))
    
def check_win_X(b):
    if b[0]=='X'and b[1]=='X' and b[2]=='X':
        return True 
    elif b[0]=='X' and b[3]=='X' and b[6]=='X':
        return True
    elif b[0]=='X'and b[4]=='X' and b[8]=='X':
        return True
    elif b[1]=='X' and b[4]=='X' and b[7]=='X':
        return True
    elif b[2]=='X' and b[5]=='X' and b[8]=='X':
        return True
    elif b[2]=='X' and b[4]=='X' and b[6]=='X':
        return True
    elif b[3]=='X' and b[4]=='X' and b[5]=='X':
        return True
    elif b[6]=='X' and b[7]=='X' and b[8]=='X':
        return True
    else: return False
        
def check_win_O(b):
    if b[0]=='o'and b[1]=='o' and b[2]=='o':
        return True 
    elif b[0]=='o' and b[3]=='o' and b[6]=='o':
        return True
    elif b[0]=='o'and b[4]=='o' and b[8]=='o':
        return True
    elif b[1]=='o' and b[4]=='o' and b[7]=='o':
        return True
    elif b[2]=='o' and b[5]=='o' and b[8]=='o':
        return True
    elif b[2]=='o' and b[4]=='o' and b[6]=='o':
        return True
    elif b[3]=='o' and b[4]=='o' and b[5]=='o':
        return True
    elif b[6]=='o' and b[7]=='o' and b[8]=='o':
        return True
    else: return False

def check_board_full(b):
    if not '-' in b:
        return True
    else:
        return False
    
def which_player(a):
    if a==1:
        print('Player 1 its your turn')
    elif a==2:
        print('Player 2 its your turn')
        
count=0
player=1
b=['-','-','-','-','-','-','-','-','-']
places_already_filled=[]
print('Player 1 is X ')
print('Player 2 is o')
print('to quit type: bye')
while True:
    if count==0:
        print_table(b)
        count=count+1
    else:
        if not check_board_full(b):
            which_player(player)
            a=input('Enter the position : ')
            if a=='bye':
                break
            a=int(a)
            if not a in range(1,10):
                print('Input not valid')
                continue
            a=a-1
            if player==1:
                if a in places_already_filled:
                    print('oops already filled')
                    continue
                b[a]='X'
                places_already_filled.append(a)
                print_table(b)
                player=2
                if check_win_X(b):
                    print('Player 1 wins')
                    break
            elif player==2:
                if a in places_already_filled:
                    print('oops already filled')
                    continue
                places_already_filled.append(a)
                b[a]='o'
                print_table(b)
                player=1
                if check_win_X(b):
                    print('Player 2 wins')
                    break
        else:
            print('Its a draw')
            break


