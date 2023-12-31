"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    ####################################################################
    # Generate random indices based on the probabilities
    # First, calculate all the areas for the probabilities
    A, B, C = vertices[faces[:, 0]], vertices[faces[:, 1]], vertices[faces[:, 2]]
    areas = 0.5 * np.linalg.norm(np.cross(B - A, C - A), axis=1)
    probs = areas / np.sum(areas, axis=0)
    indices = np.random.choice(faces.shape[0], size=n_points, p=probs)

    r1 = np.random.rand(n_points)
    r2 = np.random.rand(n_points)

    u = 1 - np.sqrt(r1)
    v = np.sqrt(r1) * (1 - r2)
    w = np.sqrt(r1) * r2

    points = u[:, np.newaxis] * A[indices] + v[:, np.newaxis] * B[indices] + w[:, np.newaxis] * C[indices]

    return points
    ####################################################################
