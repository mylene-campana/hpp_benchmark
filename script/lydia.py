from hpp.corbaserver.lydia import Robot
from hpp.corbaserver import ProblemSolver
from hpp.gepetto import Viewer, PathPlayer

robot = Robot ('lydia')
robot.setJointBounds('base_joint_xyz', [-0.9, 0.9, -0.9, 0.9, -1.1, 1.1])
ps = ProblemSolver (robot)
r = Viewer (ps)

r.loadObstacleModel ("hpp_benchmark", "obstacle", "obstacle")

q_init = robot.getCurrentConfig ()
q_goal = q_init [::]

q_init [2] = -0.6
q_goal [2] =  0.6

ps.selectPathPlanner ("VisibilityPrmPlanner")
ps.selectPathValidation ("Dichotomy", 0.)

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)

ps.readRoadmap ("/local/mcampana/devel/hpp/src/hpp_benchmark/roadmap/lydia.rdm")
#ps.solve ()

pp = PathPlayer (robot.client, r)

"""
ps.addPathOptimizer ("GradientBased")
ps.optimizePath (0)
ps.numberPaths()
ps.pathLength(ps.numberPaths()-1)
"""
