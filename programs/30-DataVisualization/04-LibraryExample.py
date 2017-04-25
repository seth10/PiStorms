#!/usr/bin/env python
#
# Copyright (c) 2017 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author          Comments
# 04/25/17  Seth Tenembaum  Initial development.
#

from DataLogging import DataGraph
from PiStorms import PiStorms
from mindsensors import ABSIMU

psm = PiStorms()
imu = ABSIMU()
psm.BAS1.activateCustomSensorI2C() # see example in 50-SensorDemos

graph = DataGraph('Title', 'X axis', 'Y axis', grid=True, dataSource=imu.get_tiltx)

while not psm.isKeyPressed(): pass
graph.stop = True
