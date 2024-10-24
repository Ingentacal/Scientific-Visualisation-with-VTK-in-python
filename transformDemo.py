import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtk
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkDiskSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def GetDiscSource():

    colors = vtkNamedColors()
    diskSource = vtkDiskSource()
    diskSource.SetOuterRadius(20)
    diskSource.SetInnerRadius(10)
    diskSource.SetCircumferentialResolution(50)    

    return diskSource

def GetDisc():

    colors = vtkNamedColors()

    diskSource = GetDiscSource()
    
    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(diskSource.GetOutputPort())

    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d("Red"))
    actor.SetMapper(mapper)

    return actor

def GetTranslatedDisc():

    colors = vtkNamedColors()
    diskSource = GetDiscSource()

    # Apply the transforms
    discTransform = vtk.vtkTransform()
    discTransform.Translate(0,0,100)

    # Transform the polydata
    transformPDisc = vtk.vtkTransformPolyDataFilter()
    transformPDisc.SetInputConnection(diskSource.GetOutputPort())
    transformPDisc.SetTransform(discTransform)
    transformPDisc.Update()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(transformPDisc.GetOutputPort())

    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d("Blue"))
    actor.SetMapper(mapper)

    return actor


def main():
    colors = vtkNamedColors()    
    
    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName("Disk")
    renderer.GetActiveCamera().ParallelProjectionOn()    
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    

    # Add the actors to the scene
    disc = GetDisc()
    translatedDisc = GetTranslatedDisc()

    renderer.AddActor(disc)
    renderer.AddActor(translatedDisc)

    renderer.SetBackground(colors.GetColor3d("DarkGreen"))
    renderer.ResetCamera()

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()