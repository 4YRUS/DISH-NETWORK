

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAQe4aGtyKMUq1RHiMXZx3BBJt7YRDDHac")


def prep_image(image_path):
    sample_file = genai.upload_file(path=image_path, display_name="Diagram")
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    return sample_file

def extract_text_from_image(sample_file, prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([sample_file, prompt])
    return response.text

def read_image_for_blind(path):

    sample_file=prep_image(path)
    text = extract_text_from_image(sample_file, "Explain whats in the image to a blind person in a brief.")
    return text


