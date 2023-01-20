## Original position and font

import photoshop.api as ps
from areaDetection import detection_text

def main(input_img, output_psd):
	detection_results = detection_text(input_img)
	app = ps.Application()
	doc = app.documents.add()
	for block in detection_results:
		# new_layer = doc.artLayers.add()

		text_color = ps.SolidColor()
		text_color.rgb.red = 0
		text_color.rgb.green = 255
		text_color.rgb.blue = 0

		new_text_layer = doc.artLayers.add()
		new_text_layer.kind = ps.LayerKind.TextLayer
		new_text_layer.textItem.contents = block[1][0]
		print("content", block[1][0])
		new_text_layer.textItem.position = block[0][0]
		print("position", block[0][0])
		new_text_layer.textItem.size = abs(block[0][0][1] - block[0][3][1])
		new_text_layer.textItem.color = text_color

	# options = ps.PhotoshopSaveOptions(quality=5)
	options = ps.PhotoshopSaveOptions()
	# # save to file
	doc.saveAs(output_psd, options, asCopy=True)

if __name__ == '__main__':
	input_img = 'Capture-1.png'
	output_psd = "result_psd.psd"
	main(input_img, output_psd)
