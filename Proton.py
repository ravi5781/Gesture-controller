import pyttsx3 #Converts text to speech.
import speech_recognition as sr #Recognizes and converts speech to text.
from datetime import date #date object can help you fetch today's date or manipulate dates in different formats.
import time #Manages time-related tasks (delays, current time) or manipulate dates in different formats..
import webbrowser  #Opens web pages in a browser.
import datetime #Works with both dates and times.
from pynput.keyboard import Key, Controller #Controls and monitors the keyboard.
import pyautogui #control mouse and keyboard actions.
import sys # Interacts with the system and handles program exit
import os # Manages files and directories on the system
from os import listdir #Lists all files and directories in a given directory.
from os.path import isfile, join #isfile: Checks if a path is a file. #join: Joins paths in a way that works across different operating systems.
import smtplib #sed to send emails using the Simple Mail Transfer Protocol (SMTP).
import wikipedia #Allows you to access Wikipedia articles and get information programmatically.
import Gesture_Controller #controlling gestures from "Gesture-Controlled Virtual Mouse" project.
import app #the main application logic of "Gesture-Controlled Virtual Mouse" project.
from threading import Thread #Enables running tasks in parallel using threads, improving performance and allowing multitasking.
import requests #Makes it easy to send HTTP requests (like GET or POST) to web services or APIs.
import math #Provides mathematical functions(eg:-square roots, trigonometric functions, pi)



# -------------Object Initialization---------------


today = date.today() #for today's date from datetime module
r = sr.Recognizer() #Initializes a recognizer object from the speech_recognition library to recognize audio input (speech).
keyboard = Controller() #Initializes a Controller object from the pynput.keyboard module to control the keyboard
engine = pyttsx3.init('sapi5') #Initializes the pyttsx3 text-to-speech engine, 'sapi5' specifies the speech engine for Windows.
 
engine = pyttsx3.init() #overriding the pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #Retrieves available voice options for the speech engine.
engine.setProperty('voice', voices[1].id)  #Sets the speech engine to use the first voice in the list of available voices.


# ----------------Variables------------------------


file_exp_status = False #it indicates whether a file operation or task is in progress
files =[] #Initializes an empty list to store files
path = '' #Initializes an empty string to store a file or directory path
is_awake = True  #Bot status active or inactive


# ------------------Functions----------------------#


def reply(audio): #text response to be handled
    app.ChatBot.addAppMsg(audio) #Uses the pyttsx3 text-to-speech engine to convert the audio text into speech

    print(audio) #audio response (text) to the console for debugging or logging purposes.
    engine.say(audio) #Uses the pyttsx3 text-to-speech engine to convert the audio text into speech.
    engine.runAndWait() #Ensures the speech is finished before moving to the next task.


#---------------------WISHING-----------------#


def wish():
    hour = int(datetime.datetime.now().hour) #determine the current hour of the day.

    if hour>=0 and hour<12: #morning time upto 1-12
        reply("Good Morning!")
    elif hour>=12 and hour<18: #afternoontime 12-18
        reply("Good Afternoon!")   
    else:
        reply("Good Evening!")  
        
    reply("I am Proton, how may I help you?")


# ------------------Set Microphone parameters----------------#


with sr.Microphone() as source:  #Opens the microphone for speech input.
        r.energy_threshold = 1500  #Sets a fixed sensitivity to filter out background noise.
        r.dynamic_energy_threshold = False #Disables automatic noise sensitivity adjustments."""


with sr.Microphone() as source:
    print("Adjusting for ambient noise, please wait...")
    r.adjust_for_ambient_noise(source, duration=2)  # Automatically sets a baseline
    print(f"Suggested energy threshold: {r.energy_threshold}")


#---------------------Audio to String------------------------#


def record_audio():
    with sr.Microphone() as source:  # to capture audio input.
        r.pause_threshold = 0.8 #Adjusts the pause duration before ending speech capture
        voice_data = '' 
        audio = r.listen(source, phrase_time_limit=5) #Records up to 5 seconds of speech using r.listen.


        try:
            voice_data = r.recognize_google(audio) #Tries to convert speech to text using Google's speech recognition
        except sr.RequestError: #If there's no internet (RequestError), informs the user.
            reply('Sorry my Service is down. Plz check your Internet connection')
        except sr.UnknownValueError: #If speech is unclear (UnknownValueError), skips processing.
            print('cant recognize')
            pass
        return voice_data.lower() #Converts recognized text to lowercase for consistency.


