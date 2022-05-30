from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageDraw, ImageFont

WHITE = "#FFF"
FONTNAME = "Courier"


def watermark_img():

    # Create an Image Object from the selected Image
    img = Image.open(openfilename())
    width = simpledialog.askinteger(parent=window, title="Width", prompt="Enter a width for your image, must be an interger.")
    height = simpledialog.askinteger(parent=window, title="Height", prompt="Enter a height for your image, must be an interger.")
    width, height = img.size
    new_filename = simpledialog.askstring(title="Name", prompt="Enter a new name for your image.")
    font_style = simpledialog.askstring(title="Font", prompt="Choose your font, the font name must be correct.").lower()
    font_size = simpledialog.askinteger(title="Font Size", prompt="Enter a font size for your Watermark.")
    watermark_text = simpledialog.askstring(title="Watermark Text", prompt="Enter text to use as the watermark.")
    draw = ImageDraw.Draw(img)
    fontinfo = ImageFont.truetype(f"{font_style}.ttf", font_size)
    textwidth, textheight = draw.textsize(watermark_text, fontinfo)

    # calculate x,y coordinates of text.

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark on image.
    draw.text((x, y), watermark_text, font=fontinfo)
    img.save(f'./watermarked_images/{new_filename}.jpg')
    image = Image.open(f'./watermarked_images/{new_filename}.jpg')
    image.show()


def openfilename():

    # returns the file path for the img file selected.
    filename = filedialog.askopenfilename(initialdir="/desktop",
                                          title="Image to watermark",
                                          filetypes=(("all files", "*.*"), ("jpg files", "*.jpg")))
    return filename


window = Tk()
window.title("Image Watermark App")
window.resizable(False, False)
window.config(padx=50, pady=80, bg=WHITE)

logo_img = PhotoImage(file="images/logo.png")

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, pady=40)

add_watermark = Button(text="Choose File", highlightthickness=0, font=(FONTNAME, 10, "bold"), command=watermark_img)
add_watermark.grid(column=0, row=1)

window.mainloop()