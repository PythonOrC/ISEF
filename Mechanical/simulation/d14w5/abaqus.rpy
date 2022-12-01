# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-10.57.30 176069
# Run by ethan on Fri Nov 11 16:03:14 2022
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
openMdb('d14w5.cae')
#: The model database "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['d14w5']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
odb = session.mdbData['Model-1']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
mdb.jobs['d14'].submit(consistencyChecking=OFF)
#: The job input file "d14.inp" has been submitted for analysis.
#: Job d14: Analysis Input File Processor completed successfully.
#: Job d14: Abaqus/Standard completed successfully.
#: Job d14 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.mdbData['Model-1'])
o3 = session.openOdb(
    name='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14.odb')
#: Model: D:/Personal/ISEF/Mechanical/simulation/d14w5/d14.odb
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
    translucency=ON)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.Viewport(name='Viewport: 2', origin=(7.0, -141.388900756836), 
    width=436.916656494141, height=220.833343505859)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].maximize()
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(triad=OFF, 
    title=OFF, state=OFF, annotations=OFF, compass=OFF)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
session.viewports['Viewport: 2'].restore()
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    title=OFF, state=OFF, annotations=OFF, compass=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0.0, -141.388900756836), 
    width=248.20832824707, height=227.500015258789)
session.viewports['Viewport: 2'].setValues(origin=(248.20832824707, 
    -141.388900756836), width=248.20832824707, height=227.500015258789)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6974, 
    farPlane=15953.3, width=4935.65, height=4404.39, viewOffsetX=88.6134, 
    viewOffsetY=-137.884)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6940.81, 
    farPlane=15986.5, width=4912.16, height=4383.43, viewOffsetX=140.759, 
    viewOffsetY=-9.2856)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8486.94, 
    farPlane=15450.6, width=6006.4, height=5359.88, cameraPosition=(-11076.2, 
    -3906.91, 2044.26), cameraUpVector=(0.176949, 0.32681, -0.928377), 
    cameraTarget=(-377.981, -1388.66, 1006.09), viewOffsetX=172.114, 
    viewOffsetY=-11.3541)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7837.02, 
    farPlane=16080.2, width=5546.44, height=4949.43, cameraPosition=(-5700.81, 
    -11013.4, 2987.35), cameraUpVector=(-0.306805, 0.41474, -0.856658), 
    cameraTarget=(142.454, -1853.04, 1033.91), viewOffsetX=158.934, 
    viewOffsetY=-10.4846)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8340.69, 
    farPlane=15576.6, width=2492.46, height=2224.18, viewOffsetX=-3.11205, 
    viewOffsetY=46.1936)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8391.61, 
    farPlane=15514.2, width=2507.68, height=2237.76, cameraPosition=(-5765.1, 
    -11020.3, 2756.25), cameraUpVector=(-0.293727, 0.428403, -0.854515), 
    cameraTarget=(136.76, -1854.47, 1016.42), viewOffsetX=-3.13105, 
    viewOffsetY=46.4757)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=8030.97, 
    farPlane=15874.8, width=4531.95, height=4044.14, cameraPosition=(-6053.83, 
    -10744.2, 3231.63), cameraTarget=(336.323, -819.976, 1347.85))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8311.49, 
    farPlane=15314.7, cameraPosition=(-5617.68, -11184.4, 1322.11), 
    cameraUpVector=(-0.238175, 0.523277, -0.818202), cameraTarget=(336.321, 
    -819.975, 1347.86))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7995.05, 
    farPlane=15631.1, width=6988.6, height=6236.36, cameraPosition=(-5413.74, 
    -11300.7, 965.49), cameraTarget=(540.263, -936.247, 991.24))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7464.19, 
    farPlane=16010.7, cameraPosition=(-5592.05, -10985.9, -1063.28), 
    cameraUpVector=(0.249049, 0.424626, -0.870441), cameraTarget=(542.374, 
    -939.972, 1015.25))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7923.35, 
    farPlane=15702.9, cameraPosition=(-5531.79, -11230.6, 990.283), 
    cameraUpVector=(0.063751, 0.348245, -0.935233), cameraTarget=(541.268, 
    -935.48, 977.555))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7825.87, 
    farPlane=15765.9, cameraPosition=(-5387.1, -11303.7, 504.989), 
    cameraUpVector=(0.182643, 0.322694, -0.928714), cameraTarget=(539.556, 
    -934.615, 983.297))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7927.95, 
    farPlane=15698.8, cameraPosition=(-5463.19, -11270.7, 994.426), 
    cameraUpVector=(0.162868, 0.289273, -0.94329), cameraTarget=(540.569, 
    -935.054, 976.783))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8111.81, 
    farPlane=15514.9, width=5456.34, height=4869.03, cameraPosition=(-5635.49, 
    -11171.3, 604.395), cameraTarget=(368.272, -835.636, 586.752))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-5635.49, 
    -11171.3, 604.396), cameraUpVector=(0.167981, 0.286303, -0.943299))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8216.77, 
    farPlane=15410, height=4869.03, cameraPosition=(-5635.49, -11171.3, 
    604.396), cameraTarget=(368.272, -835.636, 586.752))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8165.92, 
    farPlane=15460.8, cameraPosition=(-5624.23, -11177.9, 542.626), 
    cameraTarget=(379.528, -842.28, 524.982))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8111.79, 
    farPlane=15514.9, width=5456.34, height=4869.03, cameraPosition=(-5786.02, 
    -11084.1, 443.127), cameraTarget=(217.736, -748.468, 425.483))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-5696.34, 
    -11135.9, 585.403), cameraTarget=(307.414, -800.318, 567.759))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-5679.5, 
    -11145.7, 560.718), cameraTarget=(324.259, -810.145, 543.074))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8165.83, 
    farPlane=15460.7, cameraPosition=(-5679.5, -11145.7, 560.718), 
    cameraUpVector=(0.163768, 0.28875, -0.943294))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8111.73, 
    farPlane=15514.8, width=6175.13, height=5510.45, cameraPosition=(-5534.16, 
    -11230.1, 584.921), cameraTarget=(469.598, -894.529, 567.277))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8054.18, 
    farPlane=15572.4, cameraPosition=(-5433.25, -11289, 409.671), 
    cameraTarget=(570.504, -953.443, 392.027))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7726.2, 
    farPlane=16828.1, cameraPosition=(-8579.76, 3661.64, 7412.67), 
    cameraUpVector=(-0.155931, -0.984791, -0.0766361), cameraTarget=(-490.651, 
    -890.802, 1436.67))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8873.28, 
    farPlane=16237, cameraPosition=(-660.395, -13104.9, -2781.81), 
    cameraUpVector=(-0.40746, 0.596741, -0.691286), cameraTarget=(307.673, 
    -2580.98, 409))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8299.85, 
    farPlane=16556.8, cameraPosition=(1400.06, -10605.3, -7341.13), 
    cameraUpVector=(-0.02075, 0.86835, -0.495518), cameraTarget=(556.408, 
    -2279.23, -141.395))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8081.53, 
    farPlane=16667.2, cameraPosition=(2303.95, -8799.28, -8918.65), 
    cameraUpVector=(-0.0398972, 0.946692, -0.319658), cameraTarget=(657.411, 
    -2077.42, -317.672))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8106.73, 
    farPlane=16603.3, cameraPosition=(2087.34, -8111.9, -9455.44), 
    cameraUpVector=(-0.0517711, 0.96609, -0.252963), cameraTarget=(634.044, 
    -2003.27, -375.576))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8106.73, 
    cameraPosition=(2028.86, -7635.69, -9785.18), cameraTarget=(575.566, 
    -1527.06, -705.311))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8064.68, 
    farPlane=16655, cameraPosition=(2444.8, -7374.69, -9881.87), 
    cameraUpVector=(-0.0601057, 0.970688, -0.232705), cameraTarget=(619.852, 
    -1499.27, -715.606))
