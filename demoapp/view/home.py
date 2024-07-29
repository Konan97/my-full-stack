from datetime import datetime
from django.shortcuts import render

def home(request):
    time = datetime.today()
    path = request.path
    method = request.method
    content = '''
    <center><h2>Http Request Response</h2>
    <p>time: {}</p>
    <p>path: " {}</p>
    <p>method: {}</p></center>
    '''.format(time, path, method)
    about_content = {'time': time, 'path': path, 'method': method}
    return render(request, 'index.html', {'content': about_content})