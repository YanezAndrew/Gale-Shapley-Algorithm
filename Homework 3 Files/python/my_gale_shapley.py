'''
Skeleton code for Gale-Shapley algorithm.
Please do not change the filename or the function names!
'''

import numpy as np

P1 = np.load('example_1.npy')
P2 = np.load('example_2.npy')

print(P1)
print(P2)

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

    m, n = np.shape(P1)
    Match = np.zeros((m, n), dtype=int)  # Initialize Match matrix with zeros
    NumStages = 0

    # Keep track of the indices of the women each man has proposed to
    proposals = np.zeros(m, dtype=int)

    while np.sum(Match == 0) > 0:  # Check if there are unmatched men
        for i in range(m):
            if Match[i, proposals[i]] == 0:
                woman = P1[i, proposals[i]]
                
                if 0 <= woman < n:  # Ensure the index is within bounds
                    if Match[:, woman].sum() == 0:
                        Match[i, proposals[i]] = 1
                    else:
                        other_man = np.where(Match[:, woman] == 1)[0][0]
                        if P2[woman, i] < P2[woman, other_man]:
                            Match[i, proposals[i]] = 1
                            Match[other_man, woman] = 0
                else:
                    print("Warning: Invalid woman index:", woman)
                    print("Dimensions of P1:", np.shape(P1))
                    print("Dimensions of Match:", np.shape(Match))

            proposals[i] += 1

        NumStages += 1

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