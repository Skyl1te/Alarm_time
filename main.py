import datetime
import time
import pyglet

#your sound
sound = pyglet.media.load('bad_song.mp3')

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Try again'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Try again'
        elif int(alarm_time[3:5]) > 59:
            return 'Try again'
        elif int(alarm_time[6:8]) > 59:
            return 'Try again'
        else:
            return 'ok'


while True:
    alarm_time = input('Enter the time like:\n HH:MM:SS\n ')
    validate = validate_time(alarm_time)
    if validate != 'ok':
        print(validate)
    else:
        print(f'You set the time: {alarm_time}...')
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print('ok')
                # Your sound
                sound.play()
                time.sleep(999)
                break