from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patron_password_app.forms import SearchForm, EditForm, PatronForm, GoogleForm, YahooForm, HotmailForm, OtherForm
from patron_password_app.models import Patron, GoogleAccount, YahooAccount, HotmailAccount, OtherAccount

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from array import *

# Create your views here.
@login_required
def patron_delete(request, patron_number):
    patron = Patron.objects.get(pk=patron_number)
    patron.delete()
    return HttpResponseRedirect(reverse('patron_password_app:search'))

@login_required
def search(request):
    searchform = SearchForm()
    searchresults = None
    if request.method == 'POST':
        searchform = SearchForm(data=request.POST)

        if searchform.is_valid():
            fname = searchform.cleaned_data['firstname']
            lname = searchform.cleaned_data['lastname']
            cardnumber = searchform.cleaned_data['cardnumber']

            if fname:
                fname=stripit(fname)
            if lname:
                lname=stripit(lname)
            if cardnumber:
                cardnumber=stripit(cardnumber)

            if fname != "" or lname != "" or cardnumber != "":
                searchresults = [patron for patron in Patron.objects.all()
                                if fname == patron.first_name or lname == patron.last_name
                                or cardnumber == patron.library_card_number]
            else:
                searchresults = Patron.objects.all().order_by('pk').reverse()
    else:
        searchresults = Patron.objects.all().order_by('pk').reverse()

    return render(request, 'patron_password_app/search.html', {'searchform':searchform, 'searchresults':searchresults})

@login_required
def patron_view(request, patron_number):
    patron = Patron.objects.get(pk=patron_number)
    try:
        ga = GoogleAccount.objects.get(pk=patron_number)
    except:
        ga = None
    try:
        ya = YahooAccount.objects.get(pk=patron_number)
    except:
        ya = None
    try:
        ha = HotmailAccount.objects.get(pk=patron_number)
    except:
        ha = None
    try:
        oa = OtherAccount.objects.get(pk=patron_number)
    except:
        oa = None

    context = {'patron': patron,
               'ga': ga,
               'ya': ya,
               'ha': ha,
               'oa': oa,
               'patron_number': patron_number}
    return render(request, 'patron_password_app/patronview.html', context)
@login_required
def patron_edit(request, patron_number):
    updated = False
    patron = Patron.objects.get(pk=patron_number)
    try:
        ga = GoogleAccount.objects.get(pk=patron_number)
    except:
        ga = None
    try:
        ya = YahooAccount.objects.get(pk=patron_number)
    except:
        ya = None
    try:
        ha = HotmailAccount.objects.get(pk=patron_number)
    except:
        ha = None
    try:
        oa = OtherAccount.objects.get(pk=patron_number)
    except:
        oa = None

    if request.method == "POST":
        edit_form =   EditForm(data=request.POST)

        if edit_form.is_valid():
            firstname = edit_form.cleaned_data['firstname']
            lastname = edit_form.cleaned_data['lastname']
            cardnumber = edit_form.cleaned_data['cardnumber']
            phonenumber = edit_form.cleaned_data['phonenumber']
            gusername = edit_form.cleaned_data['gusername']
            gpassword = edit_form.cleaned_data['gpassword']
            yusername = edit_form.cleaned_data['yusername']
            ypassword = edit_form.cleaned_data['ypassword']
            husername = edit_form.cleaned_data['husername']
            hpassword = edit_form.cleaned_data['hpassword']
            oservice = edit_form.cleaned_data['oservice']
            ousername = edit_form.cleaned_data['ousername']
            opassword = edit_form.cleaned_data['opassword']
            patron.first_name = firstname
            patron.last_name = lastname
            patron.library_card_number = cardnumber
            patron.phone_number = phonenumber
            patron.save()


            checkForUpdate(GoogleAccount, patron, ga, gusername, gpassword)
            checkForUpdate(YahooAccount, patron, ya, yusername, ypassword)
            checkForUpdate(HotmailAccount, patron, ha, husername, hpassword)
            checkForUpdate(OtherAccount, patron, oa, ousername, opassword, service = oservice)

            updated = True
            print('success!')
        else:
            print(edit_form.errors)
    else:
        populated_fields = {'firstname': patron.first_name,
                            'lastname': patron.last_name,
                            'cardnumber': patron.library_card_number,
                            'phonenumber': patron.phone_number,}

        if ga:
            populated_fields.update({'gusername': ga.username, 'gpassword': ga.password})
        if ya:
            populated_fields.update({'yusername': ya.username, 'ypassword': ya.password})
        if ha:
            populated_fields.update({'husername': ha.username, 'hpassword': ha.password})
        if oa:
            populated_fields.update({'oservice': oa.service, 'ousername': oa.username, 'opassword': oa.password})
        edit_form =   EditForm(populated_fields)

    context = {'editform': edit_form,'updated': updated, 'patron': patron, 'editpage': True}
    return render(request, 'patron_password_app/patronedit.html', context)
