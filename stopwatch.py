"""Stopwatch

"""

from tkinter import *

class Time(object):
	def __init__(self):
		self.min = 0
		self.sec = 0

	def increment(self):		
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

class Application(Frame):
	
	stopwatch = Time()
	start = False
	lst = iter(['Bicycles','Reverse Crunches','Double Leg Kickouts','Russian Twist','Toe Touch Left','Toe Touch Right'])
	
	def createWidgets(self):
		self.start = Button(self, text="START", fg="green", command=self.start, width=10)
		self.start.grid(row=2,column=0)

		self.reset = Button(self, text="RESET", fg="blue",command=self.reset, width=10)
		self.reset.grid(row=3,column=0)

		self.stop = Button(self, text = "STOP", fg = "red", command = self.stop, width=10)
		self.stop.grid(row=4,column=0)

		self.quit = Button(self, text="QUIT", command=self.quit,width=10)
		self.quit.grid(row=5,column=0)

		self.time = Label(self, fg = "black", font=("Helectevia",150))
		self.time["text"] = Application.stopwatch
		self.time.grid(row=1,column=0)

		self.exercise = Label(self, font= ("Helectevia",50), width=25)
		self.exercise["text"] = "Exercise Will Appear Here"
		self.exercise.grid(row=0,column=0)

		

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def start(self):
		Application.start = True
		stopwatch.update_time()

	def reset(self):
		Application.start = False
		Application.stopwatch.min, Application.stopwatch.sec = 0, 0
		self.time.config(text="00:00")
		self.exercise["text"] = "Exercise Will Appear Here"

	def stop(self):
		Application.start = False

	def update_time(self):
		"""
		Updates stopwatch every second, accounting for time program run.
		"""
		if Application.start:
			if Application.stopwatch.sec == 0 or Application.stopwatch.sec == 20 or Application.stopwatch.sec == 40:
				self.update_exercise(Application.lst)
			Application.stopwatch.increment()
			self.time.config(text = Application.stopwatch)
			root.after(1000, self.update_time)
	
	def update_exercise(self,exercise_lst):
		self.exercise.config(text = next(exercise_lst))

x = Time()
root = Tk()

# create the application
stopwatch = Application(master = root)
stopwatch.master.title("Workoutwatch")


# start the program
stopwatch.mainloop()
root.destroy()

# code for updating stopwatch every second
#while start:
#	update()
#	time.sleep(1)




