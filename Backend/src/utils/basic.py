import re

def format_tel(tel: str):
    if not tel: return None
    
    digits = re.findall(r'\d', tel)
    
    return ''.join(digits)

def format_name(name: str):
    if not name: return None

    return name.lower()