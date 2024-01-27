'''
Skeleton code for Gale-Shapley algorithm.
Please do not change the filename or the function names!
'''

import numpy as np

# P1 = np.load('example_1.npy')
# driver = np.array([[3, 3, 2, 3],
#         [4, 1, 3, 2],
#         [2, 4, 4, 1],
#         [1, 2, 1, 4]])
# rider = np.array([[1, 2, 3, 4],
#         [1, 4, 3, 2],
#         [2, 1, 3, 4],
#         [4, 2, 3, 1]])

# P2 = np.load('example_2.npy')


with open('example_1.npy', 'rb') as f:
    P1 = np.load(f)
    P2 = np.load(f)

with open('example_2.npy', 'rb') as f:
    P11 = np.load(f)
    P22 = np.load(f)

print(P1)
print(P2)





# print(P1)
# print(P2)
def is_one_match_per_row(Match):
    '''
    Check if there is exactly one "1" in each row of the match matrix.

    Args:
        Match (numpy.ndarray): an m x n matrix indicating the matches.

    Returns:
        bool: True if there is exactly one "1" in each row, False otherwise.
    '''
    row_sums = np.sum(Match, axis=1)
    return np.all(row_sums == 1)

def GaleShapleyAlgorithm(P1, P2):
    '''
    Runs the Gale-Shapley algorithm, where agents in Group 1 (the group corresponding to P1) propose.

    Args:
        P1 (numpy.ndarray): an m x n matrix describing the preferences of the agents in Group 1. Each column is preference of each of m men.
        P2 (numpy.ndarray): an m x n matrix describing the preferences of the agents in Group 2. Each column is preference of each of n women.

    Returns:
        Match (numpy.ndarray): an m x n matrix which indicates the matches after running the algorithm. See the HW assignment for additional details on the structure of Match.
        NumStages (int): the number of stages that it takes the Gale-Shapley algorithm to return a proposal.
    '''

    ### WRITE YOUR CODE BELOW
    # P1 is proposing
    NumStages = 0
    m, n = np.shape(P1)
    my_dict = {int(i): -1 for i in range(0, m)}
    proposers = set()

    Match = np.zeros((m, n), dtype=int)  # Initialize Match matrix with zeros

    # Arrays to keep track of the proposals received by each man and the current proposal index

    # proposals_received = np.zeros(n, dtype=int)
    # current_proposal = np.zeros(n, dtype=int)

    # Run the Gale-Shapley algorithm
    # print("----------------------------------")
    while (is_one_match_per_row(Match) == False):
        for x, row in enumerate(P1):
            if (x not in proposers):
                y = np.argmin(row)
                # proposal_val is the value that the person being proposed to values to the person proposing
                val = P2[y][x]
                
                if my_dict[y] != -1:
                    # if (NumStages == 1):
                    #     print("here: ", (x,y))
                    #     print(my_dict[y])
                    #     print("row: ", row)
                    #     print(P1)
                    # print("MYDICT: ", my_dict[y])
                    if val < my_dict[y][2]:
                        # Remove the previous proposer from the set
                        proposers.remove(my_dict[y][0])
                        proposers.add(x)
                    
                        
                        
                        P1[x][y] = 10e5
                        Match[my_dict[y][1]][my_dict[y][0]] = 0 
                        Match[y][x] = 1 
                        my_dict[y] = (x, y, val)
                    else:
                        P1[x][y] = 10e5


                else:

                    proposers.add(x)
                    Match[y][x] = 1
                    my_dict[y] = (x, y, val)
                    P1[x][y] = 10e5
                    # print("P1: --------------------------------------------------\n", P1)
                    
                    
        NumStages +=1
        # print("NumStages:", NumStages)
        # print("proposers:", proposers)
        # print("Proposal Dict" ,my_dict)
        # print("Match:\n", Match)

    ### DO NOT EDIT BELOW THIS LINE
    return Match, NumStages

def GaleShapleyAlgorithmQuota(P1, P2, quota):
    '''
    Runs the Gale-Shapley algorithm, where agents in Group 1 (the group corresponding to P1) propose. Each agent in P2 has a number of spots available specified by the variable quota.

    Args:
        P1 (numpy.ndarray): an m x n matrix describing the preferences of the agents in Group 1. Each column is preference of each of m men.
        P2 (numpy.ndarray): an m x n matrix describing the preferences of the agents in Group 2. Each column is preference of each of n women.
        quota (numpy.ndarray): an m x 1 vector describing the quota of each agent in Group 2.

    Returns:
        Match (numpy.ndarray): an m x n matrix which indicates the matches after running the algorithm. See the HW assignment for additional details on the structure of Match.
        NumStages (int): the number of stages that it takes the Gale-Shapley algorithm to return a proposal.
    '''

    ### WRITE YOUR CODE BELOW
    Match = None
    NumStages = None

    ### DO NOT EDIT BELOW THIS LINE
    return Match, NumStages

Match, NumStages = GaleShapleyAlgorithm(P1, P2)