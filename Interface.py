import pyglet
import random

#user-defined modules
import Engine
import timer
import QQQ


win = pyglet.window.Window(width = 1180, height = 590, caption = 'PINOY AKO: gaano?')

#images to display
titleA = pyglet.image.load_animation('title.gif')
title = pyglet.sprite.Sprite(titleA)


modep = pyglet.image.load('Mode.jpg')
modep = modep.get_texture()
modep.width = win.width
modep.height = win.height
preG = pyglet.image.load('pregame.jpg')
preG = preG.get_texture()
preG.width = win.width
preG.height = win.height
back = pyglet.image.load('back.jpg')
back = back.get_texture()
back.width = win.width
back.height = win.height
back2 = pyglet.image.load('back2.jpg')
back2 = back2.get_texture()
back2.width = win.width
back2.height = win.height

def intro():
	@win.event
	def on_draw():
		win.clear()
		title.draw()
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 690<=x<=1052 and 107<=y<=195:
			mode()
		elif 753<=x<=982 and 29<=y<=83:
			win.close()


def mode():
	@win.event
	def on_draw():
		win.clear()
		modep.blit(0,0)
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 325<=x<=797 and 376<=y<=458:
			pregame(Easy)
		elif 325<=x<=797 and 219<=y<=314:
			pregame(Medium)
		elif 325<=x<=797 and 70<=y<=163:
			pregame(Difficult)

def pregame(ans):
	@win.event
	def on_draw():
		win.clear()
		preG.blit(0,0)
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 525<=x<=596 and 198<=y<=255:
			countdown.running = True
			@win.event
			def on_draw():
				win.clear()
				countdown.display.draw()
				if countdown.display.text=='SIMULAN!':
					ans()
	
def Easy():
	list_q = Engine.Q_Easy()
	answ = Engine.A_Easy(list_q )
	choi = Engine.choiceEasy(list_q)
	qqq.choices = list(choi)
	qqq.tanongs = list(list_q)
	qqq.tanong.text = list_q[0]
	qqq.answers = list(answ)
	choicess = []
	choicess.append(answ[0])
	choicess.append(choi[0][0])
	random.shuffle(choicess)
	qqq.choiceA.text = choicess[0]
	qqq.choiceB.text = choicess[1]
	qqq.answer.text = answ[0]
	game_time.running=True
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 180<=x<=400 and 180<=y<=250:
			Engine.record(qqq.answer.text,qqq.choiceA.text)
			qqq.change = True
		elif 760<=x<=970 and 175<=y<=260:
			Engine.record(qqq.answer.text,qqq.choiceB.text)
			qqq.change = True
	@win.event
	def on_draw():
		win.clear()
		back.blit(0,0)
		game_time.display.draw()
		qqq.tanong.draw()
		qqq.choiceA.draw()
		qqq.choiceB.draw()
		if game_time.display.text == 'TIGIL!' or qqq.index == 10:
			stopna()

def Medium():
	list_q = Engine.Q_Medium()
	answ = Engine.A_Medium(list_q )
	choi = Engine.choiceMedium(list_q)
	qqq.tanongs = list(list_q)
	qqq.answers = list(answ)
	qqq.choices = list(choi)
	qqq.tanong.text = list_q[0]
	qqq.answer.text = answ[0]
	choicess = []
	choicess.append(answ[0])
	choicess.append(choi[0][0])
	choicess.append(choi[0][1])
	random.shuffle(choicess)
	qqq.choiceA.text = choicess[0]
	qqq.choiceB.text = choicess[1]
	qqq.choiceCM.text = choicess[2]
	game_time.running=True
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 180<=x<=400 and 180<=y<=250:
			Engine.record(qqq.answer.text,qqq.choiceA.text)
			qqq.change = True
		elif 760<=x<=970 and 175<=y<=260:
			Engine.record(qqq.answer.text,qqq.choiceB.text)
			qqq.change = True
		elif 502<=x<=680 and 96<=y<=143:
			Engine.record(qqq.answer.text,qqq.choiceCM.text)
			qqq.change = True
	@win.event
	def on_draw():
		win.clear()
		back.blit(0,0)
		game_time.display.draw()
		qqq.tanong.draw()
		qqq.choiceA.draw()
		qqq.choiceB.draw()
		qqq.choiceCM.draw()
		if game_time.display.text == 'TIGIL!' or qqq.index == 10:
			stopna()

