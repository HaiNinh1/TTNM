import fitz
doc = fitz.open(r'D:\BTAP\TTNM\Bai 3_Phan 2_ Tinh tien dung.pdf')
out = open(r'D:\BTAP\TTNM\_pdf_text.txt', 'w', encoding='utf-8')
for i, p in enumerate(doc):
    out.write(f'\n--- PAGE {i+1} ---\n')
    out.write(p.get_text())
out.close()
print('done', len(doc))