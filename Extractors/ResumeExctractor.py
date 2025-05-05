import os
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import re
from Helpers import constants as const
from fuzzywuzzy import process

# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

def extract_skills(nlp_text, noun_chunks):
    '''
    Helper function to extract skills from spacy nlp text

    :param nlp_text: object of `spacy.tokens.doc.Doc`
    :param noun_chunks: noun chunks extracted from nlp text
    :return: list of skills extracted
    '''
    tokens = [token.text for token in nlp_text if not token.is_stop]
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'skills.csv')) 
    skills = list(data.columns.values)
    skillset = []
    # check for one-grams
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    return [i.capitalize() for i in set([i.lower() for i in skillset])]


def extract_jop_title(text):
    l = []
    titles_list = pd.read_csv("Extractors\job-phrase-list.csv")
    titles_list = titles_list.iloc[:, [0]]  # Keep only the first column
    df_list = titles_list.iloc[:, 0].tolist()  # Convert the dataframe to a list
    text_cleaned = [x.lower() for x in text.split() if x not in const.STOPWORDS and x not in ['•' , '|' , '&' , '·']][:10]
    for i in text_cleaned:
        matches = process.extract(i, df_list)
        for match , score in matches:
            if score > 80:
                l.append(match)
        if(len(l) != 0):
            break
    return l[0]



# def extract_education(nlp_text):
#     '''
#     Helper function to extract education from spacy nlp text

#     :param nlp_text: object of `spacy.tokens.doc.Doc`
#     :return: tuple of education degree and year if year if found else only returns education degree
#     '''
#     edu = {}
#     # Extract education degree
#     for index, text in enumerate(nlp_text):
#         for tex in text.split():
#             tex = re.sub(r'[?|$|.|!|,]', r'', tex)
#             if tex.upper() in const.EDUCATION and tex not in const.STOPWORDS:
#                 edu[tex] = text + nlp_text[index + 1]

#     # Extract year
#     education = []
#     for key in edu.keys():
#         year = re.search(re.compile(const.YEAR), edu[key])
#         if year:
#             education.append((key, ''.join(year.group(0))))
#         else:
#             education.append(key)
#     return education


# def extract_experience(resume_text):
#     '''
#     Helper function to extract experience from resume text

#     :param resume_text: Plain resume text
#     :return: list of experience
#     '''
#     wordnet_lemmatizer = WordNetLemmatizer()
#     stop_words = set(stopwords.words('english'))

#     # word tokenization 
#     word_tokens = nltk.word_tokenize(resume_text)

#     # remove stop words and lemmatize  
#     filtered_sentence = [w for w in word_tokens if not w in stop_words and wordnet_lemmatizer.lemmatize(w) not in stop_words] 
#     sent = nltk.pos_tag(filtered_sentence)

#     # parse regex
#     cp = nltk.RegexpParser('P: {<NNP>+}')
#     cs = cp.parse(sent)
    
#     # for i in cs.subtrees(filter=lambda x: x.label() == 'P'):
#     #     print(i)
    
#     test = []
    
#     for vp in list(cs.subtrees(filter=lambda x: x.label()=='P')):
#         test.append(" ".join([i[0] for i in vp.leaves() if len(vp.leaves()) >= 2]))

#     # Search the word 'experience' in the chunk and then print out the text after it
#     x = [x[x.lower().index('experience') + 10:] for i, x in enumerate(test) if x and 'experience' in x.lower()]
#     return x