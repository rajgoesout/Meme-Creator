from PIL import Image, ImageDraw, ImageFont
import textwrap


def generate_meme(image_path, top_text, bottom_text='', font_path='./fonts/impact/Impacted.ttf', font_size=9):
	im = Image.open(image_path)
	draw = ImageDraw.Draw(im)
	image_width, image_height = im.size

	font = ImageFont.truetype(font=font_path, size=int(image_height*font_size)//100)

	top_text = top_text.upper()
	bottom_text = bottom_text.upper()

	char_width, char_height = font.getsize('A')
	chars_per_line = image_width // char_width
	top_lines = textwrap.wrap(top_text, width=chars_per_line)
	bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

	print(top_lines)
	print(bottom_lines)

	y = 10
	for line in top_lines:
		line_width, line_height = font.getsize(line)
		x = (image_width - line_width)/2
		draw.text((x, y), line, fill='white', font=font)
		y += line_height

	y = image_height - char_height * len(bottom_lines) - 30
	for line in bottom_lines:
		line_width, line_height = font.getsize(line)
		x = (image_width - line_width)/2
		draw.text((x, y), line, fill='white', font=font)
		y += line_height

	im.save('meme-' + im.filename.split('/')[-1])
	im.show()


if __name__ == '__main__':
	top_text = "Cheers to everything that we do wrong"
	bottom_text = "'Cause nobody remembers what we do right anyway"
	generate_meme('./cheers.jpg', top_text=top_text, bottom_text=bottom_text)
