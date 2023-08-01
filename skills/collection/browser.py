
import webbrowser
import wikipedia

def search_in_browser(topic , *args):
    topic = topic[7:]
    webbrowser.open('https://www.google.com/search?q='+topic)
    return 'Opening in browser'

def play_song_in_youtube(song_name, *args):
    song_name = song_name[5:]
    webbrowser.open('https://www.youtube.com/results?search_query='+song_name)
    return 'Playing song on youtube'

def open_website(sitename, *args):
    sitename = sitename[5:]
    webbrowser.open('https://www.google.com/search?q='+sitename)
    return "Opening "+ sitename

#not added
def decoded_wiki_response(topic, *args):
    topic = topic[13]
    ny = wikipedia.page(topic)
    data = ny.content[:500].encode('utf-8')
    response = ''
    response += data.decode()
    return response