from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

# リクエストオブジェクトの中にはメソッドに関する情報も入ってきている
def signupfunc(request):
    if request =='POST':
        print('this is post method')
    else:
        print('this is not post method')
    
    # POSTされたデータの中のどのデータを持ってくるか、ここではusername
    # このusernameはsignup.htmlのname='username'でどのフォームか指定している
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = User.objects.create_user(username, '', password)
        print(user)

    # クラスベースドビューのtempletenameとmodelsみたいなもの
    return render(request, 'signup.html', {'some':100})