from django.shortcuts import render
from django.http import HttpResponse
from .models import Software


def index_view(request):
    all_software = Software.objects.all()
    context = {'all_software': all_software}
    return render(request, 'rdp/index.html', context=context)

def download_view(request, software_name):
    software = Software.objects.filter(name=software_name).first()
    filename = software.file.name.split('/')[-1]
    response = HttpResponse(software.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response