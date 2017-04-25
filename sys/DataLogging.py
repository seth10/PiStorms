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

import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from mindsensorsUI import mindsensorsUI
import threading, time

class DataGraph():
    def __init__(self, title, xAxisLabel, yAxisLabel, grid, dataSource):
        self.screen = mindsensorsUI()
        self.data = np.empty()
        self.stop = False
        self.image = tempfile.NamedTemporaryFile()

        plt.figure(figsize=(4,3), dpi=80)
        plt.title(title)
        plt.xlabel(xAxisLabel)
        plt.ylabel(yAxisLabel)
        plt.grid(grid)
        
        self.lock = threading.Lock()

        threading.Thread(target=self.drawToScreen).start()

        self.dataSource = dataSource
        threading.Thread(target=self.captureData).start()

    def drawToScreen(self):
        while not self.stop:
            with self.lock:
                plt.plot(self.data, color="blue")
                plt.tight_layout()
                plt.savefig(self.image.name, format="png")
                self.screen.fillBmp(0,0, 320,240, self.image.name)
            time.sleep(0.01)

    def captureData(self):
        while not self.stop:
            with self.lock:
                self.data = np.append(self.data, self.dataSource())
            time.sleep(0.01)
