#!/usr/bin/env python
# coding: utf-8

# In[67]:


def game_play(score_board):
    
    options = ['Rock', 'Scissors', 'Paper']
    
    option_translate = {
        'rock' : 'Rock',
        'r' : 'Rock',
        'scissor' : 'Scissors',
        'scissors' : 'Scissors',
        's' : 'Scissors',
        'paper' : 'Paper',
        'p' : 'Paper'
    }
    
    player_choice = input('Rock, Scissors or Paper? (Rock is the default choice) ')
    
    if player_choice == '':
        player_choice = 'Rock'
    
    player_choice = option_translate[player_choice.lower()]
    
    computer_choice = options[random.randint(0, 2)]
    
    print('You chose {} and computer chose {}'.format(player_choice, computer_choice))
    
    if player_choice == computer_choice:
        print('Draw!')
    elif player_choice == 'Rock':
        if computer_choice == 'Scissors':
            print('You win!')
            score_board['player'] += 1
        elif computer_choice == 'Paper':
            print('Computer win!')
            score_board['computer'] += 1
    elif player_choice == 'Scissors':
        if computer_choice == 'Paper':
            print('You win!')
            score_board['player'] += 1
        elif computer_choice == 'Rock':
            print('Computer win!')
            score_board['computer'] += 1
    elif player_choice == 'Paper':
        if computer_choice == 'Rock':
            print('You win!')
            score_board['player'] += 1
        elif computer_choice == 'Scissors':
            print('Computer win!')
            score_board['computer'] += 1
    return score_board


# In[69]:


def play_rock_scissors_paper():
    
    import random
    
    play = 'y'
    
    score_board = {
        'player' : 0,
        'computer' : 0
    }
    
    while play == 'y':
        try:
            score_board = game_play(score_board)
            print(score_board)
            play = input('Do you want to play again? (Y/n) ')
            play = play.lower()
            if play == '' or play =='y':
                play = 'y'
            elif play != 'n':
                print("I don't understand that so I assume you don't want to play again, yes?")
                play = 'n'
            
            if play == 'n':
                print('See ya!')
        except KeyError:
            print('Check your option, you can only choose among Rock, Scissors and Paper')


# In[70]:


play_rock_scissors_paper()

