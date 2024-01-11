# Requires Python 3.6 or higher due to f-strings
# %%
# Import libraries
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
from ExtractTable import ExtractTable
import pandas as pd
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
from dotenv import load_dotenv


load_dotenv()
et_sess = ExtractTable(api_key=os.getenv("extract_table_key"))
print(et_sess.check_usage())
# creating a pdf file object
pdfname = 'Exicure_Patent_WO2022147541A1'
#pdfFile = fr'\server\documents\patents\{pdfname}.pdf'
pdfFile = fr'C:\Users\apmcc\OneDrive\Documents\GRT_consulting\Analysis\{pdfname}.pdf'

if platform.system() == "Windows":
	# We may need to do some additional downloading and setup...
	# Windows needs a PyTesseract Download
	# https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine

	pytesseract.pytesseract.tesseract_cmd = (
		os.getenv("tesseract_path")
	)

	# Windows also needs poppler_exe
	path_to_poppler_exe = Path(os.getenv("poppler_path"))
	
	# Put our output files in a sane place...
	out_directory = Path(r"C:\Users\apmcc\Documents\github_projects\project_timeline\server\documents\patents").expanduser()
else:
	out_directory = Path("~").expanduser()	 

# Path of the Input pdf
PDF_file = Path(pdfFile)

# %%
# Store all the pages of the PDF in a variable
image_file_list = []

text_file = out_directory / Path(f"{pdfname}.txt")

def main():
	''' Main execution point of the program'''
	with TemporaryDirectory() as tempdir:
		# Create a temporary directory to hold our temporary images.

		"""
		Part #1 : Converting PDF to images
		"""

		if platform.system() == "Windows":
			pdf_pages = convert_from_path(
				PDF_file, 400, poppler_path=path_to_poppler_exe,first_page=100, last_page=121,
			)
		else:
			pdf_pages = convert_from_path(PDF_file, 400)
		# Read in the PDF file at 500 DPI
		

		# Iterate through all the pages stored above
		for page_enumeration, page in enumerate(pdf_pages, start=1):
			# enumerate() "counts" the pages for us.

			# Create a file name to store the image
			filename = f"{tempdir}\page_{page_enumeration:03}.jpg"

			# Declaring filename for each page of PDF as JPG
			# For each page, filename will be:
			# PDF page 1 -> page_001.jpg
			# PDF page 2 -> page_002.jpg
			# PDF page 3 -> page_003.jpg
			# ....
			# PDF page n -> page_00n.jpg

			# Save the image of the page in system
			page.save(filename, "JPEG")
			image_file_list.append(filename)
		print('images made')

		
		"""
		Part #2 - Recognizing text from the images using OCR
		"""

		with open(text_file, "a") as output_file:
			# Open the file in append mode so that
			# All contents of all images are added to the same file

			# Iterate from 1 to total number of pages
			for image_file in image_file_list:

				# Set filename to recognize text from
				# Again, these files will be:
				# page_1.jpg
				# page_2.jpg
				# ....
				# page_n.jpg

				# Recognize the text as string in image using pytesserct
				text = str(((pytesseract.image_to_string(Image.open(image_file)))))

				# The recognized text is stored in variable text
				# Any string processing may be applied on text
				# Here, basic formatting has been done:
				# In many PDFs, at line ending, if a word can't
				# be written fully, a 'hyphen' is added.
				# The rest of the word is written in the next line
				# Eg: This is a sample text this word here GeeksF-
				# orGeeks is half on first line, remaining on next.
				# To remove this, we replace every '-\n' to ''.
				text = text.replace("-\n", "")

				# Finally, write the processed text to the file.
				output_file.write(text)
			

			# At the end of the with .. output_file block
			# the file is closed after writing all the text.
				
		
		# At the end of the with .. tempdir block, the 
		# TemporaryDirectory() we're using gets removed!	 
	# End of main function!
				
		#Set mode to 'a' to add to excel file, set mode to 'w' to make new file
		with open('all_dfs.csv','a') as f:

			#Range must be all of the png files that you want to analyze
			for image_file in image_file_list:
				#check if image contains table
				print("Processing Image")
				
				#This is the API call, returns the value as a list of pd df
				table_data:pd.DataFrame = et_sess.process_file(filepath=image_file, output_format="df")
				for frame in table_data:
					frame.to_csv(f)
					f.write("\n")

		print("Extraction Complete.")
	


	
if __name__ == "__main__":
	# We only want to run this if it's directly executed!
	main()

# %%
