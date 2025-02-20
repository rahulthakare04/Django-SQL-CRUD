from django.shortcuts import render
from . services import Filmoperations

# for URL http://127.0.0.1:8000/
def home(request):
    return render(request,"index.html",{'devloper':'rahul','company':'marvel project'})

def newfilm(request):
    return render(request,"NewFilm.html")

def addfilm(request):
    if request.method=="POST":
        try:
            nm=request.POST.get("filmname")
            yr=int(request.POST.get("relyear"))
            gn=request.POST.get("genre")
            ln=request.POST.get("language")
            rt=float(request.POST.get("imdbrating"))
            #print(f"{nm} {yr} {gn} {ln} {rt}")
            obj=Filmoperations()
            obj.addfilm(nm,yr,gn,ln,rt)

        except:
            print("error in data")
    return render(request,"FilmAdded.html")

def filmreport(request):
     obj=Filmoperations()
     data=obj.filmreport()
     return render(request,"FilmReport.html",{'filmdata':data})

def serchgen(request):
    
    if request.method=="POST":
        gn=request.POST.get("genere")
        obj=Filmoperations()
        dic=obj.searchongenere(gn)
        return render(request,"SearchResultGenere.html",dic)

def searchlang(request):
    return render(request,"searchonlanguage.html")

def searchonlanguage(request,lang):
    
    obj=Filmoperations()
    dic=obj.searchonlang(lang)
    return render(request,"ShowLangResult.html",dic,)

def searchongenre(request):
    return render(request,"LinkSearchOnGenre.html")

def searchgenpara(request,genre):
    obj=Filmoperations()
    dic=obj.searchongenere(genre)
    return render(request,"LinkGenResult.html",dic)

def login(request):
    if request.method=='POST':
        uid=request.POST.get('userid')
        psw=request.POST.get('password')
        if uid=='rahul' and psw=="rahul@123":
            request.session['userid']=id
            request.session['password']=psw

            page="AdminHome.html"
        else:
            page="LoginFail.html" 
    return render(request,page)  

def changerating(request):
    return render(request,"ChangeRating.html")

def changeimdbrating(request):
    if request.method=="POST":
        rt=float(request.POST.get('imdbRating'))
        fid=int(request.POST.get('filmId'))
        obj=Filmoperations()
        pag=obj.changeimdbrating(rt,fid)
        
    return render(request,pag)

def deletefilm(request):
    return render(request,"DeleteFilmFrom.html")

def filmdelete(request):
    if request.method=="POST":
        fid=int(request.POST.get("filmId"))
        obj=Filmoperations()
        sat=obj.filmdelete(fid)

        id=request.session.get("userid","unknown")
    return render(request,"FilmDeleted.html",{"status":sat,"userid":id})

