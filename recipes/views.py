from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Recipe


@csrf_exempt
def create_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not name or not description:
            return JsonResponse({'error': 'Name and description are required.'}, status=400)

        recipe = Recipe.objects.create(name=name, description=description, image=image)
        return JsonResponse({
            'id': recipe.id,
            'name': recipe.name,
            'description': recipe.description,
            'image': recipe.image.url if recipe.image else None
        }, status=201)

def list_recipes(request):
    recipes = list(Recipe.objects.values())
    return JsonResponse(recipes, safe=False)

@csrf_exempt
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        recipe.name = name
        recipe.description = description
        if image:
            recipe.image = image
        recipe.save()
        return JsonResponse({
            'id': recipe.id,
            'name': recipe.name,
            'description': recipe.description,
            'image_url': recipe.image.url if recipe.image else None
        })
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'DELETE':
        recipe.delete()
        return JsonResponse({'message': 'Recipe deleted successfully!'}, status=204)

@csrf_exempt
def find_recipe_by_id(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return JsonResponse({
        'id': recipe.id,
        'name': recipe.name,
        'description': recipe.description,
        'image': recipe.image.url if recipe.image else None
    })