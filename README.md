Pacman Search Algorithms
This project implements various search algorithms to help "Mr. Pacman" find food in the shortest time possible. The goal is to compare the efficiency of different search algorithms, including both uninformed and informed approaches.

Introduction
The project explores a variety of search algorithms to navigate Pacman through a maze. We evaluate their performance in finding the shortest path, comparing the following algorithms:

Breadth-First Search (BFS)
Depth-First Search (DFS)
Uniform Cost Search (UCS)
A Search*
Bidirectional Search
Weighted A Search*
Additionally, a graphical version of Miss Pacman is implemented to visualize the movement of the character, enhancing the project’s interactivity and visual appeal.

Algorithms
1. BFS (Breadth-First Search)
BFS explores the shallowest nodes first and guarantees an optimal solution if the cost of each action is the same. It uses a FIFO queue to explore nodes level by level.

2. DFS (Depth-First Search)
DFS explores nodes deeply before moving to the next one. It's less efficient than BFS for this problem since it does not guarantee an optimal solution.

3. UCS (Uniform Cost Search)
UCS extends the lowest cost node first and guarantees optimal solutions. It uses a priority queue and is more efficient than BFS when the cost of edges differs.

4. A Search*
A* Search uses both the actual cost (g) and a heuristic (h) to find the optimal path efficiently. It is informed, and when using a good heuristic, it performs better than UCS.

5. Bidirectional Search
This algorithm simultaneously searches from the start and the goal. It can be faster than BFS or DFS by meeting in the middle.

6. Weighted A Search*
A modification of A*, Weighted A* introduces an epsilon factor that allows for more flexible exploration, making it more greedy or uniform depending on the value of epsilon.

Implementation
The core of the project is built using Python. The following search algorithms are implemented within the search.py file:

breadthFirstSearch
depthFirstSearch
uniformCostSearch
aStarSearch
bidirectional
weightedAStarSearch
Each search algorithm is applied to solve the Pacman maze problem, and their performance is compared based on execution time and path length.

Graphical Interface
The graphical interface is implemented for both Miss Pacman and Mr. Pacman. Miss Pacman has a distinctive purple bow, blue eyes, and playful facial features. The graphical system is based on a custom design built using a basic graphics library.

How to Run the Code
1. Clone the Repository

git clone https://github.com/your-username/pacman-search.git
cd pacman-search

2. Install Dependencies
Make sure you have Python 3 installed. You can use pip to install any required dependencies.
pip install -r requirements.txt

3. Running the Search Algorithms
You can test different algorithms using the following commands:

Breadth-First Search:
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

Depth-First Search:
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

Uniform-Cost Search:
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

A Search*:
python pacman.py -l mediumMaze -p SearchAgent -a fn=aStar

Bidirectional Search:
python pacman.py -l mediumMaze -p SearchAgent -a fn=bi

Weighted A Search*:
python pacman.py -l bigMaze -p SearchAgent -a fn=wastar

4. Running the Graphics
To test the graphical implementation, you can run:
python pacman.py -l mediumMaze -p MissPacman

Testing and Evaluation
Each algorithm’s performance is evaluated based on its ability to find the shortest path efficiently. The project includes an autograder that tests the implementation of each search algorithm.

Example:
python autograder.py

Conclusion
This project showcases the implementation and comparison of various search algorithms in the context of Pacman. By analyzing the performance of each algorithm, we aim to understand the trade-offs between different approaches, such as the completeness, optimality, and efficiency of BFS, DFS, UCS, A*, and others. The results help in selecting the most appropriate search strategy for navigating in maze-like environments.
