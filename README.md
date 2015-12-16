# TicTacToeNeural-Theano
In this project, a convolutional neural network is tries to learn to play a variant of tic-tac-toe.
### Rules of the game
1. The first player to get 5 continous Xs or Os in a row, column or diagnol wins.


Winning in a row -

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | X | X | X | X | X | _ | _ |

| _ | _ | _ | O | O | _ | O | O | _ | _ |

| _ | _ | _ | _ | _ | _ | O | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |


Winning in a column -

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | X | O | _ | _ | _ | _ | _ |

| _ | _ | _ | X | O | _ | O | O | _ | _ |

| _ | _ | _ | X | _ | _ | O | _ | _ | _ |

| _ | _ | _ | X | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | X | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |


Winning in a right to left diagonal -

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | X | _ | _ |

| _ | _ | _ | _ | _ | _ | X | _ | _ | _ |

| _ | _ | _ | _ | _ | X | _ | O | _ | _ |

| _ | _ | _ | O | X | _ | O | O | _ | _ |

| _ | _ | _ | X | _ | _ | O | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |


Winning in a left to right diagonal -

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | X | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | X | _ | _ | O | _ | _ |

| _ | _ | _ | O | O | X | O | O | _ | _ |

| _ | _ | _ | _ | _ | _ | X | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | X | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

| _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |

