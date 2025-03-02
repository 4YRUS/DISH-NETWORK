import google.generativeai as genai
import base64

genai.configure(api_key=" ''' YOUR API KEY HERE ''' ")

def encode_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        temp = base64.b64encode(audio_file.read()).decode("utf-8")
        return temp

def read_audio_for_deaf(audio_path):
    audio_data = encode_audio(audio_path) 

    model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    response = model.generate_content([
        "give me a 2 items separated by '&@&' one with the exact text in the audio and other summerizing the audio ",
        {"mime_type": "audio/webm", "data": audio_data},
    ])

    return response.text if hasattr(response, "text") else response


if __name__=='__main__':
    audio_path = "C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\DISH\\dishnetwork\\audio\\recording_xz1YUs9.webm"  # Change to your WebM file path
    result = upload_audio_to_gemini(audio_path)

    print("Gemini Response:", result)
