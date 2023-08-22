from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant

# Create your views here.

def participant_details(request):
    if request.method == "GET":
        return render(request,"registration/participant-details.html",{"email":request.user})
    elif request.method == "POST":
        email = request.user
        honorific = request.POST.get("honorific")
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        birthyear = request.POST.get("birthyear")
        affiliation = request.POST.get("affiliation")
        countryofaffiliation = request.POST.get("countryofaffiliation")
        countryCode = request.POST.get("countryCode")
        contact = request.POST.get("contact")
        WAcountryCode = request.POST.get("WAcountryCode")
        WAcontact = request.POST.get("WAcontact")
        num_papers = request.POST.get("num_papers")
        paper1_id = request.POST.get("paper1_id")
        paper2_id = request.POST.get("paper2_id")
        category = request.POST.get("category")
        num_people = request.POST.get("num_people")
        is_ishmt_member = request.POST.get("is_ishmt_member")
        ishmt_id = request.POST.get("ishmt_id")
        ishmt_id_file = request.FILES.get("ishmt_id_file")

        print(email, honorific, fullname, gender, birthyear, affiliation,countryofaffiliation, countryCode, contact, WAcountryCode, WAcontact, num_papers, paper1_id, paper2_id, category, num_people, is_ishmt_member, ishmt_id, ishmt_id_file)

        participant = Participant.objects.create(email=email,honorific=honorific,gender=gender,full_name=fullname,birth_year=birthyear,affiliation=affiliation,country_of_affiliation=countryofaffiliation,country_code=countryCode,contact_number=contact,whatsapp_country_code=WAcountryCode,whatsapp_contact_number=WAcontact,num_papers=num_papers,paper1_id=paper1_id,paper2_id=paper2_id,category=category,num_accompanying_people=num_people,is_ishmt_member=is_ishmt_member,ishmt_id=ishmt_id,ishmt_id_file=ishmt_id_file)

        participant.save()
        
        return HttpResponse("Participant Details")

def payment_details(request):
    return render(request,"payment-details.html")