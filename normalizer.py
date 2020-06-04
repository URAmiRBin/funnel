import re

def normilize(text):
    text = re.sub('ك', 'ک', text)
    text = re.sub('ي', 'ی', text)
    text = re.sub('ة', 'ه', text)
    text = re.sub('ؤ', 'و', text)
    text = re.sub('أ', 'ا', text)
    text = re.sub('ؤ', 'و', text)
    freaking_erab =     ['\u064B',
						'\u064C', 
						'\u064D', 
						'\u064E', 
						'\u064F', 
						'\u0650', 
						'\u0651', 
						'\u0652']
    rx = '[' + re.escape(''.join(freaking_erab)) + ']'
    text = re.sub(rx, '', text)
    return text