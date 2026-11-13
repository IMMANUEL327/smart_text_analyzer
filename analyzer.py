import re
from collections import Counter as counter

    
def clean_text(text):
    # Remove special characters and punctuation
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    cleaned_text =re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text 

def extract_words(text):
    # Split the text into words
    words = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return words

def count_words(words):
    word_count = counter(words)
    return word_count

#extracting nummbers

def extract_numbers(text):
    # Extract numbers from the text
    numbers = re.findall(r'-?\d+(?:\.\d+)?', text)
    return numbers

#Extract email addressesdef
def extract_email_addresses(text):
    # Extract email addresses from the text
    pattarn =r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_addresses = re.findall(pattarn, text)
    return email_addresses



def analyze_text(text):
    cleaned_text = clean_text(text)
    words = extract_words(cleaned_text)
    word_count = count_words(words)
    total_words = len(words)
    unique_words = len(set(words))
    top_words = word_count.most_common(3)
    numbers = extract_numbers(text)
    email_addresses = extract_email_addresses(text)

    return {
        'cleaned_text': cleaned_text,
        'total_words': total_words,
        'unique_words': unique_words,
        'word_frequencies': word_count,
        'top_words': top_words,
        'numbers': numbers,
        'email_addresses': email_addresses
    }

if __name__ == "__main__":
    # Run this small example only when analyzer.py is started directly.
    # Importing analyze_text from the Streamlit app will not print demo output.
    simple_text = "Hello!!! python 123 @world. Python is intresting."
    cleaned = clean_text(simple_text)
    words = extract_words(cleaned)
    word_count = count_words(words)

    print("Cleaned Text:", cleaned)
    print("Extracted Words:", words)
    print("Total Words:", len(words))
    print("Unique Words:", len(set(words)))
    print("Word Frequencies:", word_count)
    print("Top Words:", word_count.most_common(3))
