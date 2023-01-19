from django.urls import path
import  electronics.views as views

urlpatterns = [
        path("all_links", views.NetworkListView.as_view()),
]

