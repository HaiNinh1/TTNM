import fitz
doc = fitz.open(r'D:\BTAP\TTNM\Bai 3_Phan 2_ Tinh tien dung.pdf')
for i, p in enumerate(doc):
    imgs = p.get_images()
    if imgs:
        print(f'Page {i+1}: {len(imgs)} images')
