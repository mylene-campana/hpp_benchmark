from hpp.corbaserver.lydia import Robot
from hpp.corbaserver import ProblemSolver
from hpp_ros import ScenePublisher

robot = Robot ('lydia')
robot.setJointBounds('base_joint_xyz', [-0.9, 0.9, -0.9, 0.9, -1.1, 1.1])
ps = ProblemSolver (robot)
ps.loadObstacleFromUrdf ("hpp_benchmark", "obstacle", "")

s = ScenePublisher (robot)

q_init = robot.getCurrentConfig ()
q_goal = q_init [::]

q_init [2] = -0.6
q_goal [2] =  0.6

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)
ps.solve ()