#-----------------calculator---------------#


import math

def calculator(command):
    try:
        # Normalize input
        command = command.lower()
        command = command.replace('proton', '').replace('calculate', '').strip()

        if not command:
            return "Please provide a valid calculation request."

        result = None

        # Handle basic arithmetic operations (addition, subtraction, multiplication, division)
        if "add" in command or "+" in command:
            numbers = [float(num.strip()) for num in command.replace("add", "").split("+") if num.strip().replace(".", "").isdigit()]
            if len(numbers) == 2:
                result = sum(numbers)
            else:
                return "Please provide two valid numbers to add."
        elif "subtract" in command or "-" in command:
            numbers = [float(num.strip()) for num in command.replace("subtract", "").split("-") if num.strip().replace(".", "").isdigit()]
            if len(numbers) == 2:
                result = numbers[0] - numbers[1]
            else:
                return "Please provide two valid numbers to subtract."
        elif "multiply" in command or "*" in command:
            numbers = [float(num.strip()) for num in command.replace("multiply", "").split("and") if num.strip().replace(".", "").isdigit()]
            if len(numbers) == 2:
                result = math.prod(numbers)
            else:
                return "Please provide two valid numbers to multiply."
        elif "divide" in command or "/" in command:
            numbers = [float(num.strip()) for num in command.replace("divide", "").split("/") if num.strip().replace(".", "").isdigit()]
            if len(numbers) == 2 and numbers[1] != 0:
                result = numbers[0] / numbers[1]
            else:
                return "Please provide two valid numbers to divide, and ensure the denominator is not zero."

#------------------- Trigonometric Functions (sin, cos, tan, etc.)----------------#
        elif "sin" in command:
            try:
                angle = float(command.replace("sin", "").strip())
                result = math.sin(math.radians(angle))
            except ValueError:
                return "Please provide a valid number for the angle."
        elif "cos" in command:
            try:
                angle = float(command.replace("cos", "").strip())
                result = math.cos(math.radians(angle))
            except ValueError:
                return "Please provide a valid number for the angle."
        elif "tan" in command:
            try:
                angle = float(command.replace("tan", "").strip())
                result = math.tan(math.radians(angle))
            except ValueError:
                return "Please provide a valid number for the angle."
        elif "cosec" in command:
            try:
                angle = float(command.replace("cosec", "").strip())
                result = 1 / math.sin(math.radians(angle))
            except ValueError:
                return "Please provide a valid number for the angle."
        elif "sec" in command:
            try:
                angle = float(command.replace("sec", "").strip())
                result = 1 / math.cos(math.radians(angle))
            except ValueError:
                return "Please provide a valid number for the angle."
        elif "cot" in command:
            try:
                angle = float(command.replace("cot", "").strip())
                result = 1 / math.tan(math.radians(angle))
            except ValueError:
                return "Please provide a valid number for the angle."

#----------------------Square Root and Cube Root------------------#


        elif "square root" in command:
            try:
                number = float(command.replace("square root of", "").strip())
                result = math.sqrt(number)
            except ValueError:
                return "Please provide a valid number for square root."
        elif "cube root" in command:
            try:
                number = float(command.replace("cube root of", "").strip())
                result = number ** (1 / 3)
            except ValueError:
                return "Please provide a valid number for cube root."

        # Return result if computed
        if result is not None:
            return f"The result is {result}"
        else:
            return "I couldn't understand the calculation request."

    except Exception as e:
        return f"An error occurred: {str(e)}"




#-----------------MERTRICS CONVERSIONS--------------#


