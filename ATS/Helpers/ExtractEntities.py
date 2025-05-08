from Helpers import constants as const

def extract_sections(text):
    sections = {}
    key = False
    s = [i for i in text.split('\n')]
    for phrase in s:
        if len(phrase) == 1:
            sn = phrase
        else:
            sn = set(phrase.lower().split()) & set(const.RESUME_SECTIONS)
        try : 
            sn = list(sn)[0]
        except:
            pass
        if(sn in const.RESUME_SECTIONS):
            sections[sn] = []
            key = sn
        elif key and phrase:
            sections[key].append(phrase)
    return sections