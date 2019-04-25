from pdf2image import convert_from_path

path = '変換するpdfのパス'
images = convert_from_path(path)

i = 0
for image in images:
    image.save('unknown.png'.format(i), 'png')
    i += 1
