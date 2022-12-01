# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-10.57.30 176069
# Run by ethan on Fri Nov 11 21:41:10 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=232.749984741211, 
    height=86.1111145019531)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('d15w6.cae')
#: The model database "D:\Personal\ISEF\Mechanical\simulation\d15w6\d15w6.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['d15w6']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
odb = session.mdbData['Model-1']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.mdbData['Model-1'])
o3 = session.openOdb(
    name='D:/Personal/ISEF/Mechanical/simulation/d15w6/Job-1.odb')
#: Model: D:/Personal/ISEF/Mechanical/simulation/d15w6/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    translucency=ON)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    legendNumberFormat=FIXED, title=OFF, state=OFF, annotations=OFF)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].view.setValues(nearPlane=6928.88, 
    farPlane=14868.6, width=6950.64, height=3185.37, cameraPosition=(5455.71, 
    7945.45, 5470.25), cameraUpVector=(0.0322606, 0.0224622, -0.999227), 
    cameraTarget=(50.3593, -785.105, 1416.79))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8306.01, 
    farPlane=13952, width=8332.09, height=3818.47, cameraPosition=(10934.3, 
    -768.121, 2813.82), cameraUpVector=(-0.217203, 0.281905, -0.934533), 
    cameraTarget=(-20.3931, -672.575, 1451.1))
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8166.34, 
    farPlane=13875.6, cameraPosition=(11019.8, -638.271, 1454.96), 
    cameraUpVector=(-0.333047, 0.301813, -0.893302), cameraTarget=(-19.7057, 
    -671.531, 1440.17))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8912.62, 
    farPlane=13129.3, width=1269.95, height=582, cameraPosition=(11018.8, 
    -812.599, 2584.1), cameraTarget=(-20.6932, -845.859, 2569.31))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8903.21, 
    farPlane=13139.3, cameraPosition=(11018.4, -749.895, 2606.26), 
    cameraUpVector=(-0.332945, 0.298105, -0.894585), cameraTarget=(-20.6925, 
    -845.965, 2569.28))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(11018.4, 
    -749.895, 2606.26), cameraUpVector=(-0.333026, 0.306346, -0.891766), 
    cameraTarget=(-20.6925, -845.965, 2569.28))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8205.89, 
    farPlane=13427.8, cameraPosition=(10479.2, 2560.59, 2549.03), 
    cameraUpVector=(-0.400874, 0.149631, -0.903831), cameraTarget=(-19.7964, 
    -851.467, 2569.38))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8905.76, 
    farPlane=13110, cameraPosition=(11008.7, -734.307, 2570.1), 
    cameraUpVector=(-0.334656, 0.316405, -0.887634), cameraTarget=(-30.701, 
    -783.615, 2568.95))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7932.26, 
    farPlane=14083.4, width=13116.3, height=6010.99, cameraPosition=(11003.3, 
    512.282, 1176.07), cameraTarget=(-36.1237, 462.974, 1174.92))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7996.52, 
    farPlane=14019.1, cameraPosition=(11003.3, 512.282, 1176.07), 
    cameraUpVector=(-0.333211, -0.00587222, -0.942834), cameraTarget=(-36.1238, 
    462.974, 1174.92))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(11016.6, 
    -2457.69, 529.324), cameraTarget=(-22.7909, -2507, 528.174))
session.Viewport(name='Viewport: 2', origin=(7.0, -141.388900756836), 
    width=436.916656494141, height=220.833343505859)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].maximize()
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 2'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0.0, -141.388900756836), 
    width=248.20832824707, height=227.500015258789)
session.viewports['Viewport: 2'].setValues(origin=(248.20832824707, 
    -141.388900756836), width=248.20832824707, height=227.500015258789)
session.viewports['Viewport: 2'].view.setValues(nearPlane=4841.89, 
    farPlane=15570, cameraPosition=(9304.65, 1506.59, -3790.75), 
    cameraUpVector=(-0.632474, -0.241371, -0.736014), cameraTarget=(-17.8639, 
    -2518.41, 540.607))
session.viewports['Viewport: 2'].view.setValues(nearPlane=4696.82, 
    farPlane=15700.6, cameraPosition=(8691.43, 1546.12, -4878.88), 
    cameraUpVector=(-0.676614, -0.345109, -0.650455), cameraTarget=(32.2214, 
    -2521.64, 629.481))
session.viewports['Viewport: 2'].view.setValues(nearPlane=4773.87, 
    farPlane=15733.6, cameraPosition=(8779.95, 1304.31, -4911.68), 
    cameraUpVector=(-0.688891, -0.325546, -0.647648), cameraTarget=(24.9241, 
    -2501.71, 632.185))
