from django.shortcuts import render
from django.http import JsonResponse
from Job_Des.job_description import generate_job_description1
import json

def test(request):
    return render(request, 'job.html')

def job(request):
    if request.method == "POST":
        data = json.loads(request.body)
        jobtitle = data.get('jobtitle', '')
        company = data.get('company', '')
        experience = data.get('experience', 0)
        technology = data.get('technology', '')
        response = generate_job_description1(
        job_title=jobtitle,
        company_name=company,
        experience_required=experience,
        required_technologies=technology)
        return JsonResponse({"job_description": response})
    return JsonResponse({"success": False})