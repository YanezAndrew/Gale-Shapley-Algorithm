'''
Skeleton code for Gale-Shapley algorithm.
Please do not change the filename or the function names!
'''

import numpy as np

# P1 = np.load('example_1.npy')
driver_1 = np.array([[3, 3, 2, 3],
        [4, 1, 3, 2],
        [2, 4, 4, 1],
        [1, 2, 1, 4]])
rider_1 = np.array([[1, 2, 3, 4],
        [1, 4, 3, 2],
        [2, 1, 3, 4],
        [4, 2, 3, 1]])

# P2 = np.load('example_2.npy')
driver_2 = np.array([[1, 1, 2, 3, 3],
 [2, 3, 1, 1, 2],
 [3, 2, 3, 2, 1]])

rider_2= np.array([[2, 1, 3, 4, 5],
 [3, 1, 2, 5, 4],
 [3, 1, 4, 2, 5]])




# with open('example_1.npy', 'rb') as f:
#     P1 = np.load(f)
#     P2 = np.load(f)
#     P3 = np.load(f)

with open('example_2.npy', 'rb') as f:
    P1 = np.load(f)
    P2 = np.load(f)
    P3 = np.load(f)


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

def has_duplicates(matrix):
    # Check each row for duplicates
    for row in matrix:
        unique_elements = np.unique(row)
        if len(unique_elements) != len(row):
            return True
    return False

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
    P1 = P1.copy()
    P2 = P2.copy()
    NumStages = 0

    # Check the shape of P1 and P2
    m1, n1 = np.shape(P1)
    m2, n2 = np.shape(P2)


    # Transpose P1 if it's column-based
    if has_duplicates(P1):
        P1 = P1.T
    if not has_duplicates(P2):
        P2 = P2.T

    m1, n1 = np.shape(P1)
    m2, n2 = np.shape(P2)
    Match = np.zeros((n2, m1), dtype=int)  # Initialize Match matrix with zeros

    print("Applicants: \n", P1)
    print("Medical Schools: \n", P2)


    my_dict = {int(i): -1 for i in range(0, n2)}
    
    proposers = set()
    all_proposers = set(range(m1))

    while (proposers != all_proposers and is_one_match_per_row(Match) == False):
        for x, row in enumerate(P1):
            if (x not in proposers):
                y = np.argmin(row)
                val = P2[x][y]
                if my_dict[y] != -1:
                    if val < my_dict[y][2]:
                        # Remove the previous proposer from the set
                        proposers.remove(my_dict[y][0])
                        proposers.add(x)
                        P1[x][y] = 10e10
                        Match[my_dict[y][1]][my_dict[y][0]] = 0 
                        Match[y][x] = 1 
                        my_dict[y] = (x, y, val)
                    else:
                        P1[x][y] = 10e10
                else:
                    proposers.add(x)
                    Match[y][x] = 1
                    my_dict[y] = (x, y, val)
                    P1[x][y] = 10e10
        NumStages +=1
        # print("------------------\n")
        # print("NumStages:", NumStages)
        # print("proposers:", proposers)
        # print("Proposal Dict" ,my_dict)
        # print("Match:\n", Match)
        # print(P1)

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
    # P1 is proposing
    P1 = P1.copy()
    P2 = P2.copy()
    NumStages = 0

    # Check the shape of P1 and P2
    m1, n1 = np.shape(P1)
    m2, n2 = np.shape(P2)


    # Transpose P1 if it's column-based
    if has_duplicates(P1):
        P1 = P1.T
    if not has_duplicates(P2):
        P2 = P2.T

    m1, n1 = np.shape(P1)
    m2, n2 = np.shape(P2)
    Match = np.zeros((n2, m1), dtype=int)  # Initialize Match matrix with zeros

    print("Applicants: \n", P1)
    print("Medical Schools: \n", P2)


    my_dict = {int(i): -1 for i in range(0, n2)}
    
    proposers = set()
    all_proposers = set(range(m1))

    while (proposers != all_proposers and is_one_match_per_row(Match) == False):
        for x, row in enumerate(P1):
            if (x not in proposers):
                y = np.argmin(row)
                val = P2[x][y]
                if my_dict[y] != -1:
                    if val < my_dict[y][2]:
                        # Remove the previous proposer from the set
                        proposers.remove(my_dict[y][0])
                        proposers.add(x)
                        P1[x][y] = 10e10
                        Match[my_dict[y][1]][my_dict[y][0]] = 0 
                        Match[y][x] = 1 
                        my_dict[y] = (x, y, val)
                    else:
                        P1[x][y] = 10e10
                else:
                    proposers.add(x)
                    Match[y][x] = 1
                    my_dict[y] = (x, y, val)
                    P1[x][y] = 10e10
        NumStages +=1
        # print("------------------\n")
        # print("NumStages:", NumStages)
        # print("proposers:", proposers)
        # print("Proposal Dict" ,my_dict)
        # print("Match:\n", Match)
        # print(P1)
        
    ### DO NOT EDIT BELOW THIS LINE
    return Match, NumStages

Match, NumStages = GaleShapleyAlgorithm(P1, P2)
print("Number of Stages: " , NumStages)
print("Match: \n", Match)
# Match, NumStages = GaleShapleyAlgorithm(rider_1, driver_1)
# print(Match, NumStages)