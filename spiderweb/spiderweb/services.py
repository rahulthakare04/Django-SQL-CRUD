import pymysql

class Filmoperations:
    def searchongenere(self,gn):
        dic={}
        con=pymysql.connect("your connection url ")       
        curs=con.cursor()
        curs.execute("select * from films where genre='%s'"%gn)
        data=curs.fetchall()
        dic['searchgenresult']=data
        dic['genre']=gn
        return dic

    def filmreport(self,):
        con=pymysql.connect("your connection url ")       
        curs=con.cursor()
        curs.execute("select * from films")
        data=curs.fetchall()
        con.close()
        return data

    def addfilm(self,nm,yr,gn,ln,rt):
        con=pymysql.connect("your connection url ")        
        curs=con.cursor()
        curs.execute("insert into films(filmname,relyear,genre,language,imdbrating) values ('%s',%d,'%s','%s',%.1f)"%(nm,yr,gn,ln,rt))
        con.commit()
        con.close()

    def searchonlang(self,lang):
         dic={}
         con=pymysql.connect("your connection url ")         
         curs=con.cursor()
         curs.execute("select * from films where language='%s'"%lang)
         data=curs.fetchall()
         dic['langresult']=data
         dic['language']=lang
         return dic

    def changeimdbrating(self,rt,fid):
        con=pymysql.connect("your connection url ")        
        curs=con.cursor()
        val=curs.execute("update films set imdbrating=%f where filmid=%d"%(rt,fid))
        con.commit()
        con.close()
        if val==1:
            page="RatingChangeDone.html"
        else:
            page="RatingChangeFail.html"
        return page

    def filmdelete(self,fid):
        con=pymysql.connect("your connection url ")          
        curs=con.cursor()
        cnt=curs.execute("delete from films where filmid=%d"%fid)
        con.commit()
        con.close()
        if cnt==1:
            sat="success"
        else:
            sat="fail"
        return sat
