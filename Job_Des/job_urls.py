from django.urls import path
from Job_Des.job_views import test, job

urlpatterns = [
    path('test/', test),
    path('', job, name="job")
]