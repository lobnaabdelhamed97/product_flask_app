from __init__ import app
from getmethodview import GET
from postmethodview import POST
from deletemethodview import DELETE

app.add_url_rule('/',view_func=GET.as_view('gettest'))
app.add_url_rule('/',view_func=POST.as_view('posttest'))
app.add_url_rule('/',view_func=DELETE.as_view('deletetest'))
if __name__ == "__main__":
    app.run(debug=True)