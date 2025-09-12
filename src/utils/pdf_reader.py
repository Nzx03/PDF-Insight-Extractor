#opens and reads Pdf
import sys
import fitz
from src.logger import logger
from src.exception import CustomException
import os

pdf_path=r"input_pdfs\unit-1-da-notes-for-data-analytics-unit-1 (1).pdf"
output_path="output\highlights\Doc1.pdf"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

def extract_highlights(pdf_path: str,output_path:str):

      try:
            doc = fitz.open(pdf_path)
            
            highlight_text=[]
            for page_number in doc:
                  highlights=[] 
                  # page=doc[page_number]  #for storing the coordinates of all highlights
                  annot=page_number.first_annot 
                  #to get the fisrt annotation
                  while annot:
                        if annot.type[0]==8:
                              coordinates=annot.vertices
                              if len(coordinates)==4:
                                    h_coordinate=fitz.Quad(coordinates).rect #converting those 4 points into rectangular box
                                    highlights.append(h_coordinate)
                              else:  #for highlights traversing to other lines
                                    coordinates=[coordinates[i:i+4] for i in range(0,len(coordinates),4)] #breaking others as a group of 4 vertices
                                    for j in range(0,len(coordinates)):
                                          coordinate=fitz.Quad(coordinates[j]).rect
                                          highlights.append(coordinate)
                        annot=annot.next
                        
                  all_words=page_number.get_text("words")

                  for h in highlights:
                        sentence= [w[4] for w in all_words if fitz.Rect(w[0:4]).intersects(h)]  #looping to  coordinates of word
                        highlight_text.append(" ".join(sentence))
                        
                          
                                    
                                                            
            logger.info(f"Writing {len(highlight_text)} highlights to {output_path}")      
                                          
            with open(output_path,'w',encoding="utf-8") as file:
                  file.write("\n".join(highlight_text))

            logger.info("Highlight extraction completed successfully")
            print(f"Extracted{len(highlight_text)} highlights saved to {output_path}")

             # print("first 200 characters of page",text[:1000].replace('\t',''))
      except Exception as e:
            logger.error("Error occured while extracting")
            raise CustomException(e,sys) 

extract_highlights(pdf_path, output_path)