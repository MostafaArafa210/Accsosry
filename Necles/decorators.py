from django.shortcuts import redirect
#-----------------------------------
# Check If User LogIn Or No
def notloguser(view_func):
    def wrapper_func(request, *args ,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        elif request.user.is_authenticated == None:
            return redirect('login')
        else:
            return view_func(request, *args ,**kwargs)
    return  wrapper_func
#-------------------------------------

#-------------------------------------
# Check If User In Groups OR No
def alloweduser(allowegroups=[]):
    def decorators(view_func):
        def wrapper_func(request, *args , **kwargs):
            group = None
            if request.user.groups.exists():
                  group = request.user.groups.all()[0].name
            if group in allowegroups:
                  return view_func(request, *args, **kwargs)
            else:
                    return redirect('profile')
        return wrapper_func
    return decorators
#-------------------------------------





# ------------------------------------
# Check If Admin Or Not Admin
def ForAdminOnly(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
               group = request.user.groups.all()[0].name
            if group == 'admin':
                return view_func(request, *args, **kwargs)
            if group == 'customer':
                return redirect('profile')
        return wrapper_func
# --------------------------------------
