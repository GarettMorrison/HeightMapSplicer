from PIL import Image
import sys
import math as m
import webbrowser
import sys


#Parameters
layers = 5


def getPix(image, x, y):
	return image[x,y]

try:
	inputFile = sys.argv[1]
	if len(sys.argv) > 2:
		layers = sys.argv[2]
	HM = Image.open(inputFile).convert('L')

except IOError:
	print("Unable to load image")
	sys.exit(1)


hPix = HM.load()

hmin = getPix(hPix, 0, 0)
hmax = getPix(hPix, 0, 0)
for i in range(HM.size[0]):
	for j in range(HM.size[1]):
		if getPix(hPix, i, j) < hmin:
			hmin = getPix(hPix, i, j)

		if getPix(hPix, i, j) > hmax:
			hmax = getPix(hPix, i, j)

layerHeight = (hmax - hmin)/(layers)

print("hmin",hmin)
print("hmax",hmax)
print("layerHeight", layerHeight)


new = Image.new("L",(HM.size[0] * layers,HM.size[1]))
nPix = new.load()

for lay in range(layers):

	layMin = lay * layerHeight
	layMax = (lay +1) * layerHeight

	for i in range(HM.size[0]):
		for j in range(HM.size[1]):
			val = getPix(hPix, i, j)
			test = val

			if test < layMax:
				nPix[i + lay*HM.size[0],j] = 255


filename = "OutputFull.png"
new.save(filename)
new.close()
print("Saved " + str(filename))