from Reader.pdf_Reader import read_pdf
import Extractors.Personal_information as Personal
import spacy
import re
import pprint
from spacy.matcher import Matcher

class resume_parser():
    def __init__(self, file_path):
        nlp = spacy.load("en_core_web_sm")
        self.__matcher = Matcher(nlp.vocab)
        self.details = {
            'Name': None,
            'Email': None,
            'Phone': None,
            'Skills': None,
            'Education': None,
            'Experience': None,
        }
        self.__file_path = file_path
        self.__text = read_pdf(self.__file_path)
        self.p__text = " ".join(self.__text.split())
        self.__nlp_doc = nlp(self.p__text)
        self.data_extractor()


    # we should add the function that assign the extracted data to the details dictionary then execute it on the __init__ method
    def data_extractor(self):
        phoneNumber =       Personal.extract_mobile_number(self.p__text)
        Name =              Personal.extract_name(self.__nlp_doc , match=self.__matcher)
        Email =             Personal.extract_email(self.p__text)


        self.details['Phone'] = phoneNumber
        self.details['Name'] = Name
        self.details['Email'] = Email

    def get_data(self):
        return self.details
    
if __name__ == "__main__":
    file_path = "OmkarResume.pdf"
    parser = resume_parser(file_path).get_data()
    print(parser)