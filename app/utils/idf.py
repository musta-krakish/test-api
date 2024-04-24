import math
import re
from collections import Counter

def idf(word: str, documents) -> float:
    documents = sum(1 for d in documents if word in d)
    return math.log(len(documents) / (1 + documents))

def process_file(file):
    text = file.read().decode("utf-8")
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)