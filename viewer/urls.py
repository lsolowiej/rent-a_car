from django.urls import path

# from viewer.views import MoviesView, MovieCreateView, GenreCreateView, MovieUpdateView, MovieDeleteView, \
#     MovieDetailView, GenreListView, GenreUpdateView, HomeView
from viewer.views import CarsView, SingleCarView, CarCreateView, HomeView, CarDetailView, CarUpdateView, CarDeleteView

app_name = 'viewer'
urlpatterns = [

    path('', HomeView.as_view(), name="index"),
    path('cars/', CarsView.as_view(), name="cars"),
    path('<int:id>', SingleCarView.as_view(), name="single_car"),
    path('new/', CarCreateView.as_view(), name="create_car"),
    path('<int:pk>/', CarDetailView.as_view(), name="read_car"),
    path('<int:pk>/update/', CarUpdateView.as_view(), name="update_car"),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name="delete_car"),
    # path('genres/', GenreListView.as_view(), name="genres"),
    # path('genres/new/', GenreCreateView.as_view(), name="create_genre"),
    # path('genres/<int:pk>/update/', GenreUpdateView.as_view(), name="update_genre"),
]
