# utils/predictor.py

import re
import easyocr

reader = easyocr.Reader(['en'])

def extract_sugar_levels_from_image(image_path):
    result = reader.readtext(image_path, detail=0)
    full_text = " ".join(result)
    print("FULL TEXT FROM IMAGE:", full_text)  # Debugging

    # Try multiple keyword patterns for flexibility
    fasting = re.search(r'(Fasting|FBS|Fasting Blood Sugar)[^\d]{0,10}(\d{2,3})', full_text, re.IGNORECASE)
    postmeal = re.search(r'(Postprandial|PPBS|Post Meal|After Food)[^\d]{0,10}(\d{2,3})', full_text, re.IGNORECASE)

    values = {}

    if fasting:
        values['fasting'] = int(fasting.group(2))

    if postmeal:
        values['postmeal'] = int(postmeal.group(2))

    return values, full_text
