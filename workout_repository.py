class Ab_workout:

	repository = {
	"Monday": ['Bicycles','Reverse Crunches','Double Leg Kickouts','Russian Twist','Toe Touch Left','Toe Touch Right'],
	"Tuesday": ['SL Jack Knife R','SL Jack Knife L','Crunches','Bus Drivers','Dead Bug','Front Plank'],
	"Wednesday": ['R Oblique Tucks', 'L Oblique Tucks', 'Toe Touches', 'V-Ups','Russian Twist','Double Leg Rowing'],
	"Thursday":['X Body Cross L','X Body Cross R','Bicycles','Crunches','SL Drop L','SL Drop R'],
	"Friday":[],
	"Saturday":[],
	"Sunday":[]
	}

	def __init__(self,day):
		self.circuit = Ab_workout.repository[day]

	def __iter__(self):
		past = []
		while True:
			try:
				yield self.circuit[0]
				past.append(self.circuit.pop(0))
			except IndexError:
				self.circuit = past
				past = []