def metric_converter(command):
    try:
        # Normalize input
        command = command.lower().replace("proton", "").replace("convert", "").strip()

        if not command:
            return "Please provide a valid conversion request."

        result = None

        # Handle conversions using shorthand notations
        if "m to km" in command or "meter to kilometer" in command:
            try:
                value = float(command.replace("m to km", "").replace("meter to kilometer", "").strip())
                result = value / 1000
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "km to m" in command or "kilometer to meter" in command:
            try:
                value = float(command.replace("km to m", "").replace("kilometer to meter", "").strip())
                result = value * 1000
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "cm to m" in command or "centimeter to meter" in command:
            try:
                value = float(command.replace("cm to m", "").replace("centimeter to meter", "").strip())
                result = value / 100
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "m to cm" in command or "meter to centimeter" in command:
            try:
                value = float(command.replace("m to cm", "").replace("meter to centimeter", "").strip())
                result = value * 100
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "mm to m" in command or "millimeter to meter" in command:
            try:
                value = float(command.replace("mm to m", "").replace("millimeter to meter", "").strip())
                result = value / 1000
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "m to mm" in command or "meter to millimeter" in command:
            try:
                value = float(command.replace("m to mm", "").replace("meter to millimeter", "").strip())
                result = value * 1000
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "km to mi" in command or "kilometer to mile" in command:
            try:
                value = float(command.replace("km to mi", "").replace("kilometer to mile", "").strip())
                result = value * 0.621371
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "mi to km" in command or "mile to kilometer" in command:
            try:
                value = float(command.replace("mi to km", "").replace("mile to kilometer", "").strip())
                result = value / 0.621371
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "yd to m" in command or "yard to meter" in command:
            try:
                value = float(command.replace("yd to m", "").replace("yard to meter", "").strip())
                result = value * 0.9144
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "m to yd" in command or "meter to yard" in command:
            try:
                value = float(command.replace("m to yd", "").replace("meter to yard", "").strip())
                result = value / 0.9144
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "in to cm" in command or "inch to centimeter" in command:
            try:
                value = float(command.replace("in to cm", "").replace("inch to centimeter", "").strip())
                result = value * 2.54
            except ValueError:
                return "Please provide a valid number for conversion."

        elif "cm to in" in command or "centimeter to inch" in command:
            try:
                value = float(command.replace("cm to in", "").replace("centimeter to inch", "").strip())
                result = value / 2.54
            except ValueError:
                return "Please provide a valid number for conversion."

        # Return result if computed
        if result is not None:
            return f"The result is {result}"

        else:
            return "I couldn't understand the conversion request."

    except Exception as e:
        return f"An error occurred: {str(e)}"


# ----------------- YouTube Control Functions ------------------


# Open YouTube
def open_youtube(): 
    try:
        webbrowser.open("https://www.youtube.com") # Attempts to open YouTube in the web browser
        reply("Opening YouTube.")
    except Exception as e:
        reply(f"Failed to open YouTube: {e}")

# Control YouTube Playback
def youtube_control(action):  # Control YouTube Playback
    try:
        if action == 'play' or action == 'pause': 
            pyautogui.press('k')  # Toggle play/pause
            reply("Toggled play/pause on YouTube.")
        elif action == 'next':
            pyautogui.hotkey('shift', 'n')  # Next video
            reply("Skipped to the next video.")
        elif action == 'previous':
            pyautogui.hotkey('shift', 'p')  # Previous video
            reply("Went back to the previous video.")
        elif action == 'close':
            pyautogui.hotkey('ctrl', 'w')  # Close the tab
            reply("Closed YouTube.")
        else:
            reply("Unknown YouTube command.") # Replies with an error message for unknown commands
    except Exception as e:
        reply(f"YouTube control error: {e}")


# ------------------Functions----------------------


def reply(audio):
    app.ChatBot.addAppMsg(audio)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def record_audio():
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)

        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry my Service is down. Please check your Internet connection')
        except sr.UnknownValueError:
            print('Cannot recognize')
            pass
        return voice_data.lower()


#----------------------------Add get_weather function here--------------------------------


def get_weather(city):
    API_KEY = "f25bc715d82c6a7c44acb71f3bab236d"  # Replace with your actual API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        print(data)  # Debugging: Print API response

        if data.get('cod') != 200:
            reply(f"Error: {data.get('message', 'Unable to fetch weather details')}")
        else:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            reply(f"The weather in {city} is {weather} with a temperature of {temp}°C, feels like {feels_like}°C.")
    except Exception as e:
        reply("Sorry, I couldn't fetch the weather details.")
        print("Error:", e)

#---------------------------------Executes Commands (input: string)---------------------------


