class Workout:
	def __init__(self):
		self.past = []

	@property
	def first(self):
		return self.circuit[0]

	def __iter__(self):
		while True:
			try:
				yield self.first
				self.past.append(self.circuit.pop(0))
			except IndexError:
				self.circuit = self.past
				self.past = []

class Abdominals(Workout):

	ab_circuits = {
	"Ab Circuit 1": ['Bicycles','Reverse Crunches','Double Leg Kickouts','Russian Twist','Toe Touch Left','Toe Touch Right'],
	"Ab Circuit 2": ['SL Jack Knife R','SL Jack Knife L','Crunches','Bus Drivers','Dead Bug','Front Plank'],
	"Ab Circuit 3": ['R Oblique Tucks', 'L Oblique Tucks', 'Toe Touches', 'V-Ups','Russian Twist','Double Leg Rowing'],
	"Ab Circuit 4":['X Body Cross L','X Body Cross R','Bicycles','Crunches','SL Drop L','SL Drop R'],
	"Ab Circuit 5":['Oblique Lift L','Oblique Lift R','Bus Drivers','Toe Touches','V-Ups','Russian Twist'],
	"Ab Circuit 6":['Scissor Kicks','Double Leg Kickouts','Side Crunch L','Side Crunch R','Reverse Crunch','Double Leg Rowing'],
	}

	def __init__(self,number,interval=20):
		Workout.__init__(self)
		self.circuit = Abdominals.ab_circuits[number]
		self.interval = 20

class Jumprope(Workout):

	jumprope_circuits = {
	"Jumprope Circuit 1": ['Up & Back','Side to Side','2 Right, 2 Left','X Jumps','Jabs','High Knees']
	}

	def __init__(self,number,interval=30):
		Workout.__init__(self)
		self.circuit = Jumprope.jumprope_circuits[number]
		self.interval = interval





