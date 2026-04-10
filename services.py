import re
from collections import Counter

def text_analysis(text:str):
    
    words = re.findall(r'\b\w+\b', text.lower())

    word_count = len(words)
    char_count = len(text)
    sentence_count = len(re.findall(r'[.!?]+', text))
    
    top_words = [word for word, _ in Counter(words).most_common(5)]

    reading_time = round(word_count / 200, 2)

    return {
    "word_count": word_count,
    "character_count": 5,
    "sentence_count": sentence_count,
    "top_words": top_words,
    "reading_time_minutes": reading_time
    }
