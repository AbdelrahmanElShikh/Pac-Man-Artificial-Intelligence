#  Introduction : 
Pac-man Game is a game  which the player (The PACMAN) moves around the maze to eat all cheese inside the maze Without being touched by the ghosts who run after him .

![alt text](https://github.com/AbdelrahmanElShikh/Pac-Man-Artificial-Intelligence/blob/master/implementationScreenShot.png)

As this project concerns with The Ai I only implemented the part of the Pac-man and ghosts that the Pac-man can’t go inside the wall (he recognize the walls and stop waiting the player to move him to another position) and the Ghost follow the Pac-Man using **Breadth first Search Algorithm** and if they touched themselves the ghost disappear as a mark that he reached his destination .

#  Descreption
## First we have four classes 
  ### 1-	PlayerClass (The Pac-man)
  ### 2-	GhostClass 
  ### 3-	WallClass (that the player can’t go inside)
  ### 4-	The Main Class 
  before going in details with every class we must mention that the main library I used was Pygame which enabled me to handle user input      from the screen and open the gameplay screen and enabled me to work with sprites to know if the player hit the wall or not.
  
  ### THE PLAYERCLASS :
  **It has 2 methods** 
-	The constructor which is called when we create the player object to initialize it’s variables and to initialize it’s position and image which will be shown on the screen.

-	The Update method which will be called every frame on the game to check the user input and change his position as the player press and check the walls to stop the Pac-man if there a wall in front of his destination.

### THE GHOST CLASS :
**It has 3 methods**
-	The Constructor which initialize the ghost used variable and the grid system that will control the movement of the Ghost.

-	BFS method (implemented by Queue Data Structure) that will look for the path from the start position given to the method as a parameter and return a list contains the (X,Y) positions to the destination.

-	The movement method that call the BFS method and give it the position of the goal (Pac-man position) and the start position (the Ghost current position) and update this method every frame to keep up with the changing position of the Pac-man. 

### The WALL Class :
It has only a constructor that initialize the properties of the wall as its color and dimensions on the screen

### The main Class :	
Which we create an object of each class and display it on the screen and the most important part is the while loop that the whole game code consider be inside it … there we check for the user input and pass it to the player update method to move the player every loop or we can consider it as a frame also we check if the user clicked the red exit button on the screen to close the game and also call the movement method of the ghost to make him follow the  Pac-man at any position he go. 

