from flask import Flask, request
from SVG import SVG

app = Flask(__name__)

@app.route('/img')
def generate_svg():

	try:
		x = int(request.args.get('x'))
		y = int(request.args.get('y'))
		bg_color = request.args.get('bg_color')
		cross_color = request.args.get('cross_color')
		if bg_color is not None and cross_color is not None:
			bg_color = "#" + str(request.args.get('bg_color'))
			cross_color = "#" + str(request.args.get('cross_color'))
			svg = SVG(x=x, y=y, background_color=bg_color, cross_color = cross_color)
		elif bg_color is not None:
			bg_color = "#" + str(request.args.get('bg_color'))
			svg = SVG(x=x, y=y, background_color=bg_color)
		elif cross_color is not None:
			cross_color = "#" + str(request.args.get('cross_color'))
			svg = SVG(x=x, y=y, cross_color=cross_color)
		else:
			svg = SVG(x=x, y=y)

		return svg.create().min_svg(), 200
	except Exception, e:
		return 'something went wrong!\nTry /img?x=10&y=10&bg_color=ff0000&cross_color=00ff000', 404
	
if __name__ == '__main__':
    app.run()