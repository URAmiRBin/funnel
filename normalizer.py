import re
from fetch import fetch_column

def normilize(contents):
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            contents[i][j] = re.sub('ك', 'ک', contents[i][j])
            contents[i][j] = re.sub('ي', 'ی', contents[i][j])
            contents[i][j] = re.sub('ة', 'ه', contents[i][j])
            contents[i][j] = re.sub('ؤ', 'و', contents[i][j])
            contents[i][j] = re.sub('أ', 'ا', contents[i][j])
            contents[i][j] = re.sub('ؤ', 'و', contents[i][j])
            freaking_erab =     ['\u064B',
                                '\u064C',
                                '\u064D',
                                '\u064E',
                                '\u064F',
                                '\u0650',
                                '\u0651',
                                '\u0652']
            rx = '[' + re.escape(''.join(freaking_erab)) + ']'
            contents[i][j] = re.sub(rx, '', contents[i][j])
    return contents

def cleanup(contents):
    for i in range(len(contents)):
        contents[i] = re.sub('<.*?>', ' ', contents[i])
        contents[i] = re.sub('{.*?}', ' ', contents[i])
        contents[i] = re.sub('\u200f', ' ', contents[i])
        contents[i] = re.sub(r'\&.+;', ' ',contents[i])
        contents[i] = re.sub('[؟.();}@_=:!$%^&/،,;۲۶۷۵۰{۳۴۸۱۹؛1234567890]', '', contents[i])
        contents[i] = re.sub('[a-zA-Z]', '', contents[i])
        contents[i] = re.sub('\u200c', ' ', contents[i])
        contents[i] = re.sub('\-', ' ', contents[i])
        contents[i] = contents[i].replace('\n', ' ')
        contents[i] = re.sub(' +', ' ', contents[i])
    return contents