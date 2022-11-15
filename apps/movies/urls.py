from django.urls import path
from .views import MovieList, MovieFilter, MovieFilterCategory, MovieFilterDate, MovieFilterNew, \
    MovieFilterNameAsc, MovieFilterDateDesc, MovieFilterViewed

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movies'),
    path('movies/filter/', MovieFilter.as_view(), name='movies_filter'),
    path('movies/filter/category/', MovieFilterCategory.as_view(), name='movies_filter_category'),
    path('movies/filter/date/', MovieFilterDate.as_view(), name='movies_filter_date'),
    path('movies/filter/new/', MovieFilterNew.as_view(), name='movies_filter_new'),
    path('movies/filter/name_asc/', MovieFilterNameAsc.as_view(), name='movies_filter_name_asc'),
    path('movies/filter/date_desc/', MovieFilterDateDesc.as_view(), name='movies_filter_date_desc'),
    path('movies/filter/viewed/', MovieFilterViewed.as_view(), name='movies_filter_viewed'),

]
