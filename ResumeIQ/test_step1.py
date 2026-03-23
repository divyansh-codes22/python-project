print("🚀 FILE EXECUTION STARTED 🚀")

from core.resume_reader import read_resume
from core.text_cleaner import clean_text

raw_text = read_resume("sample_resumes/sample.txt") 
cleaned_text = clean_text(raw_text) 

print("\nRAW TEXT (first 200 chars):") 
print(raw_text[:200]) 

print("\nCLEANED TEXT (first 200 chars):") 
print(cleaned_text[:200]) 

print("\nSTEP 1 TEST COMPLETED SUCCESSFULLY")