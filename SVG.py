from xml.dom.minidom import Document

class SVG:
	def __init__(self, x=100, y=100):
		self.doc = Document()
		self.x = x
		self.y = y

	def create(self, path=None):
		svg_attributes = {}
		text_attributes = {}

		svg_attributes["xmlns"] = "http://www.w3.org/2000/svg"
		svg_attributes["version"] = "1.1"
		svg_attributes["width"] = str(self.x)+"px"
		svg_attributes["height"] = str(self.y)+"px"
		svg = self._create_svg_canvas(svg_attributes)
		self.doc.appendChild(svg)

		background = self._create_background()
		svg.appendChild(background)

		cross = self._create_cross()
		svg.appendChild(cross)

		text_attributes["text"] = str(self.x)+"px x "+str(self.y)+"px"
		text_attributes["font-size"] = "12"
		text_attributes["font-family"] = "monospace"
		text_tag = self._create_text(text_attributes)
		if text_tag is not None:
			svg.appendChild(text_tag)

		return self


	def _create_svg_canvas(self, svg_attributes):
		svg = self.doc.createElement("svg")
		for key, value in svg_attributes.items():
			svg.setAttribute(key, value)
		return svg
		
	def _create_text(self, text_attributes):
		fsize = int(text_attributes["font-size"])
		textsize = fsize * 0.55 * len(text_attributes["text"])
		if self.x  >=  textsize and self.y > fsize + 2:
			attributes = dict(text_attributes.items() + self._text_coords(fsize, textsize).items())
			text_tag = self.doc.createElement("text")
			text_tag.appendChild(self.doc.createTextNode(attributes.pop("text")))
			for key, value in attributes.items():
				text_tag.setAttribute(key, value)
			return text_tag
		else:
			return None

	def _text_coords(self, fsize, textsize):
		x = int((self.x - textsize) / 2)
		y = int((self.y - 2) / 2) + fsize / 2
		return {"x" : str(x), "y" : str(y)}

	def _create_cross(self, color = "#aaaaaa"):
		cross = self.doc.createElement("g")
		line1 = self.doc.createElement("line")
		line1.setAttribute("x1", "0")
		line1.setAttribute("y1", "0")
		line1.setAttribute("x2", str(self.x))
		line1.setAttribute("y2", str(self.y))
		line1.setAttribute("style", "stroke:"+color)

		line2 = self.doc.createElement("line")
		line2.setAttribute("x1", str(self.x))
		line2.setAttribute("y1", "0")
		line2.setAttribute("x2", "0")
		line2.setAttribute("y2", str(self.y))
		line2.setAttribute("style", "stroke:"+color)

		cross.appendChild(line1)
		cross.appendChild(line2)

		return cross

	def _create_background(self, color = "#dddddd"):
		rect = self.doc.createElement("rect")
		rect.setAttribute("x", "0")
		rect.setAttribute("y", "0")
		rect.setAttribute("width", str(self.x))
		rect.setAttribute("height", str(self.y))
		rect.setAttribute("style", "fill:"+color+";stroke:"+color)

		return rect





	def pretty_svg(self):
		return self.doc.toprettyxml(indent="  ")
	def min_svg(self):
		return self.doc.toprettyxml(indent="")