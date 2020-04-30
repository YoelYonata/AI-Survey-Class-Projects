# CMPT 310 - Artifical Intelligence Survey
This is a project that implements concepts from artificial intelligence class into a pacman game. There are four parts of the projects:
Searches, adversarial searches, reinforcement learning and tracking.

## Part 1 - Search
In this part of the project, we were tasked to implement three different searches: Breadth First Search, Depth First Search and A* Search. 

![Search](https://github.com/YoelYonata/AI-Survey-Class-Projects/blob/master/Screenshots/BFS_search.PNG)
*Pacman searching for its food using BFS*

## Part 2 - Adversaries
Adding other agents to the game, Pacman now has to decide his actions depending on his opponents actions. We utilize Minimax, Alpha beta pruning to optimize it and expectimax to further improve pacman's decision. <br/>

![Adversaries](https://github.com/YoelYonata/AI-Survey-Class-Projects/blob/master/Screenshots/Adveraries.PNG)<br/>
*Pacman playing against other ghosts with excpectimax search*

## Part 3 - Reinforcement Learning
This part of the project uses value iteration to solve the MDP problem. However, value iteration solves MDP by observing and not through experience. After implementing, Q-Learning we can see that the agent will go through training first and then into testing. <br/>

![Learning1](/Screenshots/pacman_no_learning.gif)<br/>
*Pacman without training*<br/>

![Learning2](/Screenshots/pacman_with_learning.gif)<br/>
*Pacman after 2000 episodes of training*<br/>

## Part 4 - Tracking
The location of each ghost is hidden and Pacman only has a noisy reading of the location of each ghost. We use particle filtering to figure out where they are. <br/>
![Tracking](https://github.com/YoelYonata/AI-Survey-Class-Projects/blob/master/Screenshots/Tracking.PNG)<br/>
*Pacman tracking ghosts*
