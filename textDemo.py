import vtk

# Create a mapper
colors = vtk.vtkNamedColors()
    
text_mapper = vtk.vtkTextMapper()
text_mapper.SetInput("INGENTACAL")
text_mapper.GetTextProperty().ItalicOn()
text_mapper.GetTextProperty().BoldOn()
text_mapper.GetTextProperty().SetFontSize(24)

# Create a text actor
text_actor = vtk.vtkActor2D()
text_actor.SetMapper(text_mapper)
text_actor.GetProperty().SetColor(colors.GetColor3d('White'))  # Set text color (white)
text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
text_actor.GetPositionCoordinate().SetValue(0.05, 0.05)

text_mapper2 = vtk.vtkTextMapper()
text_mapper2.SetInput("Engineering Solutions")
text_mapper2.GetTextProperty().SetFontSize(15)

text_actor2 = vtk.vtkActor2D()
text_actor2.SetMapper(text_mapper2)
text_actor2.GetProperty().SetColor(colors.GetColor3d('White'))  # Set text color (white)
text_actor2.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
text_actor2.GetPositionCoordinate().SetValue(0.05, 0.02)

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.2, 0.3, 0.4)  # Set background color for the renderer

# Add the text actor to the renderer
renderer.AddActor(text_actor)
renderer.AddActor(text_actor2)

# Create a render window and add the renderer to it
render_window = vtk.vtkRenderWindow()
render_window.SetSize(400, 400)
render_window.AddRenderer(renderer)

# Create an interactor and start the interaction
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the interaction
interactor.Start()