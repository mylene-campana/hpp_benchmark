#!/usr/bin/env python
# Copyright (c) 2014 CNRS
# Author: Florent Lamiraux
#
# This file is part of hpp_benchmark.
# hpp_benchmark is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp_benchmark is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp_benchmark.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.robot import Robot as Parent

##
#  Control of device Lydia in hpp
#
#  This class implements a client to the corba server implemented in
#  hpp_benchmark. It derive from class hpp.corbaserver.robot.Robot.
#
#  This class is also used to initialize a client to rviz in order to
#  display configurations of the PR2 robot.
#
#  At creation of an instance, the urdf and srdf files are loaded using
#  idl interface hpp::corbaserver::Robot::loadRobotModel.
class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    packageName = "hpp_benchmark"
    ##
    #  Information to retrieve urdf and srdf files.
    urdfName = "lydia"
    urdfSuffix = ""
    srdfSuffix = ""

    def __init__ (self, robotName, load = True):
        Parent.__init__ (self, robotName, "freeflyer", load)
        self.tf_root = "base_link"
