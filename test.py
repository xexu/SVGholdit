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

	def test_true_color_invalid_string(self):
		self.assertFalse(SVG()._true_color("asd"))

	def test_true_color_red(self):
		self.assertTrue(SVG()._true_color("#ff0000"))

	def test_true_color_invalid_red(self):
		self.assertFalse(SVG()._true_color("#gf0000"))

	def test_true_color_invalid_green(self):
		self.assertFalse(SVG()._true_color("#00gg00"))

	def test_true_color_uppercase_blue(self):
		self.assertTrue(SVG()._true_color("#0000FF"))



if __name__ == '__main__':
    unittest.main()