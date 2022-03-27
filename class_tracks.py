


class step(object):
	def __init__(self, track, gateOn, prob, len, muteOn, rst):
		self.track = track
		self.gateOn = gateOn
		self.prob = prob
		self.len = len
		self.muteOn = muteOn
		self.rst = rst
		
	def track(self):
		return self.track
	
	def gateOn(self):
		return self.gateOn
	
	def prob(self):
		return self.prob
	
	def len(self):
		return self.len
	
	def muteOn(self):
		return self.muteOn
	
	def rst(self):
		return self.rst
	
	
	
	def set_gateOn(self, value):
		self.gateOn = value