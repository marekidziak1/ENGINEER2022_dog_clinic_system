from django.shortcuts import redirect
from django.contrib import messages
def doctor_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            for group in request.user.groups.all():
                if group.name == 'doctor':
                    return view_func(request, *args, **kwargs)  
        messages.info(request,'You are not authorized')
        return redirect('user-page')
    return wrapper_func		

def allowed_users(allowed_roles=None):
    if allowed_roles == None:
        allowed_roles= []
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                for group in request.user.groups.all():
                    if group.name in allowed_roles:
                        return view_func(request, *args, **kwargs)
            messages.info(request,'You are not authorized')
            return redirect('home')
        return wrapper_func
    return decorator