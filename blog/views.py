from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Article,Reporter,Comment,Contact
from .forms import CommentForm,UserProfileForm,UserForm
import datetime

# Create your views here.
#Below view index is mail page which displays the latest 10 Article.
#-pub_date will will sort by latest and without "-" will arrange in
#ascending order.


def index(request):

    days = timezone.now() - datetime.timedelta(days=15)
    articles = Article.objects.all().order_by('-pub_date')[0:10]
    return render(request , 'blog/index.html', {'articles':articles})

#Below is details of each article displayed on main page.
#article_id is the primary key of the article .
#int is used in int(article_id) since http post contais string.

#@login_required
def article_detail(request,article_id):
    context = RequestContext(request)
    '''
    if request.method == 'POST':
        print "yes"
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print True
            comment_by_user = comment_form.cleaned_data['comment_by_user']
            print comment_by_user

            #creating an object for the given article_id to associate with
            #the incoming comment.

            article = Article.objects.get(pk=int(article_id))
            comment_to_save = Comment(comment=comment_by_user,
                                     article=article)
            comment_to_save.save()

            return  HttpResponseRedirect((reverse('article_detail',args=(article_id))))
    else:
        comment_form = CommentForm()'''
    try:
        articleData = Article.objects.get(pk=int(article_id))
    except Article.DoesNotExist:
        raise Http404("Article does not exists")
    commentsByUser = articleData.comment_set.all()
    comment_form = CommentForm
    return render(request,'blog/article_detail.html',
                  {'articleData':articleData,'commentsByUser':commentsByUser,
                   'comment_form':comment_form},context)



#Below comment method can also be used for comment.
@login_required
def comment(request,article_id):
    context = RequestContext(request)
    if request.method == 'POST':
        print "yes"
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print True
            comment_by_user = comment_form.cleaned_data['comment_by_user']
            print comment_by_user

            #creating an object for the given article_id to associate with
            #the incoming comment.

            article = Article.objects.get(pk=int(article_id))
            comment_to_save = Comment(comment=comment_by_user,
                                      article=article)
            comment_to_save.save()

            return HttpResponseRedirect((reverse('article_detail', args=(article_id))))
    else:
        comment_form = CommentForm()
    try:
        articleData = Article.objects.get(pk=int(article_id))
    except Article.DoesNotExist:
        raise Http404("Article does not exists")
    commentsByUser = articleData.comment_set.all()
    comment_form = CommentForm
    return render(request, 'blog/article_detail.html',
                  {'articleData': articleData, 'commentsByUser': commentsByUser,
                   'comment_form': comment_form}, context)

#End of comment method------------------------------------






def year_archive(request,year):
    context = RequestContext(request)
    year=year
    try:
        article_list = Article.objects.filter(pub_date__year=year)
    except Article.DoesNotExist:
        raise Http404("Article does not Exists")
    context = {'year':year, 'article_list':article_list}
    return render(request, 'blog/year_archive.html',context)

def month_archive(request,year,month):

    month_article = Article.objects.filter(pub_date__year=year).filter(pub_date__month=month)
    context = {'year':year,'month':month,'month_article':month_article}
    return render(request,'blog/month_archive.html',context)


def contact(request):

    contact_details = Contact.objects.all()
    return render(request,'blog/contact.html',
                  {'contact_details':contact_details})
#------------------------------------------------------------------
#Login page
#-------------------------------------------------------------------
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request:
                profile.picture = request.POST['picture']
            profile.save()

            registered = True
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'blog/register.html',
              {'user_form':user_form,'profile_form':profile_form,
               'registered':registered},context)
#--------------------------------
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/blog/')
        else:
            print("Wrong username or password {0} , {1}".format(username,password))
            return HttpResponse("wrong username or password")
    else:
        return render(request,'blog/user_login.html',{},context)

#----------------------------------------------------------------
#logout view
#---------------------------------------------------------------
@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/blog/')








