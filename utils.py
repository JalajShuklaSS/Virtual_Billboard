import numpy as np
from matplotlib.path import Path

def calculate_interior_pts(image_size, corners):
    """ 
    Calculate_interior_pts takes in the size of an image and a set of corners
    that define a polygon in the image, and returns all (x,y) points within
    the polygon
    
    Input:
        image_size: size of image in [y,x]
        corners: the four corners of a polygon in [x,y] format
    Returns:
        interior_pts: coordinates of points inside polygon in [x,y] format
        
    Explanation:
    This function calculates the interior points within a polygon defined by its corners
    in a given image. It uses the matplotlib.path.Path class to create a path object 
    representing the polygon and then checks each point in the image to determine if it lies
    within the polygon. The interior points are then returned as an array.
    
    Parameters:
    - image_size: A 2-element list [y, x] representing the size of the image.
    - corners: A 4x2 matrix representing the (x, y) coordinates of the four corners of the polygon.

    Returns:
    - interior_pts: An array containing the (x, y) coordinates of points inside the polygon.

    Example Usage:
    ```python
    image_size = [height, width]
    corners = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    interior_pts = calculate_interior_pts(image_size, corners)
    ```

    Note: Ensure that the corners are provided in the correct order (clockwise or counterclockwise).
    """


    path = Path(corners)

    xx, yy = np.meshgrid(range(image_size[1]), range(image_size[0]))
    xxyy = np.stack([xx.ravel(), yy.ravel()], 1)

    interior_ind = path.contains_points(xxyy)
    interior_pts = xxyy[interior_ind]
    
    return interior_pts


def inverse_warping(img_initial, img_final, pts_initial, pts_final):
    """ 
    Takes two images and a set of correspondences between them, 
    and warps all the pts_initial in img_initial to the pts_final in img_final

    Input:
        img_initial: Initial image on top of which we want to overlay img_final
        img_final:   Target image to lay on top of img_initial
        pts_initial: Nx2 matrix of (x,y) coordinates of points in video frame
        pts_final:   Nx2 matrix of (x,y) coordinates of points in penn logo
    Returns:
        projected_img: 
        
    Explanation:
    This function performs inverse warping by replacing the specified points in the initial image 
    with the corresponding points from the final image. The input points are provided as matrices
    containing (x, y) coordinates. The resulting image, projected_img, is a combination of the initial 
    and final images based on the specified correspondences.

    Parameters:
    - img_initial: The initial image on top of which the final image will be overlaid.
    - img_final: The target image to lay on top of the initial image.
    - pts_initial: A Nx2 matrix representing the (x, y) coordinates of points in the video frame.
    - pts_final: A Nx2 matrix representing the (x, y) coordinates of points in the penn logo.

    Returns:
    - projected_img: An image resulting from the overlay of img_final on img_initial based on the specified correspondences.

    Example Usage:
    ```python
    projected_img = inverse_warping(img_initial, img_final, pts_initial, pts_final)
    ```

    Note: The input matrices pts_initial and pts_final should have the same number of points (N) and be in the correct order.
    """
    pts_final = pts_final.astype(int)
    pts_initial = pts_initial.astype(int)
    
    projected_img = img_initial.copy()
    for i in range(3):
        sub_img_i = img_initial[:,:,i][pts_initial[:,1], pts_initial[:,0]]
        sub_img_f = img_final[:,:,i][pts_final[:,1], pts_final[:,0]]
        
        # sub_img = sub_img_i*1 + sub_img_f*1
        sub_img = sub_img_f*1 
        projected_img[:,:,i][pts_initial[:,1], pts_initial[:,0]] = sub_img
        
    return projected_img
