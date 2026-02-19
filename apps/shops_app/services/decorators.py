from django.shortcuts import redirect
from apps.shops_app.models import User


def login_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id')

        if not user_id:
            return redirect(f'/login/?next={request.path}')

        try:
            request.my_user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return redirect(f'/login/?next={request.path}')

        return view_func(request, *args, **kwargs)

    return wrapper

def logout_def(request):
    request.session.flush()
