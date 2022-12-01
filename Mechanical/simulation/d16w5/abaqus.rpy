# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-10.57.30 176069
# Run by ethan on Fri Nov 11 22:20:19 2022
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
openMdb('d16w5.cae')
#: The model database "D:\Personal\ISEF\Mechanical\simulation\d16w5\d16w5.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['d16w5']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Error in job Job-1: Time increment required is less than the minimum specified
#: Error in job Job-1: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job Job-1: Abaqus/Standard aborted due to errors.
#: Error in job Job-1: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-1 aborted due to errors.
o3 = session.openOdb(
    name='D:/Personal/ISEF/Mechanical/simulation/d16w5/Job-1.odb')
#: Model: D:/Personal/ISEF/Mechanical/simulation/d16w5/Job-1.odb
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
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    legendNumberFormat=FIXED, title=OFF, state=OFF, annotations=OFF, 
    compass=OFF)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    translucency=ON)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=7932.48, 
    farPlane=15622.9, width=4086.62, height=3646.75, cameraPosition=(-5947.84, 
    9120.13, 2812.8), cameraUpVector=(-0.0434113, -0.227015, -0.972923), 
    cameraTarget=(-903.605, -541.861, 1059.95))
session.viewports['Viewport: 2'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7921.42, 
    farPlane=15511.9, cameraPosition=(-6433.43, 9024.36, 947.037), 
    cameraUpVector=(0.0209102, -0.372024, -0.927988), cameraTarget=(-934.04, 
    -547.863, 943.012))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-6433.43, 
    9024.36, 947.037), cameraUpVector=(0.176054, -0.282885, -0.942858), 
    cameraTarget=(-934.04, -547.863, 943.012))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8110.75, 
    farPlane=15322.6, width=4423.7, height=3947.54, cameraPosition=(-6281.46, 
    9111.64, 1019.88), cameraTarget=(-782.073, -460.586, 1015.86))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8117.69, 
    farPlane=15315.7, cameraPosition=(-6281.46, 9111.64, 1019.88), 
    cameraUpVector=(0.164899, -0.289294, -0.94293), cameraTarget=(-782.073, 
    -460.586, 1015.86))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7924.73, 
    farPlane=15508.6, width=6027.63, height=5378.83, cameraPosition=(-6147.1, 
    9188.77, 1160.9), cameraTarget=(-647.711, -383.452, 1156.88))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-6471.08, 
    9002.92, 492.409), cameraTarget=(-971.688, -569.301, 488.388))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7896.36, 
    farPlane=15537, width=5790.12, height=5166.88, cameraPosition=(-6475.09, 
    9000.62, 472.712), cameraTarget=(-975.702, -571.599, 468.691))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7905.45, 
    farPlane=15527.9, cameraPosition=(-6361.62, 9065.8, 511.896), 
    cameraTarget=(-862.229, -506.423, 507.875))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7940.89, 
    farPlane=15492.5, width=5618.15, height=5013.42, cameraPosition=(-6358.23, 
    9067.75, 506.762), cameraTarget=(-858.839, -504.473, 502.741))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7917.46, 
    farPlane=16832.6, cameraPosition=(4578.84, -11252.2, 5389.2), 
    cameraUpVector=(0.263497, 0.789337, 0.554542), cameraTarget=(-80.4073, 
    -2135, 1261.42))
