from django.urls import path
from challenges import views

urlpatterns = [
    path("", views.all_month_challenges, name="index"),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenges, name="challenges")
]
