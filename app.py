from waveapi import robot
from waveapi import events
from waveapi import appengine_robot_runner

from archivey import *

import logging

def Main():
	_robot = robot.Robot('Archivey', 
		image_url='http://archiveyrobot.appspot.com/assets/icon.png',
		profile_url='http://bit.ly/dbUZzt')
	_robot.register_handler(events.WaveletBlipCreated, OnBlipCreated, events.Context.ALL)
	appengine_robot_runner.run(_robot)

if __name__ == '__main__':
  Main()


