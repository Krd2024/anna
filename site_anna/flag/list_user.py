from site_anna.models import User


def flag_user(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(pk=request.user.id)
            flag = 1 if user.on_the_list else 0
        except Exception as e:
            print(e)
    else:
        flag = 0

    return {"flag": flag}
