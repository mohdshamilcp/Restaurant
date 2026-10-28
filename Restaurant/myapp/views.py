from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Feedback, Reservation


def home(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "reservation":
            Reservation.objects.create(
                name=request.POST.get("name", "").strip(),
                phone=request.POST.get("phone", "").strip(),
                date=request.POST.get("date"),
                time=request.POST.get("time", ""),
            )
            messages.success(request, "Your reservation request was received.")
            anchor = "reservation"

        elif form_type == "feedback":
            Feedback.objects.create(
                feedback_type=request.POST.get("feedback_type", ""),
                rating=int(request.POST.get("rating", 0)),
                message=request.POST.get("message", "").strip(),
            )
            messages.success(request, "Thank you for your feedback.")
            anchor = "feedback"

        else:
            messages.error(request, "The form could not be identified.")
            anchor = "home"

        return redirect("f{reverse('home')}#{anchor}")

    return render(request, "home.html")