from django.shortcuts import render
from .models import patient,symptom,treatment

def home(request):

    r_symptom = None

    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        r_symptom=request.POST.get('symptoms')
        en=patient(name=name,age=age,gender=gender,contact=contact,email=email)
        en.save()

    symptoms=symptom.objects.all() 
    treatments=treatment.objects.all()
    patients=patient.objects.latest('id')

    recentSelected = None
    recentS = None

    for i in treatments:
        if str(i.symptom) == r_symptom:
            recentSelected = i.possible_diseases
            recentS = i.treatment
            break

    contex={
        'symptoms':symptoms,
        'treatments':treatments,
        'patients':patients,
        'recentSelected':recentSelected,
        "recentS":recentS,
    }

    return render(request,'index.html',contex)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# Create your views here.
