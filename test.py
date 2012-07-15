import unittest
from SVG import *


class TestSVG(unittest.TestCase):
	def test_default(self):
		f = open('./img/test_default.svg', 'w')
		f.write(SVG().create().pretty_svg())
		f.close()

	def test_default_min(self):
		f = open('./img/test_default_min.svg', 'w')
		f.write(SVG().create().min_svg())
		f.close()

	def test_10x10(self):
		f = open('./img/test_10x10.svg', 'w')
		f.write(SVG(x=10, y=10).create().min_svg())
		f.close()

	def test_100x16_red_bg(self):
		f = open('./img/test_100x16_red_bg.svg', 'w')
		f.write(SVG(y=16, background_color="#FF0000").create().min_svg())
		f.close()

	def test_50x150_green_cross(self):
		f = open('./img/test_50x150_green_cross.svg', 'w')
		f.write(SVG(x=50, y=150, cross_color="#00FF00").create().min_svg())
		f.close()



if __name__ == '__main__':
    unittest.main()