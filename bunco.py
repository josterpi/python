
import random

win = """
<img src="http://www.flightglobal.com/blogs/terminal-q/dice.gif" style="height: 100px;" />
<h1>You win!</h1>
<p>Here's your prize<br />
<img src="%s"/>
</p>
<form action="."><input type="submit" value="Play Bunco by yourself again"/></form>
"""
lose = """
<img src="http://www.flightglobal.com/blogs/terminal-q/dice.gif" style="height: 100px;" />
<h1>Sorry, you lose.</h1>
<form action="."><input type="submit" value="Play Bunco by yourself again"/></form>
"""

prizes = [
        "http://mfrost.typepad.com/cute_overload/images/bunny.jpg",
        "http://img.photobucket.com/albums/v252/SentimentArt/kitty.jpg",
        "http://img.dailymail.co.uk/i/pix/2007/07_03/mallardMS2807_468x397.jpg",
        "http://www.funpic.hu/files/pics/00030/00030946.jpg",
        "http://img.photobucket.com/albums/v120/LadyMalchav/05.jpg"
        ]

def app(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    result = random.choice([False, True])
    if result:
        prize = random.choice(prizes)
        return [win % prize]
    else:
        return [lose]

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host="0.0.0.0", port='8080')

