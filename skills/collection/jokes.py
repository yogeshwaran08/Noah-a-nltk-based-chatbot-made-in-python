import pyjokes

def tell_jokes(*args):
    return pyjokes.get_joke(language="en", category="neutral")