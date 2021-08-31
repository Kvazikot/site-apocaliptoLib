import fitz
from PyQt5.QtGui import QImage
from PIL import Image, ImageQt
import os

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

def save_pdf_as_jpgs(in_filename, out_path):
    pdf_document = fitz.open(in_filename)
    #for current_page in range(len(pdf_document)):
    for page in reversed(pdf_document):
        pix = page.get_pixmap()
        pix = fitz.Pixmap(fitz.csRGB, pix)
        fmt = QImage.Format_RGBA8888
        # set the mode depending on alpha
        mode = "RGBA" if pix.alpha else "RGB"
        img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        qtimg = ImageQt.ImageQt(img)
        #qtimg = QImage(pix.samples_ptr, pix.width, pix.height, fmt)
        pagenum = "page%s.jpg" % (page.number)
        os.makedirs(f"images\{out_path}",mode=0o777, exist_ok=True)
        qtimg.save(f"images\{out_path}\{pagenum}.jpg")


f = open('map.txt', 'w')

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    #print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if (file.find(".pdf") != -1) or (file.find(".epub") != -1):
            print(len(path) * '---', file)
            file_trns = transliterate(file, cyrillic_translit)
            file_trns = file.replace(' ', '_')
            print(root + "\\" + file)
            path_trns = file_trns.split('.')[0]
            path_trns = path_trns[0:25]
            save_pdf_as_jpgs(root + "\\" + file, path_trns)
            f.write(f'{file} # {path_trns}\n')
            #print(path)
            #print(file)