session.viewports['Viewport: 2'].view.setValues(nearPlane=8194.66, 
    farPlane=16545.7, cameraPosition=(1635.49, -7205.28, -10115.6), 
    cameraUpVector=(-0.042231, 0.977008, -0.208979), cameraTarget=(533.4, 
    -1481.17, -740.575))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7864.9, 
    farPlane=16567.9, cameraPosition=(-9024.02, -7926.43, 4034.49), 
    cameraUpVector=(0.0149062, 0.0479945, -0.998736), cameraTarget=(-613.213, 
    -1558.74, 781.509))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7597.61, 
    farPlane=16728.2, cameraPosition=(-6446.32, -5190.83, 9674.15), 
    cameraUpVector=(-0.491712, -0.132352, -0.86064), cameraTarget=(-364.886, 
    -1295.2, 1324.82))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7716.36, 
    farPlane=16643.8, cameraPosition=(-6686.31, -3960.09, 9982.95), 
    cameraUpVector=(-0.456451, -0.27194, -0.847172), cameraTarget=(-387.052, 
    -1181.53, 1353.34))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7664.37, 
    farPlane=16745.6, cameraPosition=(-8202.66, -4930.07, 8232.75), 
    cameraUpVector=(-0.296513, -0.178485, -0.938202), cameraTarget=(-529.046, 
    -1272.36, 1189.45))
