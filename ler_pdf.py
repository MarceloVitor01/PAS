from PyPDF2 import PdfReader
import re

with open('Notas.pdf', 'rb') as pdf:
    leitor = PdfReader(pdf)

    numero_paginas = len(leitor.pages)

    texto_base = ''
    for _ in range(numero_paginas):
        pagina = leitor.pages[_]

        texto_base += pagina.extract_text()

with open('Notas.txt', 'w', encoding='utf-8') as txt:
    txt.write(texto_base)
