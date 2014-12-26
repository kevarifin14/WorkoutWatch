class Timer:
	def __init__(self):
		"""
		Initializes the time
		"""
		self.min = 0
		self.sec = 0

	def increment(self):
		"""
		Increments time and checks if minute should be incremented.
		Capped at one hour before it restarts.
		"""
		self.sec += 1
		if self.sec == 60:
			self.min += 1
			self.sec = 0
		if self.min == 60:
			self.min == 0
		
	def __str__(self):
		if self.min < 10 and self.sec < 10:
			return "0{0}:0{1}".format(self.min,self.sec)
		if self.sec < 10:
			return "{0}:0{1}".format(self.min,self.sec)
		if self.min < 10:
			return "0{0}:{1}".format(self.min,self.sec)

	def __repr__(self):
		if self.min < 10 and self.sec < 10:
			return "0{0}:0{1}".format(self.min,self.sec)
		if self.sec < 10:
			return "{0}:0{1}".format(self.min,self.sec)
		if self.min < 10:
			return "0{0}:{1}".format(self.min,self.sec)