def Difficult():
	list_q = Engine.Q_Diff()
	answ = Engine.A_Diff(list_q )
	choi = Engine.choiceDiff(list_q)
	qqq.tanongs = list(list_q)
	qqq.answers = list(answ)
	qqq.choices = list(choi)
	qqq.tanong.text = list_q[0]
	qqq.answer.text = answ[0]
	choicess = []
	choicess.append(answ[0])
	choicess.append(choi[0][0])
	choicess.append(choi[0][1])
	choicess.append(choi[0][2])
	random.shuffle(choicess)
	qqq.choiceA.text = choicess[0]
	qqq.choiceB.text = choicess[1]
	qqq.choiceC.text = choicess[2]
	qqq.choiceD.text = choicess[3]
	game_time.running=True
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 180<=x<=400 and 180<=y<=250:
			Engine.record(qqq.answer.text,qqq.choiceA.text)
			qqq.change = True
		elif 760<=x<=970 and 175<=y<=260:
			Engine.record(qqq.answer.text,qqq.choiceB.text)
			qqq.change = True
		elif 183<=x<=409 and 95<=y<=141:
			Engine.record(qqq.answer.text,qqq.choiceC.text)
			qqq.change = True
		elif 770<=x<=995 and 95<=y<=141:
			Engine.record(qqq.answer.text,qqq.choiceD.text)
			qqq.change = True
	@win.event
	def on_draw():
		win.clear()
		back.blit(0,0)
		game_time.display.draw()
		qqq.tanong.draw()
		qqq.choiceA.draw()
		qqq.choiceB.draw()
		qqq.choiceC.draw()
		qqq.choiceD.draw()
		if game_time.display.text == 'TIGIL!' or qqq.index == 10:
			stopna()


def stopna():
	table = Engine.tableResults()
	scoresss = Engine.scoreResults()
	comment = Engine.rate(scoresss)
	while len(table) < 10:
		table.append(' ')
	qqq.result1.text = table[0]
	qqq.result2.text = table[1]
	qqq.result3.text = table[2]
	qqq.result4.text = table[3]
	qqq.result5.text = table[4]
	qqq.result6.text = table[5]
	qqq.result7.text = table[6]
	qqq.result8.text = table[7]
	qqq.result9.text = table[8]
	qqq.result10.text = table[9]
	qqq.score.text = str(scoresss)+'/10'
	qqq.comment.text = comment
	@win.event
	def on_draw():
		win.clear()
		back2.blit(0,0)
		qqq.result1.draw()
		qqq.result2.draw()
		qqq.result3.draw()
		qqq.result4.draw()
		qqq.result5.draw()
		qqq.result6.draw()
		qqq.result7.draw()
		qqq.result8.draw()
		qqq.result9.draw()
		qqq.result10.draw()
		qqq.legend.draw()
		qqq.score.draw()
		qqq.comment.draw()
	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if 971<=x<=1165 and 531<=y<=579:
			game_time.reset()
			countdown.reset()
			qqq.reset()
			open("Records.txt", "w").close()
			open("Score.txt", "w").close()
			intro()
		elif 1027<=x<=1111 and 501<=y<=525:
			win.close()


intro()
qqq = QQQ.quest()
countdown = timer.cd()
game_time = timer.game_timer()
pyglet.clock.schedule_interval(countdown.update, 1)
pyglet.clock.schedule_interval(game_time.update, 1)
pyglet.clock.schedule_interval(qqq.update, 1)
pyglet.app.run()