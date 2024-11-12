import os , sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, QIcon , QPixmap
import vtkviewer as vtkView

class vtkWnd(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.Parent = parent
        if(self.Parent == None):
            self.resize(550, 400)

        self.Mainlayout = QVBoxLayout()
        self.setLayout(self.Mainlayout)

        #Add Toolbar
        self.vtk3DView = vtkView.vtkViewer(self)
        self.ViewToolbar = QToolBar("View", self) 
        self.CreateActions()
        self.CreateToolbar() 

        #Add Vtk Window        
        self.Mainlayout.addWidget(self.vtk3DView) 

    def CreateActions(self):
        path = os.path.join(os.path.dirname(__file__), 'icons\\front.svg')
        self.frontAction = QAction(QIcon(QPixmap(path)), "&Front...", self)
        self.frontAction.triggered.connect(self.vtk3DView.OnFrontView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\front.svg')
        self.frontAction = QAction(QIcon(QPixmap(path)), "&Front...", self)
        self.frontAction.triggered.connect(self.vtk3DView.OnFrontView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\back.svg')
        self.backAction = QAction(QIcon(QPixmap(path)), "&Back...", self)
        self.backAction.triggered.connect(self.vtk3DView.OnBackView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\top.svg')
        self.topAction = QAction(QIcon(QPixmap(path)), "&Top...", self)
        self.topAction.triggered.connect(self.vtk3DView.OnTopView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\bottom.svg')
        self.bottomAction = QAction(QIcon(QPixmap(path)), "&Bottom...", self)
        self.bottomAction.triggered.connect(self.vtk3DView.OnBottomView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\left.svg')
        self.leftAction = QAction(QIcon(QPixmap(path)), "&Left...", self)
        self.leftAction.triggered.connect(self.vtk3DView.OnLeftView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\right.svg')
        self.rightAction = QAction(QIcon(QPixmap(path)), "&Right...", self)
        self.rightAction.triggered.connect(self.vtk3DView.OnRightView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\iso.svg')
        self.isoAction = QAction(QIcon(QPixmap(path)), "&Iso...", self)
        self.isoAction.triggered.connect(self.vtk3DView.OnIsometricView)

        path = os.path.join(os.path.dirname(__file__), 'icons\\resize.svg')
        self.fitAction = QAction(QIcon(QPixmap(path)), "&Fit...", self)
        self.fitAction.triggered.connect(self.vtk3DView.OnFitView)

    def CreateToolbar(self):                
        self.ViewToolbar.addAction(self.frontAction)
        self.ViewToolbar.addAction(self.backAction)
        self.ViewToolbar.addAction(self.topAction)
        self.ViewToolbar.addAction(self.bottomAction)
        self.ViewToolbar.addAction(self.leftAction)
        self.ViewToolbar.addAction(self.rightAction)
        self.ViewToolbar.addAction(self.isoAction)
        self.ViewToolbar.addAction(self.fitAction)
        self.Mainlayout.addWidget(self.ViewToolbar) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = vtkWnd(None)
    window.setWindowTitle('vtkSCVis - Vtk Viewer')
    window.show()
    sys.exit(app.exec())