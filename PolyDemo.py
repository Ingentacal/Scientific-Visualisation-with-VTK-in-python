import vtk

def Surface():

    # Create points for the vertices of the polygon
    points = vtk.vtkPoints()
    points.InsertNextPoint(0, 0, 0)  # Vertex 1
    points.InsertNextPoint(5, 1, 0)  # Vertex 2
    points.InsertNextPoint(6, 2, 0)  # Vertex 3
    points.InsertNextPoint(4, 5, 0)  # Vertex 4
    points.InsertNextPoint(2, 6, 0)  # Vertex 5

    # Create a cell array to define the polygon
    polygon = vtk.vtkCellArray()
    polygon.InsertNextCell(5)  # 5 vertices in the polygon
    polygon.InsertCellPoint(0)  # Vertex 1
    polygon.InsertCellPoint(1)  # Vertex 2
    polygon.InsertCellPoint(2)  # Vertex 3
    polygon.InsertCellPoint(3)  # Vertex 4
    polygon.InsertCellPoint(4)  # Vertex 5

    # Create a polydata object and set the points and cells
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetPolys(polygon)

    # Create a mapper and connect it to the polydata
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)

    # Create an actor and set its mapper
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    #actor.GetProperty().SetColor(1.0,0.0,0.0)

    return actor


