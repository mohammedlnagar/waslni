from django.shortcuts import render

# Create your views here.
def viewReferral(request):
    return render(request, 'referrals/referral.html')