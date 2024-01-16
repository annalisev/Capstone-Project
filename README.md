This repository contains a Connect 4 replica game.
You can play either two-player or against the computer.

To play, download the connect4.py file onto your computer. 
Navigate to the directory you downloaded the file into with your terminal, then enter the command 'python3 connect4.py' into your terminal.
From there the game should be self-explanatory, as the programme talks you through the game. 
In essence you want to get 4 of your colours in a row, either vertical, horizontal or diagonal, while blocking your opponent from doing so too.

The file win_checker.py is unnecessary to play the game, as all the code within it is now implemented within the connect4.py file. 
It was mearly for my own use during development of the programme and I have left it in, just for interest (and testing).

--Further Development--
Should you choose to play against the computer, it will pick it's plays randomly from a uniform distribution. This is not a particularly strategic move. (Although on a few occasions it did beat me!)
In the future prehaps I would try to make the computer's moves smarter, however at present I am not sure how to do this!
It would probably require some detection of when the player is close to winning. However my win_checker quite long winded currently and this is only checking if one counter will generate a win.
It is not checking every possible move for a win, or thinking several moves ahead, so I have decided that currentl random moves are most efficient for the computer.