session.viewports['Viewport: 2'].view.setValues(nearPlane=9069.88, 
    farPlane=15766.7, cameraPosition=(-981.671, -13309.3, 2276.86), 
    cameraUpVector=(0.527045, 0.413124, 0.742666), cameraTarget=(-680.498, 
    -2357.01, 925.537))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7625.9, 
    farPlane=16994.9, cameraPosition=(-5221.26, -8739.67, -7797.75), 
    cameraUpVector=(0.622158, -0.499143, 0.603139), cameraTarget=(-1151.21, 
    -1849.65, -193.03))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7833.03, 
    farPlane=16865, cameraPosition=(-8500.04, 1581.2, -8454.09), 
    cameraUpVector=(0.397564, -0.904854, -0.152259), cameraTarget=(-1489.72, 
    -784.112, -260.791))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8020.34, 
    farPlane=16680.9, cameraPosition=(-5516.18, 9607.26, -3162.72), 
    cameraUpVector=(-0.0420809, -0.672943, -0.738497), cameraTarget=(-1173.29, 
    67.0334, 300.347))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7659.69, 
    farPlane=17080.1, cameraPosition=(-8783.6, 3984.91, -7098.04), 
    cameraUpVector=(0.358475, -0.846601, -0.393397), cameraTarget=(-1520.16, 
    -529.84, -117.43))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7989.41, 
    farPlane=16552.4, cameraPosition=(-5305.76, -3193, -10536.7), 
    cameraUpVector=(0.99779, 0.0385766, -0.0540949), cameraTarget=(-1146.1, 
    -1301.86, -487.274))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7593.96, 
    farPlane=17030.8, cameraPosition=(-7711.88, 3930.42, -8080.87), 
    cameraUpVector=(0.783864, -0.453426, -0.424219), cameraTarget=(-1387.57, 
    -586.975, -240.814))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7786.63, 
    farPlane=16820.7, cameraPosition=(-7323.55, 1775.94, -9279.34), 
    cameraUpVector=(0.856707, -0.429233, -0.286028), cameraTarget=(-1347.42, 
    -809.716, -364.718))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7829.09, 
    farPlane=16916.4, cameraPosition=(-9552.07, 1996.69, -7264.74), 
    cameraUpVector=(0.793872, -0.337972, -0.505511), cameraTarget=(-1576.4, 
    -787.034, -157.721))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7674.71, 
    farPlane=17052.6, cameraPosition=(-9254.38, 3993.02, -6526.99), 
    cameraUpVector=(0.678104, -0.46493, -0.569223), cameraTarget=(-1544.32, 
    -571.915, -78.2225))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7749.93, 
    farPlane=17027.4, cameraPosition=(-9846.87, 4551.2, -5267.87), 
    cameraUpVector=(0.617134, -0.421359, -0.664531), cameraTarget=(-1607.78, 
    -512.133, 56.6299))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7844.66, 
    farPlane=16972.3, cameraPosition=(-10302.8, 4581.55, -4461.57), 
    cameraUpVector=(0.600661, -0.352197, -0.717749), cameraTarget=(-1657.44, 
    -508.827, 144.439))
session.viewports['Viewport: 2'].view.setValues(cameraPosition=(-10223.1, 
    4589.81, -4601.99), cameraTarget=(-1577.76, -500.565, 4.02161))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7788.22, 
    farPlane=17028.6, width=6436.51, height=5743.69, cameraPosition=(-10214, 
    4572.03, -4638.77), cameraTarget=(-1568.64, -518.349, -32.7561))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7728.24, 
    cameraPosition=(-10227.9, 4500.37, -4691.85), cameraTarget=(-1582.55, 
    -590.002, -85.834))
session.viewports['Viewport: 2'].view.setValues(width=6050.31, height=5399.07, 
    cameraPosition=(-10238.5, 4507.9, -4663.63), cameraTarget=(-1593.15, 
    -582.475, -57.6135))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7788.23, 
    farPlane=17028.6, cameraPosition=(-10247.9, 4446.75, -4713.51), 
    cameraTarget=(-1602.58, -643.627, -107.498))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=0)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d16w5/images/d16w5 t0.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.printOptions.setValues(vpDecorations=OFF)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d16w5/images/d16w5 t0.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=28)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=28)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d16w5/images/d16w5 t4.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=12)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=26)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=12)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d16w5/images/d16w5 t3.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=8)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=8)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d16w5/images/d16w5 t2.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=4)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=4)
session.viewports['Viewport: 1'].makeCurrent()
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d16w5/images/d16w5 t1.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d16w5\d16w5.cae".
