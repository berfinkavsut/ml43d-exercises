"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """

    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    with open(path, 'w') as file:
        for vertex in vertices:
            v_str = 'v' + ' ' + str(vertex[0]) + ' ' + str(vertex[1]) + ' ' + str(vertex[2]) + ' \n'
            file.write(v_str)

        for face in faces:
            f_str = 'f' + ' ' + str(face[0]) + ' ' + str(face[1]) + ' ' + str(face[2]) + ' \n'
            file.write(f_str)
    return
    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    # TODO: Implement
    raise NotImplementedError
    # ###############
