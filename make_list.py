import fitz
from PyQt5.QtGui import QImage
from PIL import Image, ImageQt
import os

ignore_list = ('apocaliptoLIB_booklist.txt',
'file.pdf',
'ideas_apocaliptoLIB.txt',
'map.txt',
'The_Charcoal_Foundry_by_David_J.._Gingery_(z-lib.org)[',
'youtube.txt',
'books.txt',
'.~lock.',
'f.txt')

cyrillic_translit={'\u0410': 'A', '\u0430': 'a',
'\u0411': 'B', '\u0431': 'b',
'\u0412': 'V', '\u0432': 'v',
'\u0413': 'G', '\u0433': 'g',
'\u0414': 'D', '\u0434': 'd',
'\u0415': 'E', '\u0435': 'e',
'\u0416': 'Zh', '\u0436': 'zh',
'\u0417': 'Z', '\u0437': 'z',
'\u0418': 'I', '\u0438': 'i',
'\u0419': 'I', '\u0439': 'i',
'\u041a': 'K', '\u043a': 'k',
'\u041b': 'L', '\u043b': 'l',
'\u041c': 'M', '\u043c': 'm',
'\u041d': 'N', '\u043d': 'n',
'\u041e': 'O', '\u043e': 'o',
'\u041f': 'P', '\u043f': 'p',
'\u0420': 'R', '\u0440': 'r',
'\u0421': 'S', '\u0441': 's',
'\u0422': 'T', '\u0442': 't',
'\u0423': 'U', '\u0443': 'u',
'\u0424': 'F', '\u0444': 'f',
'\u0425': 'Kh', '\u0445': 'kh',
'\u0426': 'Ts', '\u0446': 'ts',
'\u0427': 'Ch', '\u0447': 'ch',
'\u0428': 'Sh', '\u0448': 'sh',
'\u0429': 'Shch', '\u0449': 'shch',
'\u042a': '"', '\u044a': '"',
'\u042b': 'Y', '\u044b': 'y',
'\u042c': "'", '\u044c': "'",
'\u042d': 'E', '\u044d': 'e',
'\u042e': 'Iu', '\u044e': 'iu',
'\u042f': 'Ia', '\u044f': 'ia'}

def transliterate(word, translit_table):
    converted_word = ''
    for char in word:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        else:
            transchar = char
        converted_word += transchar
    return converted_word

f = open('apocaliptoLIB_booklist.txt', 'w')

# traverse root directory, and list directories as dirs and files as files
extensions = ['pdf', 'epub', 'djvu', 'mobi', 'docx', 'doc', 'txt']
counter = 0
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    for file in files:
        for ext in extensions:
            if (file.find(f".{ext}") != -1):
          
                print(len(path) * '---', file)
                file_trns = transliterate(file, cyrillic_translit)
                file_trns = file_trns.replace(' ', '_')
                ignored = False
                for filter in ignore_list:
                    if file_trns.find(filter) != -1:
                        ignored = True                        
                if not ignored:
                    counter = counter + 1
                    f.write(f'{counter}. {file_trns}\n')
                #print(path)
                #print(file)
f                