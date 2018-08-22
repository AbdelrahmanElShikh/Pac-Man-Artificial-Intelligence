# Project Introduction : 
Pac-man Game is a game  which the player (The PACMAN) moves around the maze to eat all cheese inside the maze Without being touched by the ghosts who run after him .

![alt text](https://github.com/AbdelrahmanElShikh/Pac-Man-Artificial-Intelligence/blob/master/implementationScreenShot.png)

As this project concerns with The Ai I only implemented the part of the Pac-man and ghosts that the Pac-man can’t go inside the wall (he recognize the walls and stop waiting the player to move him to another position) and the Ghost follow the Pac-Man using **Breadth first Search Algorithm** and if they touched themselves the ghost disappear as a mark that he reached his destination .

# Project Descreption
## First we have four classes 
  ### 1-	PlayerClass (The Pac-man)
  ### 2-	GhostClass 
  ### 3-	WallClass (that the player can’t go inside)
  ### 4-	The Main Class 
  before going in details with every class we must mention that the main library I used was Pygame which enabled me to handle user input      from the screen and open the gameplay screen and enabled me to work with sprites to know if the player hit the wall or not.

