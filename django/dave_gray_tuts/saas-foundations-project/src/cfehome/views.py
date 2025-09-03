from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisits

this_dir=pathlib.Path(__file__).resolve().parent

def home_page_view(request):
    qs=PageVisits.objects.all()
    page_qs=PageVisits.objects.filter(path=request.path)
    my_title="My Old Page"
    my_context={
        'page_title':my_title,
        'page_visits_count':page_qs.count(),
        'total_visit_count':qs.count()
    }
    PageVisits.objects.create(path=request.path)
    return render(request, "home.html",my_context)

def old_home_page_view(request):
    # print(this_dir)
    # html_file_path=this_dir/"base.html"
    # html_=html_file_path.read_text()
    my_title="My Old Page"
    my_context={
        'page_title':my_title
    }
    html_="""
    <!DOCTYPE html>
<html lang="en">
<body>
    <h1>{page_title} is here</h1>
</body>

</html>
""".format(**my_context)
    return HttpResponse(html_)