@login_required
def patron_add(request):
    if request.method == "POST":
        patron_form =   PatronForm(data=request.POST)
        google_form =   GoogleForm(data=request.POST)
        yahoo_form =    YahooForm(data=request.POST)
        hotmail_form =  HotmailForm(data=request.POST)
        other_form =    OtherForm(data=request.POST)

        if patron_form.is_valid() and google_form.is_valid() and yahoo_form.is_valid() and hotmail_form.is_valid() and other_form.is_valid():
            superDict = dict(request.POST.lists())
            patron_form = patron_form.save()

            if (superDict['username'][0] != "") or (superDict['password'][0] != ""):
                google_form = google_form.save(commit=False)
                google_form.patron= patron_form
                google_form.username = superDict['username'][0]
                google_form.password = superDict['password'][0]
                google_form.save()

            if (superDict['username'][1] != "") or (superDict['password'][1] != ""):
                yahoo_form = yahoo_form.save(commit=False)
                yahoo_form.patron= patron_form
                yahoo_form.username = superDict['username'][1]
                yahoo_form.password = superDict['password'][1]
                yahoo_form.save()

            if (superDict['username'][2] != "") or (superDict['password'][2] != ""):
                hotmail_form = hotmail_form.save(commit=False)
                hotmail_form.patron= patron_form
                hotmail_form.username = superDict['username'][2]
                hotmail_form.password = superDict['password'][2]
                hotmail_form.save()

            if (superDict['username'][3] != "") or (superDict['password'][3] != "") or (superDict['service'][0] != ""):
                other_form = other_form.save(commit=False)
                other_form.patron= patron_form
                other_form.username = superDict['service'][0]
                other_form.username = superDict['username'][3]
                other_form.password = superDict['password'][3]
                other_form.save()

            return HttpResponseRedirect(reverse('patron_password_app:search'))
        else:
            print('hello')
            print(patron_form.errors, google_form.errors, yahoo_form.errors, hotmail_form.errors, other_form.errors)

    else:
        patron_form     =       PatronForm()
        google_form     =       GoogleForm()
        yahoo_form      =       YahooForm()
        hotmail_form    =       HotmailForm()
        other_form      =       OtherForm()
    context = {'patron_form': patron_form,
               'google_form': google_form,
               'yahoo_form': yahoo_form,
               'hotmail_form': hotmail_form,
               'other_form': other_form,
               'editpage': True}
    return render(request, 'patron_password_app/patronadd.html', context)



def stripit(stringname):
    return stringname.replace(" ","")
def checkForUpdate(Model, patron, handler, username, password, **keyword_parameters):
    if ('service' in keyword_parameters):
        service = keyword_parameters['service']
        if handler:
            handler.username = username
            handler.password = password
            handler.service = service
            handler.save()
    else:
        if handler:
            handler.username = username
            handler.password = password
            handler.save()

    if (handler == None and username) or (handler == None and password):
        if ('service' in keyword_parameters):
            Model.objects.get_or_create(patron = patron, username = username, password = password, service = keyword_parameters['service'])
        else:
            Model.objects.get_or_create(patron = patron, username = username, password = password)
def multiFormHandler(patron_form, account_form):
    account_form = account_form.save(commit=False)
    account_form.patron= patron_form
    account_form.save()
