from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from recipes import views

urlpatterns = [
    path('recipes/', views.list_recipes),
    path('recipes/create/', views.create_recipe),
    path('recipes/<int:recipe_id>/', views.find_recipe_by_id, name='find_recipe_by_id'),
    path('recipes/update/<int:recipe_id>/', views.update_recipe),
    path('recipes/delete/<int:recipe_id>/', views.delete_recipe),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

