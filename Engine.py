Easy = open('Easy.txt', 'r')
Medium = open('Medium.txt', 'r')
Diff = open('Difficult.txt', 'r')
EasyA = open('Easy A.txt', 'r')
MediumA = open('Medium A.txt', 'r')
DiffA = open('Difficult A.txt', 'r')
EasyC = open('Choices Easy.txt', 'r')
MediumC = open('Choices Medium.txt','r')
DiffC = open('Choices Diff.txt','r')

records = open('Records.txt','w')
records.close() #file where the player's answers are located

score = open('Score.txt','w')
score.close()

Q_1 = Easy.read()
Q_2 = Medium.read()
Q_3 = Diff.read()
A_1 = EasyA.read()
A_2 = MediumA.read()
A_3 = DiffA.read()
C_1 = EasyC.read()
C_2 = MediumC.read()
C_3 = DiffC.read()

Q1 = [str(q) for q in Q_1.split('\n')] #List of Easy Questions
Q2 = [str(q) for q in Q_2.split('\n')] #List of Medium Questions
Q3 = [str(q) for q in Q_3.split('\n')] #List of Difficult Questions
A1 = [str(a) for a in A_1.split('\n')] #List of Easy Answers
A2 = [str(a) for a in A_2.split('\n')] #List of Medium Answers
A3 = [str(a) for a in A_3.split('\n')] #List of Difficult Answers
C1 = [str(c) for c in C_1.split('\n')] #List of Easy Choices
C2 = [str(c) for c in C_2.split('\n')] #List of Medium Choices
C3 = [str(c) for c in C_3.split('\n')] #List of Difficult Choices

import random

def Q_Easy():
	questions = random.sample(Q1, 10)
	return questions

def Q_Medium():
	questions = random.sample(Q2, 10)
	return questions

def Q_Diff():
	questions = random.sample(Q3, 10)
	return questions

def A_Easy(questions):
	answers = []
	for q in questions:
		qIndex = Q1.index(q)
		answers.append(A1[qIndex])
	return answers

def A_Medium(questions):
	answers = []
	for q in questions:
		qIndex = Q2.index(q)
		answers.append(A2[qIndex])
	return answers

def A_Diff(questions):
	answers = []
	for q in questions:
		qIndex = Q3.index(q)
		answers.append(A3[qIndex])
	return answers

def rate(noOfCorrects):
	if noOfCorrects<=3:
		rate = 'Ikaw ay Dayuhan sa iyong sariling bayan'
	elif 4<=noOfCorrects<=5:
		rate = 'Nanganganib ang iyong Pagka-Pilipino'
	elif 6<=noOfCorrects<=7:
		rate = 'Ordinaryong Mamamayan ng Pilipinas'
	elif 8<=noOfCorrects<=9:
		rate = 'Ayos! Isang Pilipino may alam'
	elif noOfCorrects==10:
		rate = 'Binabati Kita! Isa kang tunay na Pilipino!'
	return rate

def record(correctAnswer,PlayersAnswer):
	records = open('Records.txt','a')
	rec = str(correctAnswer)+' <-> '+str(PlayersAnswer)+'\n'
	records.write(rec)
	records.close()
	score = open('Score.txt','a')
	if correctAnswer == PlayersAnswer:
		score.write('1'+'\n')
	else:
		score.write('0'+'\n')
	score.close()

def choiceEasy(questions):
	choices = []
	for q in questions:
		qIndex = Q1.index(q)
		ch = [str(x) for x in C1[qIndex].split(',')]
		choices.append(ch)
	return choices

def choiceMedium(questions):
	choices = []
	for q in questions:
		qIndex = Q2.index(q)
		ch = [str(x) for x in C2[qIndex].split(',')]
		choices.append(ch)
	return choices

def choiceDiff(questions):
	choices = []
	for q in questions:
		qIndex = Q3.index(q)
		ch = [str(x) for x in C3[qIndex].split(',')]
		choices.append(ch)
	return choices

def tableResults():
	recorded = open('Records.txt','r')
	record_r = recorded.read()
	tables = [ str(r) for r in record_r.split('\n')]
	recorded.close()
	return tables
	
def scoreResults():
	scored = open('Score.txt','r')
	scored_r = scored.read()
	scores = [ int(r) for r in scored_r.split('\n') if r != '']
	total = 0
	for s in scores:
		total += s
	scored.close()
	return total