session.viewports['Viewport: 2'].view.setValues(cameraPosition=(8779.95, 
    1304.31, -4911.68), cameraUpVector=(-0.676439, -0.352643, -0.646586), 
    cameraTarget=(24.9241, -2501.71, 632.185))
session.viewports['Viewport: 2'].view.setValues(nearPlane=4552.63, 
    farPlane=15649.4, cameraPosition=(8437.12, 1970.78, -4940.91), 
    cameraUpVector=(-0.664889, -0.376206, -0.645284), cameraTarget=(51.1956, 
    -2552.78, 634.425))
session.viewports['Viewport: 2'].view.setValues(cameraPosition=(7084.35, 
    3744.86, -5536.23), cameraTarget=(-1301.58, -778.698, 39.1082))
session.viewports['Viewport: 2'].view.setValues(nearPlane=5348.06, 
    farPlane=14854, width=7515.57, height=6706.61, cameraPosition=(7437.43, 
    3768.05, -4986.35), cameraTarget=(-948.504, -755.512, 588.985))
session.viewports['Viewport: 2'].view.setValues(nearPlane=5392.09, 
    farPlane=14840, cameraPosition=(7115.33, 4032.11, -5233.58), 
    cameraUpVector=(-0.668946, -0.405011, -0.623279), cameraTarget=(-918.578, 
    -780.045, 611.955))
session.viewports['Viewport: 2'].view.setValues(cameraPosition=(7469.21, 
    4038.4, -4742.04), cameraTarget=(-564.694, -773.757, 1103.5))
session.viewports['Viewport: 2'].view.setValues(nearPlane=5648.03, 
    farPlane=14584, width=6242.31, height=5570.4, cameraPosition=(7458.39, 
    4079.49, -4723.08), cameraTarget=(-575.514, -732.664, 1122.46))
session.viewports['Viewport: 2'].view.setValues(cameraPosition=(7349.11, 
    4065.08, -4885.14), cameraTarget=(-684.792, -747.082, 960.4))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7971.71, 
    farPlane=14043.9, width=6242.31, height=5570.4, cameraPosition=(11008.4, 
    -622.391, 201.362), cameraTarget=(-30.9545, -671.701, 200.212))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8033.59, 
    farPlane=13982, cameraPosition=(11008.7, -674.019, 272.293), cameraTarget=(
    -30.7313, -723.329, 271.143))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(11008.7, 
    -674.019, 272.293), cameraUpVector=(-0.333258, 0.00469583, -0.942824), 
    cameraTarget=(-30.7313, -723.329, 271.143))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8033.64, 
    farPlane=13982.1, width=5867.77, height=5236.18, cameraPosition=(11008.7, 
    -672.424, 266.762), cameraTarget=(-30.7378, -721.734, 265.612))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8091.81, 
    farPlane=13923.9, cameraPosition=(11007, -296.542, 402.129), cameraTarget=(
    -32.4309, -345.852, 400.979))
session.viewports['Viewport: 1'].view.setValues(width=5515.71, height=4922.01, 
    cameraPosition=(11007.1, -314.286, 394.836), cameraTarget=(-32.3509, 
    -363.596, 393.686))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8146.5, 
    farPlane=13869.2, cameraPosition=(11007.2, -354.865, 581.96), 
    cameraTarget=(-32.1891, -404.175, 580.81))
session.viewports['Viewport: 2'].view.setValues(width=5867.77, height=5236.18, 
    cameraPosition=(7336.24, 4072.1, -4897.06), cameraTarget=(-697.667, 
    -740.063, 948.484))
session.viewports['Viewport: 2'].view.setValues(nearPlane=5648.03, 
    farPlane=14584, cameraPosition=(7357.27, 4084.91, -4857.6), cameraTarget=(
    -676.631, -727.25, 987.942))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t4.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=10)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=10)
session.printOptions.setValues(vpDecorations=OFF)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t3.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=14)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=14)
session.viewports['Viewport: 1'].makeCurrent()
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t4.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=7)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=7)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t2.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=4)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=3)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t1.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t1.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports['Viewport: 1'].makeCurrent()
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t0.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=10)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=10)
session.viewports['Viewport: 1'].makeCurrent()
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t3.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    compass=OFF)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
    compass=OFF)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=10)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6//d15w6 t3.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6//d15w6 t3.png', 
    format=SVG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t3.png', 
    format=SVG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t3', 
    format=SVG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t3_1', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.printOptions.setValues(reduceColors=False)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d15w6/images/d15w6 t3_1', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d15w6\d15w6.cae".
