# TicTacToeNeural-Theano
In this project, a convolutional neural network tries to learn how to play a variant of tic-tac-toe.
### Rules of the game
The first player to get 5 continous Xs or Os in a row, column or diagnol wins.

Winning in a row -

![Winning in a Row image](https://github.com/tapishr/TicTacToeNeural-Theano/blob/master/Markdown/Images/winning_in_row.png)


Winning in a column -

![Winning in a Row image](https://github.com/tapishr/TicTacToeNeural-Theano/blob/master/Markdown/Images/winning_in_col.png)


Winning in a right to left diagonal -

![Winning in a Row image](https://github.com/tapishr/TicTacToeNeural-Theano/blob/master/Markdown/Images/winning_in_rldiagonal.png)


Winning in a left to right diagonal -

![Winning in a Row image](https://github.com/tapishr/TicTacToeNeural-Theano/blob/master/Markdown/Images/winning_in_lrdiagonal.png)

### Contents

- learner.py - contains the CNN, implemented using Theano.
- player.py - implements the player of Tic Tac Toe
- judge.py - implements a judge which checks if illegal moves have been made. It also decides and declares the winner.
- game.py - initializes the game, the players and the judge.
- learner3X3.py - CNN for learning the normal 3 X 3 version of Tic Tac Toe.
