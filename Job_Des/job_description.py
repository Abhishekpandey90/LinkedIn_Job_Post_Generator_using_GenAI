import google.generativeai as genai
import os
import logging


import warnings
# Define a custom warning handler
def warning(*args, **kwargs):
    pass  # Suppress all warnings
warnings.warn = warning
#os.environ['API_KEY'] = 'AIzaSyCxC5BxwGAcXumrtCD9U24_h1EehOtsfDY'
genai.configure(api_key="AIzaSyCxC5BxwGAcXumrtCD9U24_h1EehOtsfDY")
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_job_description1(job_title, company_name, experience_required, required_technologies):
    # Create a refined prompt using user inputs
    prompt = f"""
    Generate a professional and concise job description for the following:
    - Job Title: {job_title}
    - Company Name: {company_name}
    - Experience Required: {experience_required}+ years
    - Required Technologies: {required_technologies}

    Exclude the "About" section and avoid informal phrases also do not use 'e.g' word. and do not repeat word 'Experience'many time use similar words, Structure it like a LinkedIn job page, including job summary, key responsibilities, requirements, and qualifications. Ensure the content is concise, avoids repetition, and is presented in a formal tone.
    """

    # Generate the job description using the model
    response = model.generate_content(prompt).text

    return response
'''
#Example user inputs
job_title = input("Enter Job Title :")#"ML Engineer"
company_name = input("Enter Company Name : ")#"I2V"
experience_required = int(input("Enter Required Experience :")) #1
required_technologies = input("Mentioned Required Technology :") # "ML, DL, NLP, CV, Gen AI"

# Generate job description
job_description1 = generate_job_description1(job_title, company_name, experience_required, required_technologies)

# Print the generated job description
print("Generated Job Description:")
print(job_description1)'''