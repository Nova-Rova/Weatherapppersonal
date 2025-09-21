import json
from dotenv import load_dotenv
import os
load_dotenv()

class Patient:
    def __init__(self,name:str,age:str,dob:str,gender:str,bp:str,temperature:str,registration_date:str ,pulse:str, complaint:str):
        self.name =name
        self.age = age
        self.dob = dob
        self.gender = gender
        self.bp = bp
        self.temperature = temperature
        self.registration_date = registration_date
        self.pulse =pulse
        self.complaint = complaint
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
    def get_dob(self):
        return self.dob
    def set_dob(self,dob):
        self.dob = dob
    def get_gender(self):
        return self.gender
    def set_gender(self,gender):
        self.gender = gender
    def get_temperature(self):
        return self.temperature
    def set_name(self,temperature):
        self.temperature = temperature
    def get_registration_date(self):
        return self.registration_date
    def set_name(self,registration_date):
        self.registration_date = registration_date
    def get_pulse(self):
        return self.pulse
    def set_name(self,pulse):
        self.name = pulse
    def get_complaint(self):
        return self.complaint
    def set_complaint(self,complaint):
        self.complaint = complaint

[
  {
    "name": "Ama Nyarko",
    "age": 58,
    "dob": "1967-04-15",
    "gender": "F",
    "BP": "150/95",
    "temp": 36.7,
    "test_date": "2024-03-12",
    "pulse": 78,
    "complaint": "Intermittent headache"
  },
  {
    "name": "Ama Nyarko",
    "age": 58,
    "dob": "1967-04-15",
    "gender": "F",
    "BP": "162/100",
    "temp": 36.8,
    "test_date": "2024-09-05",
    "pulse": 82,
    "complaint": "Dizziness, poor sleep"
  },
  {
    "name": "Ama Nyarko",
    "age": 58,
    "dob": "1967-04-15",
    "gender": "F",
    "BP": "178/110",
    "temp": 37.0,
    "test_date": "2025-01-20",
    "pulse": 96,
    "complaint": "Frequent nocturia, tiredness"
  },
  {
    "name": "Ama Nyarko",
    "age": 58,
    "dob": "1967-04-15",
    "gender": "F",
    "BP": "175/108",
    "temp": 36.9,
    "test_date": "2025-05-11",
    "pulse": 88,
    "complaint": "Shortness of breath on exertion"
  },
  {
    "name": "Ama Nyarko",
    "age": 58,
    "dob": "1967-04-15",
    "gender": "F",
    "BP": "190/120",
    "temp": 37.1,
    "test_date": "2025-09-18",
    "pulse": 102,
    "complaint": "Severe headache, blurred vision"
  }
]
   
data = [
        {
            "name": "Ama Nyarko",
            "age": 58,
            "dob": "1967-04-15",
            "gender": "F",
            "BP": "150/95",
            "temp": 36.7,
            "test_date": "2024-03-12",
            "pulse": 78,
            "complaint": "Intermittent headache"
        },
        {
            "name": "Ama Nyarko",
            "age": 58,
            "dob": "1967-04-15",
            "gender": "F",
            "BP": "162/100",
            "temp": 36.8,
            "test_date": "2024-09-05",
            "pulse": 82,
            "complaint": "Dizziness, poor sleep"
        },
        {
            "name": "Ama Nyarko",
            "age": 58,
            "dob": "1967-04-15",
            "gender": "F",
            "BP": "178/110",
            "temp": 37.0,
            "test_date": "2025-01-20",
            "pulse": 96,
            "complaint": "Frequent nocturia, tiredness"
        },
        {
            "name": "Ama Nyarko",
            "age": 58,
            "dob": "1967-04-15",
            "gender": "F",
            "BP": "175/108",
            "temp": 36.9,
            "test_date": "2025-05-11",
            "pulse": 88,
            "complaint": "Shortness of breath on exertion"
        },
        {
            "name": "Ama Nyarko",
            "age": 58,
            "dob": "1967-04-15",
            "gender": "F",
            "BP": "190/120",
            "temp": 37.1,
            "test_date": "2025-09-18",
            "pulse": 102,
            "complaint": "Severe headache, blurred vision"
        }
    ]

patients = []
for entry in data:
            patient = Patient(
                    name=entry["name"],
                    age=str(entry["age"]),
                    dob=entry["dob"],
                    gender=entry["gender"],
                    bp=entry["BP"],
                    temperature=str(entry["temp"]),
                    registration_date=entry["test_date"],
                    pulse=str(entry["pulse"]),
                    complaint=entry["complaint"]
            )
            patients.append(patient)
from google import genai
from google.genai import types
API_KEY = os.getenv("GEMINI_API_KEY")
try:
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Analyze the following patient data and provide a CONSISE on the patient's health status, including potential concerns and recommendations for further action:
        {json.dumps([patient.__dict__ for patient in patients], indent=2)}
        try to identify conditions with the reands you see in the data.
    """,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)  # Disables thinking
        ),
    )
    print(response.text)
except Exception as e:
    print("hmm something went wrong error code: ",e)