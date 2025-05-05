import json
from Reader.pdf_Reader import read_pdf
import Extractors.Personal_information as Personal
import Extractors.ResumeExctractor as rex
import spacy
import re
import pprint
from spacy.matcher import Matcher
from Helpers import ExtractEntities as ExtractEntities
from Helpers import constants as const
import pandas as pd

class resume_parser():
    def __init__(self, file_path):
        nlp = spacy.load("en_core_web_sm")
        self.__matcher = Matcher(nlp.vocab)
        self.details = {
            'Name': None,
            'Email': None,
            'Phone': None,
            "jop_title" : None,
            'Skills': None,
            'Education': None,
            'Experience': None,
        }
        self.__file_path = file_path
        self.__text = read_pdf(self.__file_path)
        self.p__text = " ".join(self.__text.split())
        self.__nlp_doc = nlp(self.p__text)
        self.__sections = ExtractEntities.extract_sections(self.__text)
        self.__noun_chunks = list(self.__nlp_doc.noun_chunks)
        self.data_extractor()


    # we should add the function that assign the extracted data to the details dictionary then execute it on the __init__ method
    def data_extractor(self):
        phoneNumber =  Personal.extract_mobile_number(self.p__text)
        Name = Personal.extract_name(self.__nlp_doc , match=self.__matcher)
        Email = Personal.extract_email(self.p__text)
        skills = rex.extract_skills(self.__nlp_doc , self.__noun_chunks)
        jop_title = rex.extract_jop_title(self.__text)
        # exp = rex.extract_experience(self.p__text)
        # edu = rex.extract_education(self.__sections["education"])


        self.details['Phone'] = phoneNumber
        self.details['Name'] = Name
        self.details['Email'] = Email
        self.details["Skills"] = skills
        self.details["jop_title"] = jop_title
    def get_data(self):
        return self.details
    def get_section(self):
        return self.__sections
    
if __name__ == "__main__":
    file_path = "12334650.pdf"
    parser = resume_parser(file_path).get_data()
    print(json.dumps(parser))
    # text = parser.__tex
    # print([x.lower() for x in text if x not in const.STOPWORDS and x not in ['•' , '|' , '&' , '·']][:10])