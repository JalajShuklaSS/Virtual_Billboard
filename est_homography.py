import numpy as np

def est_homography(X, Y):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by Y. In this assignment, X are the coordinates of the
    four corners of the soccer goal while Y are the four corners of the penn logo.

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in the video frame
        Y: 4x2 matrix of (x,y) coordinates of logo corners in the penn logo
    Returns:
        H: 3x3 homogeneous transformation matrix such that Y ~ H*X

    Explanation:
    This function computes the homography matrix H using the Direct Linear Transform (DLT) method.
    It sets up a system of linear equations using the corresponding points from the goal and the
    penn logo, and then solves for the homography matrix using Singular Value Decomposition (SVD).

    Parameters:
    - X: A 4x2 matrix representing the (x, y) coordinates of the four corners of the soccer goal.
    - Y: A 4x2 matrix representing the (x, y) coordinates of the four corners of the penn logo.

    Returns:
    - H: A 3x3 homogeneous transformation matrix such that Y ~ H*X.

    Example Usage:
    ```python
    X = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    Y = np.array([[x1', y1'], [x2', y2'], [x3', y3'], [x4', y4']])
    H = est_homography(X, Y)
    ```

    Note: Ensure that the input matrices X and Y have correct correspondences.
    """
    A = np.zeros((8, 9))  # Creating an 8x9 matrix
    for i in range(0, 4):
        A[i * 2] = np.array([-X[i][0], -X[i][1], -1, 0, 0, 0, X[i][0] * Y[i][0], X[i][1] * Y[i][0], Y[i][0]])
        A[1 + (i * 2)] = np.array([0, 0, 0, -X[i][0], -X[i][1], -1, X[i][0] * Y[i][1], X[i][1] * Y[i][1], Y[i][1]])

    U, S, V = np.linalg.svd(A, full_matrices=True)  # Implementing Singular Value Decomposition (SVD)
    homography = V[-1, :]  # Extracting the last single vector
    H = homography.reshape((3, 3))  # Reshaping the flattened vector into a 3x3 homography matrix

    return H
