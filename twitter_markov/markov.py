import nltk

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')

def generate_text(seed_text, initial_model=100):
    tokenized_content = tokenizer.tokenize(seed_text)
    content_model = nltk.NgramModel(2, tokenized_content)

    starting_words = content_model.generate(initial_model)[-2:]
    content = content_model.generate(22, starting_words)
    content =  " ".join(content)
    content = content.replace(' ,', ',')
    content = content.replace(' .', '.')
    content = content.replace(' !', '!')
    content = content.replace(' ?', '?')
    content = content.replace('( ', '(')
    content = content.replace(' )', ')')
    content = content.replace(' ;', ';')
    content = content.replace(" ' ", "'")
    content = content.replace(" : ", ": ")    
    return content
