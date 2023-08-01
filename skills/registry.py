
from .collection.general import loveYou, noanswer, nameSkill, whatAreYouDoing
from .collection.general import thankingSkill, apologySkill, whatCanYouDo, loveYou
from .collection.greeting import greet, howAreYou, bye
from .collection.time import timer
from .collection.time import date
from .collection.internet import connect
from .collection.news import get_trending_news 
from .collection.browser import search_in_browser, play_song_in_youtube, open_website
from .collection.jokes import tell_jokes
from .collection.game import playGame

intents = {'intents' :  [

    {
        'responses': open_website,
        'patterns': ['open'],
        'tag': 'browser'
    },

    {
        'responses': get_trending_news,
        'patterns': ['news', 'today news'],
        'tag': 'news'
    },

    {
        'responses': timer,
        'patterns': ['time', 'hour','what is the time'],
        'tag': 'time'
    },

    {
        'responses': date,
        'patterns': ['date', 'what is the date'],
        'tag' : 'date'
    },

    {
        'responses': search_in_browser,
        'patterns': ['search'],
        'tag': 'search'
    },
    {
        'responses' : play_song_in_youtube,
        'patterns' : ['play'],
        'tag' : "songs on youtube"
    },

    {
        'responses': connect,
        'patterns': ["connected"],
        'tag': 'connectivity'
    },

    {
        'responses': tell_jokes,
        'patterns': ["jokes", "joke","make me smile", "comedy"],
        'tag': 'joke'
    },

    {
        'responses': nameSkill,
        'patterns': ["who are you", "name"],
        'tag': 'joke'
    },

    {
        'responses': whatAreYouDoing,
        'patterns': ["what are you doing", "what is going on", "what is happening"],
        'tag': 'what are you doing'
    },

    {
        'responses': apologySkill,
        'patterns': ["stupid", "idoit"],
        'tag': 'apology'
    },
    
    {
        'responses': whatCanYouDo,
        'patterns': ["what can you do for me", "what can you do", "what is use of you"],
        'tag': 'what can you do'
    },

    {
        'responses': thankingSkill,
        'patterns': ["Great", "nice", "awesome", "wonderfull"],
        'tag': 'thank'
    },
    {
        'responses': loveYou,
        'patterns': ["i love you"],
        'tag': 'love'
    },

    {
        'responses': greet,
        'patterns': ["hi", "hello", "yo", "hlo"],
        'tag': 'greet'
    },

    {
        'responses': howAreYou,
        'patterns': ["how are you"],
        'tag': 'how are you'
    },

    {
        'responses': playGame,
        'patterns': ["game"],
        'tag': 'game'
    },

    {
        'responses': bye,
        'patterns': ["bye", "see you"],
        'tag': 'bye'
    },

    {
        'responses': noanswer,
        'patterns': [""],
        'tag': 'noanswer'
    },
    
]}