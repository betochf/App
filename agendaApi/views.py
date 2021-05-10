from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import Contact
from .serializer import ContactSerializer
from .form import ContactForm
from django.core.paginator import Paginator

# Create your views here.
@api_view(['GET'])
def ContactList(request):
    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    paged = Paginator(serializer.data, 9)
    page_num = request.GET.get('page')
    page_obj = paged.get_page(page_num)

    return render(request, 'agendaApi/index.html', {'page_obj': page_obj, 'page_num': paged.num_pages})

@api_view(['GET'])
def ContactDelete(request,pk):
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact, many=False)
    contact.delete()
    return render(request, 'agendaApi/delete.html', {'contacts':serializer.data})   

@api_view(['GET'])
def ContactCreate(request):
    action= '/contacts/create/done'
    form = ContactForm()
    return render(request, 'agendaApi/form.html', {'form': form , 'action':action})


@api_view(['POST'])
def ContactCreatePOST(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('/contacts/')
    else:
        return render(request, 'agendaApi/error.html', {'errors':serializer.errors})

def ContactUpdate(request,pk):
    action='/contacts/update/'+pk+'/done'
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)
    return render(request, 'agendaApi/form.html', {'form': form , 'action':action})

@api_view(['POST'])
def ContactUpdatePOST(request,pk):
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(instance=contact,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('/contacts/')
    else:
        return render(request, 'agendaApi/error.html', {'errors':serializer.errors})
