import time
import sys
import os
import pyaudio #used to play audio
import wave #used to play audio


def alarm(alarm_value):
	init = time.ctime()
	time_in_hr = alarm_value
	minn = time_in_hr*60
	print('\nAlarm set for {} min from now'.format(minn))
	time_in_sec = time_in_hr * 60.0 * 60.0
	newtime = init + str(time_in_sec)
	time.sleep(time_in_sec)
	if time.ctime() >= newtime:
		for i in range(10):
			play_audio('./barium.wav')



def error():
	print("want to enter again?(y/n)")
	will = input('>')
	will = will.lower()
	if will == 'y':
		start()
	else:
		sys.exit()


def start():
	os.system('clear')
	print("\n\n\n\t\t\t\t\tWelcome\n\n\n\n\n\n\n\n\n")
	print('''
					1. Enter time in hours
					2. Enter the clock hour(HHMM)
					3. Enter time in minute
					 
	Enter your choice
		''')
	try:
		choice = int(input('>'))
		if choice >= 4  and choice <= 0:
			print("Wrong choice")
			error()

		else:
			if choice==1:
			
				print('\nEnter time in hours')
				time_hr = float(input('>'))
				alarm(time_hr)
				
			elif choice == 2:
				print('Enter the clock hour(HHMM)')
				global time
				curr_time = time.localtime(time.time())
				curr_hr = curr_time.tm_hour
				curr_min = curr_time.tm_min
				curr_time_sec = curr_hr*60*60 + curr_min*60
				alarm_time = input('>')
				alarm_hr = float(alarm_time[:2])
				alarm_min = float(alarm_time[-2:])
				alarm_time_sec = alarm_hr*60*60 + alarm_min*60
				final = (alarm_time_sec - curr_time_sec)/(60*60)
				alarm(final)


			
			elif choice == 3:
			
				print('\nEnter time in minute')
				time3 = float(input('>'))
				time3 /= 60
				alarm(time3)	
			else:
				print('something terribly went wrong')
				error()


	except:
		error()

def play_audio(filename):
	chunk = 1024
	wf = wave.open(filename, 'rb')
	pa = pyaudio.PyAudio()

	stream = pa.open(
		format = pa.get_format_from_width(wf.getsampwidth()),
		channels = wf.getnchannels(),
		rate = wf.getframerate(),
		output= True
		)
	data_stream = wf.readframes(chunk)
	while data_stream:
		stream.write(data_stream)
		data_stream= wf.readframes(chunk)

	stream.close()
	pa.terminate()


start()


