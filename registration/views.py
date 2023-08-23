from django.shortcuts import redirect, render
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

        participant = Participant.objects.create(email=email,honorific=honorific,gender=gender,full_name=fullname,birth_year=birthyear,affiliation=affiliation,country_of_affiliation=countryofaffiliation,country_code=countryCode,contact_number=contact,whatsapp_country_code=WAcountryCode,whatsapp_contact_number=WAcontact,num_papers=num_papers,paper1_id=paper1_id,paper2_id=paper2_id,category=category,num_accompanying_people=num_people,is_ishmt_member=is_ishmt_member,ishmt_id=ishmt_id,ishmt_id_file=ishmt_id_file)

        participant.save()
        
        return redirect("payment-details")

def payment_details(request):
    if request.method == "GET":
        try:
            participant = Participant.objects.get(email=request.user)
        except:
            return HttpResponse("Participant Details not found")
        x = 'S'
        y = 'P'
        z = 'C'
        if participant.country_of_affiliation == "SAARC":
            x = 'S'
        elif participant.country_of_affiliation == "Non-SAARC":
            x = 'N'
        if participant.category == "Student":
            y = 'S'
        elif participant.category == "Faculty":
            y = 'F'
        elif participant.category == "Others":
            y = 'O'
        if participant.is_ishmt_member == "Yes":
            z = 'M'
        elif participant.is_ishmt_member == "No":
            z = 'N'

        p = x+y+z
        fee = "Rs. 0"
        if p == "SSM":
            fee = 6500*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*3800
            fee = str(fee) + " INR"
        elif p == "SSN":
            fee = 7200*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*3800
            fee = str(fee) + " INR"
        elif p == "SFM":
            fee = 8400*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*3800
            fee = str(fee) + " INR"
        elif p == "SFN":
            fee = 9600*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*3800
            fee = str(fee) + " INR"
        elif p == "SIM":
            fee = 11000*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*3800
            fee = str(fee) + " INR"
        elif p == "SIN":
            fee = 12100*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*3800
            fee = str(fee) + " INR"
        elif p == "NSN":
            fee = 200*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*180
            fee = str(fee) + " USD"
        elif p == "NFN":
            fee = 460*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*180
            fee = str(fee) + " USB"
        elif p == "NIN":
            fee = 550*( 1 + 0.25*(int(participant.num_papers) -1)) + int(participant.num_accompanying_people)*180
            fee = str(fee) + " USD"
        return render(request,"registration/payment-details.html",{"category":p,"fee":fee})
    elif request.method == "POST":
        try:
            receipt = request.FILES.get("receipt")
            referencenum = request.POST.get("referencenum")
            comments = request.POST.get("comments")
        except:
            pass
        print(receipt,referencenum,comments)
        return HttpResponse("Payment Details Submitted")