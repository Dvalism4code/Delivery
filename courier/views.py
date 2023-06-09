from django.shortcuts import render, redirect
from .models import TrackingNumber
from .forms import FeedBackForm
from uuid import UUID
#from django.core.mail import send_mail
#from django.conf import settings


def home(request):
    return render(request, 'pages/base.html')


def about(request):
    return render(request, 'pages/about.html')



def is_valid_uuid(uuid_string):
    try:
        uuid_obj = UUID(uuid_string, version=4)
        return str(uuid_obj) == uuid_string
    except ValueError:
        return False


def tracker(request):
    if request.method == 'POST':
        tracker_code = request.POST.get('input')
        if not is_valid_uuid(tracker_code):
            # Handle the case when the tracker_code is not a valid UUID
            error_message = "Invalid UUID provided."
            return render(request, 'pages/error.html', {'error_message': error_message})

        tracking = TrackingNumber.objects.get(unique_id=tracker_code)
        context = {'tracking': tracking}
        return render(request, 'pages/track_details.html', context)

    else:
        return render(request, 'pages/base.html')


def tracking(request):
    if request.method == 'POST':
        tracker_code = request.POST.get('input')
        if not is_valid_uuid(tracker_code):
            # Handle the case when the tracker_code is not a valid UUID
            error_message = "Invalid UUID provided."
            return render(request, 'pages/error.html', {'error_message': error_message})

        tracking = TrackingNumber.objects.get(unique_id=tracker_code)
        context = {'tracking': tracking}
        return render(request, 'pages/track_details.html', context)

    else:
        return render(request, 'pages/tracking.html')


# Feedback form """

def feedback(request):
    if request.method == "POST":
        form = FeedBackForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            form.save()
            return redirect('success')
    else:
        form = FeedBackForm()
    return render(request, 'pages/contact.html', context={'form': form})


def feedsuccess(request):
    return render(request, 'pages/feed_success.html')