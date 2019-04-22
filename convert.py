from pdf2image import convert_from_path

path = '任意のpdfののパス'
images = convert_from_path(path)

i = 0
for image in images:
    image.save('test.png'.format(i), 'png')
    i += 1
