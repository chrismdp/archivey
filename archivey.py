from waveapi import robot
from waveapi import events
from waveapi import appengine_robot_runner

import logging

def Main():
	_robot = robot.Robot('Archivey', 
		image_url='http://archiveyrobot.appspot.com/assets/icon.png',
		profile_url='http://archiveyrobot.appspot.com/')
	_robot.register_handler(events.WaveletBlipCreated, OnBlipCreated, events.Context.ALL)
	appengine_robot_runner.run(_robot)

def OnBlipCreated(event, wavelet):
	b = []
	for v in wavelet.blips:
		b.append(wavelet.blips.get(v))
	if len(b) < 5:
		return
	b.sort(key=lambda obj: obj.last_modified_time)
	for blip in b[0:-4]:
		logging.debug("Deleting blip"+repr(blip))
		wavelet.delete(blip)

if __name__ == '__main__':
  Main()


