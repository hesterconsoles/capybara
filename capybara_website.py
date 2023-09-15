import time
#import pyttsx3
from flask import Flask, render_template

website=Flask(__name__,static_url_path='/static/')

@website.route('/')
def input_content():
    #language = input('pls input your wish: ')
    return render_template('capybara.html')


if __name__ == '__main__':
    website.run(host='0.0.0.0',debug=True)


'''
engine=pyttsx3.init()
def sayoutloud(content):

    if gender == 'F':
        voice = engine.getProperty('voices')
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tingting')
    else:
        pass

    #engine.say('明天要上班')
    engine.say(content)
    engine.runAndWait()



language=input('pls input your wish: ')
#gender = input('what kind of voice you want? M/F: ')


total=language.count("!")
while total>=0:
    if language.count("!")==0:
        print(f'{language}' + 'capybara~')
        sayoutloud(f'{language}'+'capybara~')

        
    else:
        print(f'{language}' + 'capybara~' * language.count('!'))
        sayoutloud(f'{language}'+'capybara~'*language.count('!'))


    time.sleep(0.1)
    total-=1

'''
