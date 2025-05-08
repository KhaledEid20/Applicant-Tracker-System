import re
from Helpers import constants as const


def extract_mobile_number(text):
    """This extracts the mobile number from the text using regex."""
    # Found this complicated regex on : https://zapier.com/blog/extract-links-email-phone-regex/
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number
        
def extract_name(text, match):
    """This extracts the name from the text using spacy matcher."""
    # Define the pattern for matching names
    pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}]]
    match.add("NAME", *[pattern])
    matches = match(text)

    for match_id, start, end in matches:
        span = text[start:end]
        return span.text
    
def extract_email(text):
    '''
    Helper function to extract email id from text

    :param text: plain text extracted from resume file
    '''
    email = re.findall("[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}", text)
    if email:
        # return email
        try:
            return email[0].split()[0].strip()
        except IndexError:
            return None