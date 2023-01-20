## Absolute position and font

import photoshop.api as ps
from areaDetection import detection_text

def main(input_img, output_psd):
	detection_results = detection_text(input_img)
	app = ps.Application()
	doc = app.documents.add()

	for idx, block in enumerate(detection_results):
		text_item = block[1][0]
		new_text_layer = doc.artLayers.add()
		new_text_layer.kind = ps.LayerKind.TextLayer
		new_text_layer.textItem.contents = text_item
		print("content", text_item)
		new_text_layer.textItem.position = [50, idx * 14 + 20]
		new_text_layer.textItem.size = 12

	# options = ps.PhotoshopSaveOptions(quality=5)
	options = ps.PhotoshopSaveOptions()
	# # save to file
	doc.saveAs(output_psd, options, asCopy=True)

if __name__ == '__main__':
	input_img = 'Capture-1.png'
	output_psd = "result_psd.psd"
	main(input_img, output_psd)
