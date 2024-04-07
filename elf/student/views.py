from django.shortcuts import render, redirect
from .models import Lost_Item, Found_Item
from .forms import FoundItemForm, LostItemForm
from .similar import query
from .score import score_calculator
from django.urls import reverse

def home(request):
    context = {}
    return render(request, 'index.html', context)

def max_index(points):
    max_num = 0
    index = 0 
    for i in range(len(points)):
        if points[i] > max_num:
            max_num = points[i]
            index = i
    return index

def lost(request):
    match_name = match_des = match_loc = match_date = match_item = ""

    if request.method == 'POST':
        lost_form = LostItemForm(request.POST, request.FILES)
        if lost_form.is_valid():
            item_name = request.POST.get('item_name')
            item_des = request.POST.get('item_description')
            loc = request.POST.get('location')

            all_items = Found_Item.objects.all()
            all_item_ids = [item.id for item in all_items]
            all_item_name = [item.name for item in all_items]
            all_item_des = [item.item_description for item in all_items]
            all_loc = [item.location for item in all_items]

            name_out = query({"inputs": {"source_sentence": item_name, "sentences": all_item_name}})
            des_out = query({"inputs": {"source_sentence": item_des, "sentences": all_item_des}})
            loc_out = query({"inputs": {"source_sentence": loc, "sentences": all_loc}})

            points = []
            for i in range(len(all_items)):
                points.append(score_calculator(name_out[i], des_out[i], loc_out[i])) 

            match_id = max_index(points)

            if match_id is not None:
                matched_item_id = all_item_ids[match_id]
                matched_item = Found_Item.objects.get(id=matched_item_id)
                match_name = matched_item.name
                match_item = matched_item.item_name
                match_des = matched_item.item_description
                match_loc = matched_item.location
                match_date = matched_item.date

            else:
                match_name = match_des = match_loc = match_date = ""

            lost_item = lost_form.save(commit=False)
            lost_item.status = 'not_received'
            lost_item.save()
            return redirect(reverse('dashboard') + '?data=' + ','.join(map(str, points)))
        else:
            print(lost_form.errors)
    else:
        lost_form = LostItemForm()

    context = {
        'lost_form': lost_form,
        'name': match_name,
        'item': match_item,
        'des': match_des,
        'loc': match_loc,
        'date': match_date,
    }
    return render(request, 'lost.html', context)

def found(request):
    if request.method == 'POST':
        found_form = FoundItemForm(request.POST, request.FILES)
        if found_form.is_valid():
            found_item = found_form.save(commit=False)
            found_item.status = 'not_received'
            found_item.save()
            return redirect('home')
        else:
            print(found_form.errors)
    else:
        found_form = FoundItemForm()
    
    context = {'found_form': found_form}
    return render(request, 'found.html', context)

def about(request):
    return render(request, 'aboutUs.html')

def contact(request):
    return render(request, 'contactUs.html')

def student_dashboard(request):
    data = request.GET.get('data')
    points = []
    match_items = []
    print(data)

    

    if data:
        float_points = list(map(float, data.split(',')))
    match_id = max_index(float_points)
    

    all_items = Found_Item.objects.all()
    all_item_ids = [item.id for item in all_items]

    if len(points) >= 5:
        indexed_numbers = list(enumerate(points))
        sorted_numbers = sorted(indexed_numbers, key=lambda x: x[1], reverse=True)
        top_5_indices = [index for index, _ in sorted_numbers[:5]]  
        print(top_5_indices)

        if top_5_indices is not None:
            
            matched_item = Found_Item.objects.get(id=all_item_ids[match_id])
            match_items.append({
                'name': matched_item.name,
                'enrol': matched_item.enrollment_no,
                'phone': matched_item.phone_no,
                'item': matched_item.item_name,
                'des': matched_item.item_description,
                'loc': matched_item.location,
                'date': matched_item.date,
                'status': matched_item.status,
                'img': matched_item.imageURL
            })
    else:
        if points is not None:
            for i in points:
                matched_item = Found_Item.objects.get(id=all_item_ids[i])
                match_items.append({
                    'name': matched_item.name,
                    'enrol': matched_item.enrollment_no,
                    'phone': matched_item.phone_no,
                    'item': matched_item.item_name,
                    'des': matched_item.item_description,
                    'loc': matched_item.location,
                    'date': matched_item.date,
                    'status': matched_item.status,
                    'img': matched_item.imageURL
                })

    context = {
        'points': points,
        'match_items': match_items,
    }
    return render(request, 'dashboard.html', context)


def logged_in(request):
    return render(request, 'logged_home.html')
