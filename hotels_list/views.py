from django.shortcuts import render, get_object_or_404
from hotels_list.models import Hotel, Comments
from hotels_list.forms import CommentForm

def hotels_list_list(request):
    """Вывод всех отелей
    """
    hotels = Hotel.objects.all()

    return render(request, "hotels_list/hotels_list_list.html", {"hotels_list": hotels})

def hotel_list_single(request, pk):
    """Вывод полного списка отелей
    """
    hotel = get_object_or_404(Hotel, id=pk)
    if request.method == "POST"
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
    else:

    comment = Comments.objects.filter(hotel=pk)
    form = CommentForm()
    return render(request, "hotels_list/hotel_list_single.html",
                  {"hotel_list": hotel,
                   "comments": comment,
                   "form": form})
