import sys
from PySide6.QtWidgets import QApplication

import vtk
import vtkmodules.qt.QVTKRenderWindowInteractor as QVTK
from PySide6.QtWidgets import QWidget

import PolyDemo as PD

class vtkViewer(QWidget):
    def __init__(self, parent):
        super(vtkViewer,self).__init__()
        self.Parent = parent

        if(self.Parent == None):
            self.resize(500, 500)

        # vtk initialization
        self.QVTKRenderWindowInteractor = QVTK.QVTKRenderWindowInteractor
        self.renderer = None
        self.interactor = None
        self.TrihedronPos = 1
        '''1 = Lower Left , 2 = Lower Right''' 
        self.ShowEdges = True

        self.SetupWnd()

    def SetupWnd(self):
        self.SetupRenderer()
        self.SetupTrihedron()

    def SetupRenderer(self):
        self.renderer = vtk.vtkRenderer()

        # Set background color of the renderer
        self.renderer.SetBackground(0.2, 0.3, 0.4)  # RGB color

        self.interactor = self.QVTKRenderWindowInteractor(self)
        
        self.trackball = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(self.trackball) 

        self.interactor.GetRenderWindow().AddRenderer(self.renderer)
        self.interactor.GetRenderWindow().PointSmoothingOn()
        self.interactor.GetRenderWindow().LineSmoothingOn()
        self.interactor.Initialize()
        self.interactor.Start()

    def UpdateView(self):
        self.interactor.ReInitialize()
        self.interactor.GetRenderWindow().Render()
        self.repaint()

    def paintEvent(self, ev):
        size = self.size()
        self.interactor.GetRenderWindow().SetSize(size.width(),size.height())

    def MakeAxesActor(self):
        axes = vtk.vtkAxesActor()
        axes.SetShaftTypeToCylinder()
        axes.SetXAxisLabelText('X')
        axes.SetYAxisLabelText('Y')
        axes.SetZAxisLabelText('Z')
        axes.SetTotalLength(1.5, 1.5, 1.5)
        axes.SetCylinderRadius(0.5 * axes.GetCylinderRadius())
        axes.SetConeRadius(1.025 * axes.GetConeRadius())
        axes.SetSphereRadius(1.5 * axes.GetSphereRadius())
        return axes

    def SetupTrihedron(self):
        self.Trihedron = self.MakeAxesActor()
        self.om1 = vtk.vtkOrientationMarkerWidget()
        self.om1.SetOrientationMarker(self.Trihedron)
        self.om1.SetInteractor(self.interactor)
        self.om1.EnabledOn()
        self.om1.InteractiveOff() 

    def ResizeTrihedron(self, width, height):
        if self.Trihedron:
            if(width==0):
                width=100
            if(height==0):
                height=100
            
            if self.TrihedronPos==1: # Position lower Left in the viewport.
                self.om1.SetViewport(0, 0, (200.0 / width), (200.0 / height)) 
            
            if self.TrihedronPos==2: # Position lower Right in the viewport.
                self.om1.SetViewport(1 - (200.0 / width), 0, 1, (200.0 / height))

    def resizeEvent(self, ev):
        self.interactor.GetRenderWindow().SetSize(self.size().width(),self.size().height())
        self.ResizeTrihedron(self.size().width(),self.size().height())  

    def ResetCamera(self):
        self.renderer.ResetCamera()
        self.camera = self.renderer.GetActiveCamera()
        self.camera.ParallelProjectionOn()

    def AddActor(self, pvtkActor):
        if self.ShowEdges:
            pvtkActor.GetProperty().EdgeVisibilityOn()

        self.renderer.AddActor(pvtkActor)
        self.ResetCamera()        

    def RemoveActor(self, pvtkActor):
        self.renderer.RemoveActor(pvtkActor)
        self.ResetCamera()

    def SetRepresentation(self, aTyp):
        ''' aTyp = 1 - Points
            aTyp = 2 - Wireframe 
            aTyp = 3 - Surface
            aTyp = 4 - Surface with edges
        '''
        num_actors = self.renderer.GetActors().GetNumberOfItems()
        for i in range(num_actors):
            actor = self.renderer.GetActors().GetItemAsObject(i)
            if(aTyp==1):
                actor.GetProperty().SetRepresentationToPoints()
                actor.GetProperty().SetPointSize(4.0)  
                self.ShowEdges = False              

            if(aTyp==2):
                actor.GetProperty().SetRepresentationToWireframe()
                self.ShowEdges = False

            if(aTyp==3):
                actor.GetProperty().SetRepresentationToSurface()
                actor.GetProperty().EdgeVisibilityOff()
                self.ShowEdges = False

            if(aTyp==4):
                actor.GetProperty().SetRepresentationToSurface()
                actor.GetProperty().EdgeVisibilityOn()
                self.ShowEdges = True

        self.UpdateView()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = vtkViewer(None)
    window.setWindowTitle('vtkSCVis - Vtk Viewer')
    window.AddActor(PD.Surface())
    window.SetRepresentation(4)
    window.show()
    sys.exit(app.exec())

