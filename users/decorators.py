from django.shortcuts import redirect


def user_is_owner(func):
    def wrapper(request, username, *args, **kwargs):
        logged_user = request.user.username
        if logged_user != username:
            return redirect(f'/accounts/profile/{logged_user}')
        
        return func(request, username, *args, **kwargs)
    return wrapper
        
