import json
import os

def save_result(image_path, extracted_text, confidence):
    os.makedirs("results", exist_ok=True)

    output = {
        "image_name" : image_path,
        "extracted_text" : extracted_text,
        "confidence" : round(float(confidence),1)
    }

    output_path = os.path.join("results", image_name + ".json")

    with open(output_path, "w") as f:
        json.dump(output, f, indent=4)
    
    return output_path     