from django.shortcuts import render

from documentation.models import Document
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def documents(request):
    documents = Document.objects.all()
    return render(request, 'documentation.html', {'documents': documents})
