import logging

def _create_blip_array(wavelet):
	b = []
	for v in wavelet.blips:
		blip = wavelet.blips.get(v)
		if blip.is_root() == False:
			b.append(blip)
	return b

def OnBlipCreated(event, wavelet):
	blips = _create_blip_array(wavelet)
	if len(blips) < 5:
		return
	blips.sort(key=lambda obj: obj.last_modified_time)
	for blip in blips[0:-4]:
		logging.debug("Deleting blip"+repr(blip))
		wavelet.delete(blip)


