from MoinMoin.theme import rightsidebar

class Theme(rightsidebar.Theme):
    name = "europython"

def execute(request):
    return Theme(request)
