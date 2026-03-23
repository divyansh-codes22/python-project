print("🚀 FILE EXECUTION STARTED 🚀")

from core.text_cleaner import clean_text
from core.skill_extractor import extract_skills

# Read resume
with open("resumes/sample_resume.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

cleaned_text = clean_text(raw_text)

skills = extract_skills(cleaned_text)

print("\nDETECTED SKILLS:")
if skills:
    for skill in skills:
        print("-", skill)
else:
    print("No skills detected")