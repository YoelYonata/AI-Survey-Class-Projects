# CMPT 310 - Artifical Intelligence Survey
This is a project that implements concepts from artificial intelligence class into a pacman game. There are four parts of the projects:
Searches, adversarial searches, reinforcement learning and tracking.

## Part 1 - Search
In this part of the project, we were tasked to implement three different searches: Breadth First Search, Depth First Search and A* Search. Pacman starts at the very top right of the maze and there is one dot of food at the bottom left as seen in the photo. Pacman's goal is to search for the food.
![Search](https://github.com/YoelYonata/AI-Survey-Class-Projects/blob/master/Screenshots/BFS_search.PNG)
*Pacman searching for its food using BFS*

## Part 2 - Adversaries
Adding other agents to the game, Pacman now has to decide his actions depending on his opponents actions. We first start with a simple reflex agent that reacts depending on the action of the ghost. Then, we use Minimax algorithm. Minimax algorithm is optimal when we are assuming that the enemy ghost is trying to minimize our utility, while we (pacman) is trying to maximize the utility. After implementing, minimax, we can optimize the algorithm by using alpha beta pruning. Lastly, we implement expectimax. Since the ghosts in pacman move randomly, we calculate the optimal move by considering the probability of each move from the ghosts.
![Adversaries](https://github.com/YoelYonata/AI-Survey-Class-Projects/blob/master/Screenshots/Adveraries.PNG)
*Pacman playing against other ghosts with excpectimax search*

## Part 3 - Reinforcement Learning
For this part of the project, our agent is in a MDP world. MDP (Markov's Decision Process) means that every decision/action the agent takes, there is a probability that another action may occur. We start with policy iteration and then into Q-Learning. We can also use the Q-learning on our pacman.
![Learning1](/Screenshots/pacman_no_learning.gif)
*Pacman without training*
![Learning2](/Screenshots/pacman_with_learning.gif)
*Pacman after 2000 episodes of training*

## Part 4 - Tracking
![Tracking](https://github.com/YoelYonata/AI-Survey-Class-Projects/blob/master/Screenshots/Tracking.PNG)
*Pacman tracking ghosts*
