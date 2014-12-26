"""Workoutwatch

A stopwatch that doubles as a workout guide. 
	
"""

from tkinter import *
from workout_repository import *
from timer import Timer

class Application(Frame):
	
	stopwatch = Timer()
	start = False
	
	def createWidgets(self):
		self.start = Button(self, text="START", fg="green", command=self.start, width=10)
		self.start.grid(row=2,column=2)

		self.reset = Button(self, text="RESET", fg="blue",command=self.reset, width=10)
		self.reset.grid(row=3,column=2)

		self.stop = Button(self, text = "STOP", fg = "red", command = self.stop, width=10)
		self.stop.grid(row=4,column=2)

		self.quit = Button(self, text="QUIT", command=self.quit,width=10)
		self.quit.grid(row=5,column=2)

		self.time = Label(self, fg = "black", font=("Helectevia",150))
		self.time["text"] = Application.stopwatch
		self.time.grid(row=1,column=2)

		self.exercise = Label(self, font= ("Helectevia",50), width=25)
		self.exercise["text"] = "Select Workout"
		self.exercise.grid(row=0,column=2)

		self.ab_circuit_label = Label(self, text="Abs",width=10,font="Helectevia")
		self.ab_circuit_label.grid(row=2,column=0)

		self.ab_circuit_1 = Button(self, text="Ab Circuit 1",command=self.create_ab_workout("Ab Circuit 1"),width=10)
		self.ab_circuit_1.grid(row=3,column=0)

		self.ab_circuit_2 = Button(self, text="Ab Circuit 2",command=self.create_ab_workout("Ab Circuit 2"),width=10)
		self.ab_circuit_2.grid(row=4,column=0)

		self.ab_circuit_3 = Button(self, text="Ab Circuit 3",command=self.create_ab_workout("Ab Circuit 3"),width=10)
		self.ab_circuit_3.grid(row=5,column=0)

		self.ab_circuit_4 = Button(self, text="Ab Circuit 4",command=self.create_ab_workout("Ab Circuit 4"),width=10)
		self.ab_circuit_4.grid(row=6,column=0)

		self.ab_circuit_5 = Button(self, text="Ab Circuit 5",command=self.create_ab_workout("Ab Circuit 5"),width=10)
		self.ab_circuit_5.grid(row=7,column=0)

		self.ab_circuit_6 = Button(self, text="Ab Circuit 6",command=self.create_ab_workout("Ab Circuit 6"),width=10)
		self.ab_circuit_6.grid(row=8,column=0)

		self.jumprope_circuit_label = Label(self,text="Jumprope",width=10,font="Helectevia")
		self.jumprope_circuit_label.grid(row=2,column=1)

		self.jumprope_circuit_1 = Button(self, text="Jumprope 1",command=self.create_jumprope_workout("Jumprope Circuit 1"),width=10)
		self.jumprope_circuit_1.grid(row=3,column=1)
		

	def __init__(self, master=None,circuit="Ab Circuit 1"):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
		self.workout = Abdominals(circuit)
		self.iter_workout = iter(self.workout)
		self.circuit = circuit

	def start(self):
		"""
		Starts the stopwatch by changing the start value to true and beginning update.
		"""
		Application.start = True
		stopwatch.update_time()
		self.start.config(state="disabled")

	def reset(self):
		"""
		Resets stopwatch and also returns to the beginning of the circuit.
		"""
		Application.start = False
		Application.stopwatch.min, Application.stopwatch.sec = 0, 0
		self.time.config(text="00:00")
		self.exercise["text"] = "Select Workout"
		self.start.config(state="active")
		if type(self.workout) is Abdominals:
			self.workout = Abdominals(self.circuit)
		if type(self.workout) is Jumprope:
			self.workout = Jumprope(self.circuit)
		self.iter_workout = iter(self.workout)

	def stop(self):
		"""
		Stops the time by changing start value to false. 
		"""
		Application.start = False
		self.start.config(state="active")

	def update_time(self):
		"""
		Updates stopwatch every second, also checking multiples of set cycle to swtich workout.
		Uses root.after to pause the operation of update_time. 
		"""
		if Application.start:
			if Application.stopwatch.sec % self.workout.interval == 0:
				self.update_exercise(self.iter_workout)
			Application.stopwatch.increment()
			self.time.config(text = Application.stopwatch)
			root.after(1000, self.update_time)
	
	def update_exercise(self,exercise_lst):
		"""
		Changes display to the following exercise.
		"""
		self.exercise.config(text = next(self.iter_workout))

	def create_ab_workout(self,circuit):
		"""
		Creates ab workout.
		"""
		def helper():
			self.circuit = circuit
			self.workout = Abdominals(self.circuit)
			self.iter_workout = iter(self.workout)
			Application.reset(self)
		return helper

	def create_jumprope_workout(self,circuit):
		"""
		Creates jumprope workout
		"""
		def helper():
			self.circuit = circuit
			self.workout = Jumprope(self.circuit)
			self.iter_workout = iter(self.workout)
			Application.reset(self)
		return helper

root = Tk()

# create the application
stopwatch = Application(master = root)
stopwatch.master.title("Workoutwatch")


# start the program
stopwatch.mainloop()
root.destroy()






