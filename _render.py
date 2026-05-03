import fitz, os
os.makedirs(r'D:\BTAP\TTNM\_slides', exist_ok=True)
doc = fitz.open(r'D:\BTAP\TTNM\Bai 3_Phan 2_ Tinh tien dung.pdf')
for i, p in enumerate(doc):
    pix = p.get_pixmap(dpi=120)
    pix.save(rf'D:\BTAP\TTNM\_slides\page_{i+1:02d}.png')
print('done', len(doc))
