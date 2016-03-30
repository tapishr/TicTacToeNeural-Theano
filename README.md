# TicTacToeNeural-Theano
In this code, an attempt is made to get a better understanding of Neural Networks through experiments. A neural network is made to learn how to play 2 variations of Tic Tac Toe and changes are made to the number of nodes in the hidden layer(s) to understand how feature representation gets affected. The Tic Tac Toe game is also represented in 3 different ways for the Neural Network to learn, to see how different reperesentations affect learning.

The 3 types of representation of a Tic Tac Toe game used in the code are -

1. Q-score  - The whole Tic Tac Toe board is given as an input to the network and it is supposed to give a score to the board. Winning board combinations are supposed to have better scores and losing combinations a bad score.
2. Index-score - The Tic Tac Toe boars is given as an input to the network along with an index and the network is supposed to predict whether making a move on that index will be a good choice or bad.
3. Index-probability - The Tic Tac Toe is given as an input and the network is supposed to tell the probability of winning for each possible move.

Representation 1 and 2 mentioned above differ from representation 3 in 2 ways - Firstly, if representation 1 or 2 is used, then for making a move, the network has to be queried multiple times, to ascertain the best possible move. For representation 3, the network gives the best move in a single query.
Secondly, representation 1 and 2 do not learn all the rules of the game. They will never know that it is illegal to make amove on an index of the board where a player has already moved. Representation 3 learns this during its training. However, knowing these rules may not provide any significant advantage.

Experiments are performed to determine which representation is better, first on the normal game of Tic Tac Toe, and secondly for a variant of the game for which rules are given below.

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
