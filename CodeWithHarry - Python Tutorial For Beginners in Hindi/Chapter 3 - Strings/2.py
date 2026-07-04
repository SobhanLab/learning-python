letter = ''' Dear <|Name|>,
You are selected!
Date: <|Date|>'''

print(letter.replace("<|Name|>", "Sobhan").replace("<|Date|>", "4 July 2026"))