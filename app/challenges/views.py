from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


challenges = {
    "january": "january challenges",
    "february": "february challenges",
    "march": "march challenges",
    "april":  "april challenges",
    "may": "may challenges",
    "june": "june challenges",
    "july": "july challenges",
    "august": "august challenges",
    "september": "september challenges",
    "october": "october challenges",
    "november": "november challenges",
    "december": None
}

def all_month_challenges(request):
    return render(request, "challenges/index.html", {
        "months": list(challenges.keys())
    })

def monthly_challenges_by_number(request, month):
    all_months = list(challenges.keys())
    if month > 12 or month <= 0:
        return HttpResponseNotFound("No such month is found")
    month_name = all_months[month - 1]
    redirect_url = reverse("challenges", args=[month_name])
    return HttpResponseRedirect(redirect_url)

def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month': month
        })
    except:
        raise Http404()

