'''
Skeleton code for Gale-Shapley algorithm.
Please do not change the filename or the function names!
'''

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
    Match = None
    NumStages = None

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