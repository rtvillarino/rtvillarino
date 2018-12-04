import pyglet
import random

class quest():
	def __init__(self):
		self.index = 0
		self.tanongs = ['a','b','c','d','e','f','g','h','i','j']
		
		self.change = False
		self.tanong = pyglet.text.Label('',font_size=32,x=1180//2, y=590*2//3, 
                            anchor_x = 'center', anchor_y = 'center', multiline=True, align='center',width = 1000)
		self.answers= ['a','b','c','d','e','f','g','h','i','j']
		self.choices = ['y','z']
		self.choiceA = pyglet.text.Label('',font_size=20,x=1180//4, y=218, align = 'center', width = 400, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.choiceB = pyglet.text.Label('',font_size=20,x=1180*3//4, y=218,  align = 'center', width = 400, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.choiceCM = pyglet.text.Label('',font_size=20,x=1180/2, y=120,  align = 'center', width = 400, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.choiceC = pyglet.text.Label('',font_size=20,x=1180//4, y=120,  align = 'center', width = 400, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.choiceD = pyglet.text.Label('',font_size=20,x=1180*3//4, y=120,  align = 'center', width = 400, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.answer = pyglet.text.Label('',font_size=20,x=1180*3//4, y=590//2,  align = 'center', width = 400, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.table = ['a','b','c','d','e','f','g','h','i','j']
		

		#results format for every end of the game..
		self.result1 = pyglet.text.Label(self.table[0],font_size=20,x=295, y=348,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result2 = pyglet.text.Label(self.table[1],font_size=20,x=295, y=278,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result3 = pyglet.text.Label(self.table[2],font_size=20,x=295, y=208,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result4 = pyglet.text.Label(self.table[3],font_size=20,x=295, y=138,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result5 = pyglet.text.Label(self.table[4],font_size=20,x=295, y=68,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result6 = pyglet.text.Label(self.table[5],font_size=20,x=885, y=348,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result7 = pyglet.text.Label(self.table[6],font_size=20,x=885, y=278,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result8 = pyglet.text.Label(self.table[7],font_size=20,x=885, y=208,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result9 = pyglet.text.Label(self.table[8],font_size=20,x=885, y=138,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.result10 = pyglet.text.Label(self.table[9],font_size=20,x=885, y=68,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.legend = pyglet.text.Label('Tamang Sagot <-> Iyong Sagot',font_size=10,x=590, y=20,  align = 'center', width = 590, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
		self.score = pyglet.text.Label('CONGRATS',font_size=50,color = (255,0,0,255), x=1180//2, y=527,  align ='center',
                            anchor_x = 'center', anchor_y = 'center',)
		self.comment = pyglet.text.Label('',font_name = 'Comic Sans MS',font_size=30,color = (255,0,0,255), x=1180//2, y=457,  align ='center',width = 1000, multiline=True,
                            anchor_x = 'center', anchor_y = 'center')
	def update(self,dt):
		if self.change == True:
			if self.index<10:
				self.index = (self.index+1)//1
				if self.index<=9:
					self.tanong.text = str(self.tanongs[int(self.index)])
					self.answer.text = str(self.answers[int(self.index)])
					updated_choices = []
					updated_choices.append(str(self.answers[int(self.index)]))
					if len(self.choices[int(self.index)])==1:
						updated_choices.append(self.choices[int(self.index)][0])
						random.shuffle(updated_choices)
						self.choiceA.text = updated_choices[0]
						self.choiceB.text = updated_choices[1]
					elif len(self.choices[int(self.index)])==2:
						updated_choices.append(self.choices[int(self.index)][0])
						updated_choices.append(self.choices[int(self.index)][1])
						random.shuffle(updated_choices)
						self.choiceA.text = updated_choices[0]
						self.choiceB.text = updated_choices[1]
						self.choiceCM.text = updated_choices[2]
					elif len(self.choices[int(self.index)])==3:
						updated_choices.append(self.choices[int(self.index)][0])
						updated_choices.append(self.choices[int(self.index)][1])
						updated_choices.append(self.choices[int(self.index)][2])
						random.shuffle(updated_choices)
						self.choiceA.text = updated_choices[0]
						self.choiceB.text = updated_choices[1]
						self.choiceC.text = updated_choices[2]
						self.choiceD.text = updated_choices[3]
			self.change = False
	def reset(self):
		self.index = 0

letter_A = pyglet.text.Label('',font_size=65,x=1180//4, y=590//2, 
                            anchor_x = 'center', anchor_y = 'center')
letter_B = pyglet.text.Label('',font_size=65,x=1180*3//4, y=590//2, 
                            anchor_x = 'center', anchor_y = 'center')
letter_C = pyglet.text.Label('',font_size=65,x=1180//4, y=590*2//3, 
                            anchor_x = 'center', anchor_y = 'center')
letter_D = pyglet.text.Label('',font_size=65,x=1180*3//4, y=590*2//3, 
                            anchor_x = 'center', anchor_y = 'center')