def respond(voice_data):
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('proton','')
    app.eel.addUserMsg(voice_data)

    if is_awake==False:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    #----------------------------STATIC CONTROLS---------------------------------------
    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        reply('My name is Proton!')

    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

    elif 'search' in voice_data:
        reply('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' + voice_data.split('search')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'location' in voice_data:
        reply('Which place are you looking for ?')
        temp_audio = record_audio()
        app.eel.addUserMsg(temp_audio)
        reply('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif ('bye' in voice_data) or ('by' in voice_data):
        reply("Good bye Sir! Have a nice day.")
        is_awake = False

    elif ('exit' in voice_data) or ('terminate' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
        app.ChatBot.close()
        #sys.exit() always raises SystemExit, Handle it in main loop
        sys.exit()
    #----------------------------------#
   
    
    elif 'calculate' in voice_data or 'math' in voice_data:
        result = calculator(voice_data)
        reply(result)


#------------------------------------------#


    elif "convert" in voice_data:
        reply(metric_converter(voice_data))

#------------------------------------------#

  
    #----------------------------------#
    elif 'open youtube' in voice_data:
        open_youtube()

    elif 'play' in voice_data:
        youtube_control('play')

    elif 'pause' in voice_data:
        youtube_control('pause')

    elif 'next' in voice_data:
        youtube_control('next')

    elif 'previous' in voice_data:
        youtube_control('previous')

    elif 'close youtube' in voice_data:
        youtube_control('close')
  
    
    #------------------------------DYNAMIC CONTROLS--------------------------------


    elif 'launch gesture recognition' in voice_data:
        if Gesture_Controller.GestureController.gc_mode:
            reply('Gesture recognition is already active')
        else:
            gc = Gesture_Controller.GestureController()
            t = Thread(target = gc.start)
            t.start()
            reply('Launched Successfully')

    elif ('stop gesture recognition' in voice_data) or ('top gesture recognition' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
            reply('Gesture recognition stopped')
        else:
            reply('Gesture recognition is already inactive')
        
    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        reply('Copied')
          
    elif 'page' in voice_data or 'pest'  in voice_data or 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        reply('Pasted')

    elif 'weather' in voice_data:
        reply('Which city should I check for weather updates?')
        city = record_audio()  # Capture city name
        app.eel.addUserMsg(city)  # Display in GUI
        get_weather(city)  # Call get_weather function


        
    #------------------------- File Navigation (Default Folder set to C://)---------------------------


    elif 'list' in voice_data:
        counter = 0
        path = 'C://'
        files = listdir(path)
        filestr = ""
        for f in files:
            counter+=1
            print(str(counter) + ':  ' + f)
            filestr += str(counter) + ':  ' + f + '<br>'
        file_exp_status = True
        reply('These are the files in your root directory')
        app.ChatBot.addAppMsg(filestr)
        
    elif file_exp_status == True:
        counter = 0   
        if 'open' in voice_data:
            if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                    files = listdir(path)
                    filestr = ""
                    for f in files:
                        counter+=1
                        filestr += str(counter) + ':  ' + f + '<br>'
                        print(str(counter) + ':  ' + f)
                    reply('Opened Successfully')
                    app.ChatBot.addAppMsg(filestr)
                    
                except:
                    reply('You do not have permission to access this folder')
                                    
        if 'back' in voice_data:
            filestr = ""
            if path == 'C://':
                reply('Sorry, this is the root directory')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a)
                path += '//'
                files = listdir(path)
                for f in files:
                    counter+=1
                    filestr += str(counter) + ':  ' + f + '<br>'
                    print(str(counter) + ':  ' + f)
                reply('ok')
                app.ChatBot.addAppMsg(filestr)
                   
    else: 
        reply('I am not functioned to do this !')

# ------------------Driver Code--------------------

t1 = Thread(target = app.ChatBot.start)
t1.start()

#-------------------------------------- Lock main thread until Chatbot has started---------------------


while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:
    if app.ChatBot.isUserInput():
        #take input from GUI
        voice_data = app.ChatBot.popUserInput()
    else:
        #take input from Voice
        voice_data = record_audio()

    #process voice_data
    if 'proton' in voice_data:
        try:
            #Handle sys.exit()
            respond(voice_data)
        except SystemExit:
            reply("Exit Successfull")
            break
        except:
            #some other exception got raised
            print("EXCEPTION raised while closing.") 
            break