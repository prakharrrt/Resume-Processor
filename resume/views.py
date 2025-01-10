from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CandidateSerializer
from .models import Candidate
import re
from PyPDF2 import PdfReader
import docx
from . import name_ext_func 

# Create your views here.

@api_view(['POST'])
def extract_resume(request):
    if 'Resume' not in request.FILES:
        return Response({"error": "No resume file uploaded"}, status=400)
    
    file = request.FILES['Resume']
    
    # Extract text from PDF or Word document
    text = ""
    if file.name.endswith('.pdf'):
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text
    else:
        return Response({"error": "Unsupported file format"}, status=400)
    
    print(text)
    

    # Extract the required fields using regular expressions
    first_name = "Not Found"
    email = "Not Found"
    mobile_number = "Not Found"

    first_name=name_ext_func.extract_first_name(text)

     # Use simple regex patterns to extract the first name, email, and mobile number
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d{1,4}?[ -]?\(?\d{1,3}?\)?[ -]?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,4}'


    # Find the first match for each pattern

    email_match = re.search(email_pattern, text)
    if email_match:
        email = email_match.group(0)

    phone_match = re.search(phone_pattern, text)
    if phone_match:
        mobile_number = phone_match.group(0)

    # Create and save the Candidate instance
    candidate = Candidate.objects.create(
        first_name=first_name,
        email=email,
        mobile_number=mobile_number
    )


    # Serialize the candidate and return as JSON
    serializer = CandidateSerializer(candidate)
    return Response(serializer.data)

