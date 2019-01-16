#check while loops on 192 , 200 and 205
import wiringpi2 as wiringpi

RS = 11
EN = 10
D4 = 6
D5 = 5
D6 = 4
D7 = 1

led1 = 26
led2 = 27
led3 = 28
led4 = 29
led5 = 14
buzz = 13

in1 = 21
in2 = 22 
in3 = 23
in4 = 24
in5 = 25 
 
vote1 = 0
vote2 = 0
vote3 = 0
vote4 = 0

vote=[] #size=5

#for pre declaration of funcs..
def compare():
	comp_are()

def show():
	sh_ow()

def lcdcmd(ch):
	temp = 0x80
	digitalWrite(D4, temp & ch<<3)
	digitalWrite(D5, temp & ch<<2)
	digitalWrite(D6, temp & ch<<1)
	digitalWrite(D7, temp & ch)
	digitalWrite(RS, LOW)
	digitalWrite(EN, HIGH)
	delay(10)
	digitalWrite(EN, LOW)
	digitalWrite(D4, temp & ch<<7)
	digitalWrite(D5, temp & ch<<6)
	digitalWrite(D6, temp & ch<<5)
	digitalWrite(D7, temp & ch<<4)
	digitalWrite(RS, LOW)
	digitalWrite(EN, HIGH)
	delay(10)
	digitalWrite(EN, LOW)

def write(ch):
	temp=0x80
	digitalWrite(D4, temp & ch<<3)
	digitalWrite(D5, temp & ch<<2)
	digitalWrite(D6, temp & ch<<1)
	digitalWrite(D7, temp & ch)
	digitalWrite(RS, HIGH)
	digitalWrite(EN, HIGH)
	delay(10)
	digitalWrite(EN, LOW)
	digitalWrite(D4, temp & ch<<7)
	digitalWrite(D5, temp & ch<<6)
	digitalWrite(D6, temp & ch<<5)
	digitalWrite(D7, temp & ch<<4)
	digitalWrite(RS, HIGH)
	digitalWrite(EN, HIGH)
	delay(10)
	digitalWrite(EN, LOW)

def clear():
	lcdcmd(0x01)

def setCursor(x,y):
	sset=0
	if(y==0):
		sset=128+x
	if(y==1):
		sset=192+x
	lcdcmd(sset)

def print(s):
	for cc in s:
		write(c)

def begin(x,y):
	lcdcmd(0x02)
	lcdcmd(0x28)
	lcdcmd(0x06)
	lcdcmd(0x0e)
	lcdcmd(0x01)

def setup():
	if(wiringPiSetup()==-1):
		print("ERROR")
	pinMode(led1, OUTPUT)
	pinMode(led2, OUTPUT)
	pinMode(led3, OUTPUT)
	pinMode(led4, OUTPUT)
	pinMode(led5, OUTPUT)
	pinMode(buzz, OUTPUT)
	pinMode(RS, OUTPUT)
	pinMode(EN, OUTPUT)
	pinMode(D4, OUTPUT)
	pinMode(D5, OUTPUT)
	pinMode(D6, OUTPUT)
	pinMode(D7, OUTPUT)
	pinMode(in1, INPUT)
	pinMode(in2, INPUT)
	pinMode(in3, INPUT)
	pinMode(in4, INPUT)
	pinMode(in5, INPUT)
	digitalWrite(in1, HIGH)
	digitalWrite(in2, HIGH)
	digitalWrite(in3, HIGH)
	digitalWrite(in4, HIGH)
	digitalWrite(in5, HIGH)
	begin(16,2)

def buzzer():
	digitalWrite(buzz, HIGH)
	delay(1000)
	digitalWrite(buzz, LOW)

def out():
	time=20
	while(time):
		setCursor(0,0)
		print(time)
		time-=1
		delay(1000)
	buzzer()

def resumeit():
	setCursor(0,0)
	print("BJP Cong AAP Ex")
	setCursor(1,1)
	print("1")
	setCursor(6,1)
	print("2")
	setCursor(10,1)
	print("3")
	setCursor(14,1)
	print("4")
	delay(2000)

def wait():
	digitalWrite(led5, LOW)
	delay(3000)

if __name__ == '__main__':
	setup()
	print("Electronic Voting")
	setCursor(0,1)
	print("Machine")
	delay(2000)
	clear()
	show()

	while(1):
		digitalWrite(led5, HIGH)
		digitalWrite(in3, HIGH)

		if(digitalRead(in1)==0):
			vote1+=1
			show()
			digitalWrite(led1, HIGH)
			buzzer()
			digitalWrite(led1, LOW)
			wait()  

		elif(digitalRead(in2)==0):
			vote2+=1 
			show()
			digitalWrite(led2, HIGH)
			buzzer()
			digitalWrite(led2, LOW)
			out()  
			#while(digitalRead(in2)==0)

		elif(digitalRead(in3)==0):
			vote3+=1   
			show()    
			digitalWrite(led3, HIGH)
			buzzer()
			digitalWrite(led3, LOW)
			out()       
			#while(digitalRead(in3)==0)

		elif(digitalRead(in4)==0):
			vote4+=1  
			show()
			digitalWrite(led4, HIGH)
			buzzer()
			digitalWrite(led4, LOW)
			out()            
			#while(digitalRead(in4)==0)

		elif(digitalRead(in5)==0):
			compare()
			#while(digitalRead(in5)==0) 

def show():
	setCursor(0,0)
	print("BJP Cong AAP Ex")
	setCursor(1,1)
	print("1")
	setCursor(6,1)
	print("2")
	setCursor(10,1)
	print("3")
	setCursor(14,1)
	print("4")
	delay(100)

def compare():
	clear()
	print("Please Wait....")
	wait()

	if(vote1 > vote2 and vote1>vote3 and vote1>vote4):
		digitalWrite(led1, HIGH)
		for i in range(0,2):
			clear()
			setCursor(0,0)
			print("Congrates.......")
			setCursor(0,1)
			print("BJP Won election")
			delay(2000)
			clear()
			resumeit()
		digitalWrite(led1, LOW)

	elif(vote2 >vote1 and vote2>vote3 and vote2>vote4):
		digitalWrite(led2, HIGH)
		for i in range(0,2):
			clear()
			setCursor(0,0)
			print("Congrates.......")
			setCursor(0,1)
			print("Cong Won election")
			delay(2000)
			clear()
			resumeit()
		digitalWrite(led2, LOW)

	elif(vote3 > vote2 and vote3>vote1 and vote3>vote4):
		digitalWrite(led3, HIGH)
		for i in range(0,2):
			clear()
			setCursor(0,0)
			print("Congrates.......")
			setCursor(0,1)
			print("AAP Won election")
			delay(2000)
			clear()
			resumeit()
		digitalWrite(led3,LOW)

	elif(vote4 > vote2 and vote4>vote3 and vote4>vote1):
		digitalWrite(led4, HIGH)
		for i in range(0,2):
			clear()
			setCursor(0,0)
			print("Congrates.......")
			setCursor(0,1)
			print("Ex Won elections")
			delay(2000)
			clear()
			resumeit()
		digitalWrite(led4, LOW)
	else:
		for i in range(0,2):
			clear()
			setCursor(0,0)
			print("Tie Between Two ")
			setCursor(0,1)
			print("or more Parties ")
			delay(2000)
			clear()
			resumeit()
	vote1=0
	vote2=0
	vote3=0
	vote4=0
	clear()
	show()

