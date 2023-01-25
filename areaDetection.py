from paddleocr import PaddleOCR,draw_ocr
ocr = PaddleOCR(use_angle_cls=True, lang='en') 

## detection
def detection_text(img):
	result = ocr.ocr(img, cls=True)
	return result[0]

def print_data():
	print("data")