session.viewports['Viewport: 2'].view.setValues(cameraPosition=(-7700, 
    -4986.26, 8751.21), cameraTarget=(-26.3883, -1328.55, 1707.91))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7651.74, 
    farPlane=16547.6, cameraPosition=(-8941.33, -5516.65, 6748.91), 
    cameraUpVector=(-0.128115, -0.0875021, -0.987892), cameraTarget=(-144.925, 
    -1379.2, 1516.71))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7651.74, 
    farPlane=16547.6, cameraPosition=(-9137.2, -5714.43, 6263.22), 
    cameraTarget=(-340.791, -1576.98, 1031.02))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7595.35, 
    farPlane=16604, width=6436.51, height=5743.69, cameraPosition=(-9107.9, 
    -5690.03, 6331.78), cameraTarget=(-311.49, -1552.58, 1099.58))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7535.37, 
    cameraPosition=(-9161.62, -5927.48, 6053.7), cameraTarget=(-365.209, 
    -1790.03, 821.498))
session.viewports['Viewport: 2'].view.setValues(width=6050.31, height=5399.07, 
    cameraPosition=(-9172.62, -5940.45, 6024.95), cameraTarget=(-376.211, 
    -1803, 792.744))
session.viewports['Viewport: 2'].view.setValues(nearPlane=7595.36, 
    farPlane=16604, cameraPosition=(-9129.37, -5843.63, 6174.23), 
    cameraTarget=(-332.955, -1706.18, 942.031))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=0)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=14)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=14)
session.printOptions.setValues(vpDecorations=OFF)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14w5 t4.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=11)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=11)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14w5 t3.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14w5 t3.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=7)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=7)
session.viewports['Viewport: 2'].makeCurrent()
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14w5 t2.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=3)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14w5 t1.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], 
    session.viewports['Viewport: 2']))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=0)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='air pump', frame=0)
session.printToFile(
    fileName='D:/Personal/ISEF/Mechanical/simulation/d14w5/d14w5 t0.png', 
    format=PNG, canvasObjects=(session.viewports['Viewport: 2'], 
    session.viewports['Viewport: 1']))
session.viewports['Viewport: 1'].makeCurrent()
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
mdb.save()
#: The model database has been saved to "D:\Personal\ISEF\Mechanical\simulation\d14w5\d14w5.cae".
