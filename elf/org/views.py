from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from student.forms import FoundItemForm
from student.models import Found_Item, Lost_Item
from django.shortcuts import HttpResponse


def not_received_items(request):
    not_received_items = Found_Item.objects.filter(status='not_received')  # Use consistent status name
    return render(request, 'listFound.html', {'not_received_items': not_received_items})

def not_found_items(request):
    query = request.GET.get('query')
    if query:
        not_found_items = Lost_Item.objects.filter(item_name__icontains=query) | Lost_Item.objects.filter(item_description__icontains=query)
    else:
        not_found_items = Lost_Item.objects.all()
    return render(request, 'listLost.html', {'not_found_items': not_found_items, 'query': query})

def search_items(request):
    query = request.GET.get('query')
    if query:
        found_items = Lost_Item.objects.filter(item_name__icontains=query) | Lost_Item.objects.filter(item_description__icontains=query)
    else:
        found_items = Lost_Item.objects.all()
    return render(request, 'organization_not_found_items.html', {'found_items': found_items})

def lost_toggle_status(request, lost_item_id):
    lost_item = get_object_or_404(Lost_Item, pk=lost_item_id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        if lost_item.status == 'not_received':
            lost_item.status = new_status
            lost_item.save()
            # Redirect to the same page with a success message
            return redirect('not_found_items')
        else:
            # Render the same page with an error message
            not_found_items = Lost_Item.objects.all()
            error_message = 'Item is already marked as received'
            return render(request, 'organization_not_found_items.html', {'not_found_items': not_found_items, 'query': None, 'error_message': error_message})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def found_toggle_status(request, found_item_id):
    found_item = get_object_or_404(Found_Item, pk=found_item_id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        if found_item.status == 'not_received':
            found_item.status = new_status
            found_item.save()
            # Redirect to the same page with a success message
            return redirect('not_received_items')
        else:
            # Render the same page with an error message
            not_received_items = Found_Item.objects.all()
            error_message = 'Item is already marked as received'
            return render(request, 'listFound.html', {'not_received_items': not_received_items, 'query': None, 'error_message': error_message})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def mark_as_complete(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Lost_Item, pk=item_id)
        item.completed = True
        item.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False}, status=405)
    

def completed_items(request):
    completed_items = Lost_Item.objects.filter(completed=True)  # Change status based on your implementation
    return render(request, 'completed_items.html', {'completed_items': completed_items})


def logged_in(request):
    return render(request, 'logged_home.html')