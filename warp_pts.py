import numpy as np
from est_homography import est_homography

def warp_pts(X, Y, interior_pts):
    """
    Compute homography from video_pts to logo_pts using X and Y,
    then use this homography to warp all points inside the soccer goal.

    Input:
        X: 4x2 matrix of (x, y) coordinates of goal corners in the video frame
        Y: 4x2 matrix of (x, y) coordinates of logo corners in the penn logo
        interior_pts: Nx2 matrix of points inside the goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
                    These coordinates describe where a point inside the goal will be warped
                    to inside the penn logo. For this assignment, you can keep these new
                    coordinates as float numbers.

    Explanation:
    This function takes the coordinates of the corners of the soccer goal in the video frame (X),
    the coordinates of the corners of the penn logo (Y), and a matrix of interior points inside the goal.
    It computes the homography matrix (H) using the est_homography function and then uses this matrix to
    warp all interior points from the video frame to the penn logo frame.

    Parameters:
    - X: A 4x2 matrix representing the (x, y) coordinates of the four corners of the soccer goal.
    - Y: A 4x2 matrix representing the (x, y) coordinates of the four corners of the penn logo.
    - interior_pts: An Nx2 matrix representing (x, y) coordinates of points inside the soccer goal.

    Returns:
    - warped_pts: An Nx2 matrix containing new coordinates for interior_pts after warping.

    Example Usage:
    ```python
    X = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    Y = np.array([[x1', y1'], [x2', y2'], [x3', y3'], [x4', y4']])
    interior_pts = np.array([[x1, y1], [x2, y2], ..., [xn, yn]])
    warped_pts = warp_pts(X, Y, interior_pts)
    ```

    Note: Ensure that X and Y have the correct correspondences.
    """
    H = est_homography(X, Y)
    warped_pts = np.ones((np.shape(interior_pts)[0], 2))

    for i in range(0, np.shape(interior_pts)[0]):
        warped_pts[i][0] = ((H[0][0] * interior_pts[i][0] + H[0][1] * interior_pts[i][1] + H[0][2])) / (
                    (H[2][0] * interior_pts[i][0] + H[2][1] * interior_pts[i][1] + H[2][2]))
    for i in range(0, np.shape(interior_pts)[0]):
        warped_pts[i][1] = ((H[1][0] * interior_pts[i][0] + H[1][1] * interior_pts[i][1] + H[1][2])) / (
                    (H[2][0] * interior_pts[i][0] + H[2][1] * interior_pts[i][1] + H[2][2]))

    return warped_pts
