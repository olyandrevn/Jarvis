import webbrowser
import datetime

def open_website(url):
    webbrowser.open(url)

def tell_time():
    return datetime.datetime.now().strftime("%I:%M %p")
