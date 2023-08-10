from PIL import Image, ImageDraw, ImageFont

# Define constants variables
CARD_WIDTH = 800
CARD_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 0)  # Black
FONT_SIZE = 48
FONT_PATH = "font.ttf"
MESSAGE = "Happy Birthday!"
SENDER_NAME = "Komen"
BACKGROUND_IMAGE_PATH = "back.jpg"  # Path to your background image

# Create a new image with the background color
card_image = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), BACKGROUND_COLOR)

# Load the background image
background_image = Image.open('Images/background.jpg')

# Resize the background image to fit the card dimensions
background_image = background_image.resize((CARD_WIDTH, CARD_HEIGHT))

# Paste the background image onto the card
card_image.paste(background_image, (0, 0))

# Create a draw object
draw = ImageDraw.Draw(card_image)

# Add text
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
text_bbox = draw.textbbox((0, 0), MESSAGE, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = (CARD_WIDTH - text_width) // 2
text_y = (CARD_HEIGHT - text_height) // 2
draw.text((text_x, text_y), MESSAGE, font=font, fill=TEXT_COLOR)

# Add sender's name
sender_font = ImageFont.truetype(FONT_PATH, FONT_SIZE - 10)
sender_text = "From: " + SENDER_NAME
text_bbox = draw.textbbox((0, 0), sender_text, font=sender_font)
sender_width = text_bbox[2] - text_bbox[0]
sender_height = text_bbox[3] - text_bbox[1]
sender_x = (CARD_WIDTH - sender_width) // 2
sender_y = text_y + text_height + 20
draw.text((sender_x, sender_y), sender_text, font=sender_font, fill=TEXT_COLOR)

# Save the card
card_image.save("birthday_card.png")
