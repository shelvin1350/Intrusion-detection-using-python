from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import MySQLdb
import datetime
from django.http import HttpResponseRedirect
import re
import csv
from django.db.models import Q, Count

from Cyberapp.models import ddos_dataset
con=MySQLdb.connect("localhost","root","","cyberspy_db")

c=con.cursor()

#`````````````````````````````````````` HOME  ````````````````````````````````

def Home(request):

    return render(request,"Home.html")

def Attacks(request):
    return render(request, "Attacks.html")

def Cyber_attacks(request):

    return render(request,"Cyber_attacks.html")


def Inbox_empty(request):

    return render(request,"Inbox_empty.html")
#`````````````````````````````````````` REGISTRATION PAGE ````````````````````````````````

def Registration(request):
   
    msg=""
    
    # if(request.session["uname"]==""):
    #     return HttpResponseRedirect("Home")

    if(request.POST):
        firstname=request.POST.get("fn")
        lastname=request.POST.get("ln")
        email=request.POST.get("e1")
        password=request.POST.get("pswd")
        cpswd=request.POST.get("cpswd")


        if(password==cpswd):
            
            s="insert into registernow (`firstname`,`lastname`,`email`,`password`) values('"+firstname+"','"+lastname+"','"+email+"','"+password+"')"
            c.execute(s)
            con.commit()
            
        else:
            msg="PASSWORD MISMATCH FOUND"

    return render(request,"Registration.html",{"data":msg})


    #`````````````````````````````````````` LOGIN PAGE ````````````````````````````````````````````````````````

def login(request):
    
    msg=""
    if(request.POST):

        email=request.POST.get("email")
        password=request.POST.get("pass")
        request.session["uname"]=email
        request.session["psw"]=password
        s="select count(*) from registernow where email='"+str(email)+"' and password='"+str(password)+"'"
        c.execute(s)
        data=c.fetchall()
        a=request.session["uname"]
        
        if(data[0][0]==1):
            print(a)
            msg=""
            return HttpResponseRedirect("/user_home")
        else:
            msg="MISTAKE FOUND"

    return render(request,"login.html",{"data":msg})  


#````````````````````````````````````````USER HOME PAGE ````````````````````````````````````````````````````````


def user_home(request):
    
    email=request.session["uname"]
    w="select * from registernow where email='"+str(email)+"'"
    c.execute(w)
    print (w)
    data=c.fetchall()
        
    return render(request,"user_home.html",{"data":data})     
  

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  PROFILE EDITING  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def user_edit_profile(request):

    msg=""
    if(request.session["uname"]==""):
        return HttpResponseRedirect("/Home")
    
    mail=request.session["uname"]
    pswd=request.session["psw"]
    s="select * from registernow where email='"+mail+"' and password='"+pswd+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"user_edit_profile.html",{"data":data})


def edit_fname(request):

    fname=request.GET.get("fname")
    id=request.GET.get("reg_id")
    firstname=request.POST.get("nfn")
    if(request.POST):

        w="update registernow set firstname='"+str(firstname)+"' where reg_id='"+str(id)+"'"
        print(w)
        c.execute(w)
        con.commit()
        data=c.fetchall()

        return HttpResponseRedirect("new_profile")

    return render(request,"edit_fname.html",{"fname":fname})

def edit_sname(request):

    sname=request.GET.get("sname")
    id=request.GET.get("id")
    lastname=request.POST.get("nln")
    if(request.POST):

        w="update registernow set lastname='"+str(lastname)+"' ,where reg_id='"+str(id)+"'"
        print(w)
        c.execute(w)
        con.commit()
        data=c.fetchall()

        return HttpResponseRedirect("new_profile")

    return render(request,"edit_sname.html",{"sname":sname})
    

def edit_email(request):

    mail=request.GET.get("mail")
    id=request.GET.get("id")
    email=request.POST.get("ne1")
    if(request.POST):

        w="update registernow set email='"+str(email)+"' where reg_id='"+str(id)+"'"
        print(w)
        c.execute(w)
        con.commit()
        data=c.fetchall()

        return HttpResponseRedirect("login")

    return render(request,"edit_email.html",{"mail":mail})

def edit_pswd(request):

    psw=request.GET.get("psw")
    id=request.GET.get("id")
    password=request.POST.get("npswd")
    if(request.POST):

        w="update registernow set password='"+str(password)+"' where reg_id='"+str(id)+"'"
        print(w)
        c.execute(w)
        con.commit()
        data=c.fetchall()

        return HttpResponseRedirect("login")


    return render(request,"edit_pswd.html",{"psw":psw})

def new_profile(request):

    msg=""
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
    
    mail=request.session["uname"]
    pswd=request.session["psw"]
    print(mail)
    s="select * from registernow where email='"+mail+"' and password='"+pswd+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"new_profile.html",{"data":data})


#`````````````````````` FILE DATA MINING ````````````````````````````

def threatlist(request):

    msg=""
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
    
    # mail=request.session["uname"]
    # pswd=request.session["psw"]
    # print(mail)
    fid=request.GET.get("file_id")
    ss="select count(*) from attack_table where file_id='"+fid+"' and attack_types<>'Unlabeled Data'"
    c.execute(ss)
    data=c.fetchall()
    if(data[0][0]==0):
       return HttpResponseRedirect("No_threats")
    else:
        s="select f.filename,a.attack_types,a.rank from attack_table a join filedata_table f on(a.file_id=f.file_id)where a.attack_types<>'Unlabeled Data' and a.file_id ='"+fid+"'"
        c.execute(s)
        data=c.fetchall()
        
       
        return render(request,"threatlist.html",{"data":data})


        #`````````````````````` FILE DATA MINING ````````````````````````````

def threat_findings(request):

    msg=""
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
    
    # mail=request.session["uname"]
    # pswd=request.session["psw"]
    # print(mail)
    fid=request.GET.get("file_id")
    ss="select count(*) from attack_table where file_id='"+fid+"' and attack_types<>'Unlabeled Data'"
    c.execute(ss)
    data=c.fetchall()
    if(data[0][0]==0):
       return HttpResponseRedirect("inbox_view")
    else:
        s="select f.filename,a.attack_types,a.rank from attack_table a join filedata_table f on(a.file_id=f.file_id)where a.attack_types<>'Unlabeled Data' and a.file_id ='"+fid+"'"
        c.execute(s)
        data=c.fetchall()
       
        return render(request,"threat_findings.html",{"data":data})
        
 #`````````````````````` FILE sharing ````````````````````````````

def file_sharing(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
    rank=0
    attack1 = []
    attack2, attack3, attack4, attack5, attack6, attack7, attack8, attack9 = [], [], [], [], [], [], [], []
    ans = ''
    txt = ''
    splt = ''
    email=request.session.get("uname")
    msg=""
    filetype=request.POST.get("file_type")
    if(request.POST):
        if(filetype=="image"):
            filename=request.POST.get("fname")
        else:
            with open('dataset.csv') as fd:
                reader=csv.reader(fd)
                interestingrows=[row for idx, row in enumerate(reader) if idx in (28,62)]
            
            for dd in interestingrows:
                filename=dd[1]
                splt = (re.findall(r"[\w']+", str(filename)))
            for f in splt:
            
                if f in ('IPid','FDDI','x25','rangingdistance'):
                    attack1.append(f)
                elif f in ('tcpchecksum','mtcp','controlflags','tcpoffset','tcpport'):
                    attack2.append(f)
                elif f in ('ICMPID','udptraffic','udpunicorn','datagramid','NTP','RIP','TFTP'):
                    attack3.append(f)
                elif f in ('GETID','POSTID','openBSD','appid','sessionid','transid','physicalid'):
                    attack4.append(f)
                elif f in ('SYN','ACK','synpacket','sycookies'):
                    attack5.append(f)
                elif f in ('serverattack','serverid','blockbankwidth'):
                    attack6.append(f)
                elif f in ('monlist','getmonlist','NTPserver'):
                    attack7.append(f)
                elif f in ('portid','FTPID','tryion','fragflag'):
                    attack8.append(f)
                elif f in ('malwareid','gethttpid','httpid'):
                    attack9.append(f)

            if len(attack1) > len(attack2) and len(attack1) > len(attack3) and len(attack1) > len(attack4) and len(
                    attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
                    attack1) > len(attack8) and len(attack1) > len(attack9):

                    ans = "Ip Fragment Attack"
                    rank=1
            elif len(attack2) > len(attack1) and len(attack2) > len(attack3) and len(attack2) > len(attack4) and len(
                    attack2) > len(attack5) and len(attack2) > len(attack6) and len(attack2) > len(attack7) and len(
                    attack2) > len(attack8) and len(attack2) > len(attack9):
                    ans = "TCP Based Attack"
                    rank=2
            elif len(attack3) > len(attack2) and len(attack3) > len(attack1) and len(attack3) > len(attack4) and len(
                    attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
                    attack1) > len(attack8) and len(attack1) > len(attack9):
                    ans = "UDP Based Attack"
                    rank=3
            elif len(attack4) > len(attack2) and len(attack4) > len(attack3) and len(attack4) > len(attack1) and len(
                    attack4) > len(attack5) and len(attack4) > len(attack6) and len(attack4) > len(attack7) and len(
                    attack4) > len(attack8) and len(attack4) > len(attack9):
                    ans = "Layer Based Attack"
                    rank=4
            elif len(attack5) > len(attack2) and len(attack5) > len(attack3) and len(attack5) > len(attack4) and len(
                    attack5) > len(attack1) and len(attack5) > len(attack6) and len(attack5) > len(attack7) and len(
                    attack5) > len(attack8) and len(attack5) > len(attack9):
                    ans = "SYN Floods Attack"
                    rank=5
            elif len(attack6) > len(attack2) and len(attack6) > len(attack3) and len(attack6) > len(attack4) and len(
                    attack6) > len(attack5) and len(attack6) > len(attack1) and len(attack6) > len(attack7) and len(
                    attack6) > len(attack8) and len(attack6) > len(attack9):
                    ans = "Slowloris"
                    rank=6
            elif len(attack7) > len(attack2) and len(attack7) > len(attack3) and len(attack7) > len(attack4) and len(
                    attack7) > len(attack5) and len(attack7) > len(attack6) and len(attack7) > len(attack1) and len(
                    attack7) > len(attack8) and len(attack7) > len(attack9):
                    ans = "NTP Amplification"
                    rank=7
            elif len(attack8) > len(attack2) and len(attack8) > len(attack3) and len(attack8) > len(attack4) and len(
                    attack8) > len(attack5) and len(attack8) > len(attack6) and len(attack8) > len(attack7) and len(
                    attack8) > len(attack1) and len(attack8) > len(attack9):
                    ans = "Ping of Death Attack"
                    rank=8
            elif len(attack9) > len(attack2) and len(attack9) > len(attack3) and len(attack9) > len(attack4) and len(
                    attack9) > len(attack5) and len(attack9) > len(attack6) and len(attack9) > len(attack7) and len(
                    attack9) > len(attack8) and len(attack9) > len(attack1):

                    ans = "HTTP Flood Attack"
                    rank=9

            else:

                ans = "Unlabeled Data"
            ddos_dataset.objects.create(ddos_data=txt,attack_result=ans)
            print("haiiiiiiiiiiiii")
            print(ddos_dataset)
            if(request.FILES.get('fname')):
                myfile=request.FILES['fname']
                fs=FileSystemStorage()
                filename=fs.save(myfile.name,myfile)
                fileurl=fs.url(filename)
            else:
                fileurl="/static/media/p1.png"
            filetype=request.POST.get("file_type")
            now = datetime.datetime.now()
            sender=request.POST.get("sender")
            receiver=request.POST.get("receiver")
            sending_purpose=request.POST.get("msg")
            s="insert into filedata_table(`filename`,`filetype`,`date`,`sender`,`receiver`,`sending_purpose`) values('"+str(filename)+"','"+str(filetype)+"','"+str(now)+"','"+str(sender)+"','"+str(receiver)+"','"+str(sending_purpose)+"')"
            c.execute(s)
            con.commit()
            qry="select max(file_id) from filedata_table"
            c.execute(qry)
            fileid=c.fetchone()
            insattack="insert into attack_table (`file_id`,`attack_types`,`date`,`rank`) values('"+str(fileid[0])+"','"+str(ans)+"','"+str(now)+"','"+str(rank)+"')"
            c.execute(insattack)
            con.commit()
            print(insattack)
            request.session["ans"]=ans

########################################################################################################        
########################################################################################################################################
        for f in splt:
            
            if f in ('IPid','FDDI','x25','rangingdistance'):
                attack1.append(f)
            elif f in ('tcpchecksum','mtcp','controlflags','tcpoffset','tcpport'):
                attack2.append(f)
            elif f in ('ICMPID','udptraffic','udpunicorn','datagramid','NTP','RIP','TFTP'):
                attack3.append(f)
            elif f in ('GETID','POSTID','openBSD','appid','sessionid','transid','physicalid'):
                attack4.append(f)
            elif f in ('SYN','ACK','synpacket','sycookies'):
                attack5.append(f)
            elif f in ('serverattack','serverid','blockbankwidth'):
                attack6.append(f)
            elif f in ('monlist','getmonlist','NTPserver'):
                attack7.append(f)
            elif f in ('portid','FTPID','tryion','fragflag'):
                attack8.append(f)
            elif f in ('malwareid','gethttpid','httpid'):
                attack9.append(f)

        if len(attack1) > len(attack2) and len(attack1) > len(attack3) and len(attack1) > len(attack4) and len(
                attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
                attack1) > len(attack8) and len(attack1) > len(attack9):

                ans = "Ip Fragment Attack"
                rank=1
        elif len(attack2) > len(attack1) and len(attack2) > len(attack3) and len(attack2) > len(attack4) and len(
                attack2) > len(attack5) and len(attack2) > len(attack6) and len(attack2) > len(attack7) and len(
                attack2) > len(attack8) and len(attack2) > len(attack9):
                ans = "TCP Based Attack"
                rank=2
        elif len(attack3) > len(attack2) and len(attack3) > len(attack1) and len(attack3) > len(attack4) and len(
                attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
                attack1) > len(attack8) and len(attack1) > len(attack9):
                ans = "UDP Based Attack"
                rank=3
        elif len(attack4) > len(attack2) and len(attack4) > len(attack3) and len(attack4) > len(attack1) and len(
                attack4) > len(attack5) and len(attack4) > len(attack6) and len(attack4) > len(attack7) and len(
                attack4) > len(attack8) and len(attack4) > len(attack9):
                ans = "Layer Based Attack"
                rank=4
        elif len(attack5) > len(attack2) and len(attack5) > len(attack3) and len(attack5) > len(attack4) and len(
                attack5) > len(attack1) and len(attack5) > len(attack6) and len(attack5) > len(attack7) and len(
                attack5) > len(attack8) and len(attack5) > len(attack9):
                ans = "SYN Floods Attack"
                rank=5
        elif len(attack6) > len(attack2) and len(attack6) > len(attack3) and len(attack6) > len(attack4) and len(
                attack6) > len(attack5) and len(attack6) > len(attack1) and len(attack6) > len(attack7) and len(
                attack6) > len(attack8) and len(attack6) > len(attack9):
                ans = "Slowloris"
                rank=6
        elif len(attack7) > len(attack2) and len(attack7) > len(attack3) and len(attack7) > len(attack4) and len(
                attack7) > len(attack5) and len(attack7) > len(attack6) and len(attack7) > len(attack1) and len(
                attack7) > len(attack8) and len(attack7) > len(attack9):
                ans = "NTP Amplification"
                rank=7
        elif len(attack8) > len(attack2) and len(attack8) > len(attack3) and len(attack8) > len(attack4) and len(
                attack8) > len(attack5) and len(attack8) > len(attack6) and len(attack8) > len(attack7) and len(
                attack8) > len(attack1) and len(attack8) > len(attack9):
                ans = "Ping of Death Attack"
                rank=8
        elif len(attack9) > len(attack2) and len(attack9) > len(attack3) and len(attack9) > len(attack4) and len(
                attack9) > len(attack5) and len(attack9) > len(attack6) and len(attack9) > len(attack7) and len(
                attack9) > len(attack8) and len(attack9) > len(attack1):

                ans = "HTTP Flood Attack"
                rank=9

        else:

            ans = "Unlabeled Data"
        ddos_dataset.objects.create(ddos_data=txt,attack_result=ans)
        print("haiiiiiiiiiiiii")
        print(ddos_dataset)
        if(request.FILES.get('fname')):
            myfile=request.FILES['fname']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
        else:
            fileurl="/static/media/p1.png"
        filetype=request.POST.get("file_type")
        now = datetime.datetime.now()
        sender=request.POST.get("sender")
        receiver=request.POST.get("receiver")
        sending_purpose=request.POST.get("msg")
        s="insert into filedata_table(`filename`,`filetype`,`date`,`sender`,`receiver`,`sending_purpose`) values('"+str(filename)+"','"+str(filetype)+"','"+str(now)+"','"+str(sender)+"','"+str(receiver)+"','"+str(sending_purpose)+"')"
        c.execute(s)
        con.commit()
        qry="select max(file_id) from filedata_table"
        c.execute(qry)
        fileid=c.fetchone()
        insattack="insert into attack_table (`file_id`,`attack_types`,`date`,`rank`) values('"+str(fileid[0])+"','"+str(ans)+"','"+str(now)+"','"+str(rank)+"')"
        c.execute(insattack)
        con.commit()
        print(insattack)
        request.session["ans"]=ans

        msg="Message sent successfully"

    return render(request,"file_sharing.html",{"data":msg,"uname":email,"msg":msg})

#```````````````````````````````````````` FILE CONTENTS ``````````````````````````````````


def filecontent(request):

    if(request.session["ans"]=="Unlabed Data"):
        return HttpResponseRedirect("/No_threats")

    else:

        return HttpResponseRedirect("/threatlist")

    return render(request,"filecontent.html")


#```````````````````````````````````````` NO THREATS IN FILE ``````````````````````````````````

def No_threats(request):

    return render(request,"No_threats.html")




#```````````````````````````````````````` ATTACK DEFINING ````````````````````````````````````


def attack_defining(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    fid=request.GET.get("fid")
    d1=request.GET.get("d1")
    s="select count(attack_id) as atkc,attack_types from attack_table group by attack_types"
    c.execute(s)
    data=c.fetchall()
    atkc1=data[0][0]
    typ1=data[0][1]
    atkc2=data[1][0]
    typ2=data[1][1]

    fid=request.GET.get("fid")
    d1=request.GET.get("d1")
    ss="select date,count(attack_types),attack_types from attack_table group by date"
    c.execute(ss)
    data1=c.fetchall()
    print(data1)
    da=data1[0][0]
    da1=data1[0][1]
    dc=data1[0][1]
    dc1=data1[1][1]
    da2=data1[1][0]
    dc2=data1[1][1]
    da3=data1[0][0]
    dc3=data1[0][1]
    da4=data1[1][0]
    dc4=data1[1][1]

    return render(request,"attack_defining.html",{"atkc1":atkc1,"typ1":typ1,"atkc2":atkc2,"typ2":typ2,"da":da,"da1":da1,"dc":dc,"dc1":dc1,"da":da2,"da1":da3,"dc2":dc2,"dc3":dc3})


#```````````````````````````````````````` FILE INBOX ````````````````````````````````````````````

def file_inbox(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
    

    email=request.session.get("uname")

    s="select f.filename,f.sender,f.date,f.filetype,f.sending_purpose,a.attack_types,a.rank,f.file_id from attack_table a join filedata_table f on(a.file_id=f.file_id)where f.receiver ='"+email+"'"
    c.execute(s)
    data=c.fetchall()

    if(data):

        return render(request,"file_inbox.html",{"data":data})
    else:

        return render(request,"Inbox_empty.html",{"data":data})

#```````````````````````````````````````` INBOX VIEW  ````````````````````````````````````````````    


def inbox_view(request):
    
    file_id=request.GET.get("file_id")
    print(file_id)
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    email=request.session.get("uname")
    s="select * from filedata_table where file_id='"+str(file_id)+"'"
    print(s)
    c.execute(s)
    data=c.fetchall()

    return render(request,"inbox_view.html",{"data":data})


#```````````````````````````````````````` FILE CONTENT  ````````````````````````````````````````````  


def filecontent(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("/Home")
        
    file_id=request.GET.get("file_id")
    s="select * from filedata_table where file_id='"+file_id+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"filecontent.html",{"data":data})

 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  MESSAGE REPLY  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def msg_reply(request):

    msg=""
    
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    username=request.session["uname"]
    n="select * from filedata_table where receiver='"+str(username)+"'"
    c.execute(n)
    dat=c.fetchall()


    frm=request.GET.get("receiver")
    fid=request.GET.get("sender")
    s="select * from filedata_table where receiver='"+str(username)+"' and file_id='"+str(fid)+"'"
    print(s)
    c.execute(s)
    data=c.fetchall()
    to=data[0][3]
    if(request.POST):
        
        if(request.FILES.get('fname')):
            myfile=request.FILES['fname']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
        else:
            fileurl="/static/media/p1.png"
            filetype=request.POST.get("file_type")

       
        File_type=request.POST.get("file_type")
        now = datetime.datetime.now()
        Message=request.POST.get("msg")

        s="insert into reply_table(`from`,`to`,`filename`,`file_type`,`date`,`message`) values('"+str(username)+"','"+str(to)+"','"+str(filename)+"','"+str(File_type)+"','"+str(now)+"','"+str(Message)+"')"
        c.execute(s)
        con.commit()
        
    return render(request,"msg_reply.html",{"data":msg,"dat":data,"frm":frm,"to":to})



#``````````````````````````````````````  FEEDBACK FORM ``````````````````````````````````````````


def feedback(request):
    
    msg=""
    
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
    
    Email=""
    if(request.POST):
        Name_of_user=request.POST.get("n1")
        Email=request.session.get("uname")
        Experience_with_app=request.POST.get("experience")
        Rating=request.POST.get("star")
        Comments=request.POST.get("msg")
        s="insert into feedback_table values('"+str(Name_of_user)+"','"+str(Email)+"','"+str(Experience_with_app)+"','"+str(Rating)+"','"+str(Comments)+"')"
        c.execute(s)
        con.commit()
        print(s)
        msg="FEEDBACK SUCCESSFULLY UPLOADED"


    return render(request,"feedback.html",{"data":msg,"uname":Email})

def viewfeedback(request):
    r="select * from feedback_table"
    c.execute(r)
    data=c.fetchall()
    
    return render(request,"viewfeedback.html",{"data":data})
#`````````````````````````````````` STAR RATING ``````````````````````````````````````````````````

def rat(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    data=request.GET.get["v"]
    request.session["rate"]=data



 
def add_data(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    attack1 = []
    attack2, attack3, attack4, attack5, attack6, attack7, attack8, attack9 = [], [], [], [], [], [], [], []
    ans = ''
    txt = ''
    splt = ''
    if request.method == "POST":
        txt = request.POST.get("name")

        splt = (re.findall(r"[\w']+", str(txt)))

    for f in splt:
        if f in ('IPid','FDDI','x25','rangingdistance'):
            attack1.append(f)
        elif f in ('tcpchecksum','mtcp','controlflags','tcpoffset','tcpport'):
            attack2.append(f)
        elif f in ('ICMPID','udptraffic','udpunicorn','datagramid','NTP','RIP','TFTP'):
            attack3.append(f)
        elif f in ('GETID','POSTID','openBSD','appid','sessionid','transid','physicalid'):
            attack4.append(f)
        elif f in ('SYN','ACK','synpacket','sycookies'):
            attack5.append(f)
        elif f in ('serverattack','serverid','blockbankwidth'):
            attack6.append(f)
        elif f in ('monlist','getmonlist','NTPserver'):
            attack7.append(f)
        elif f in ('portid','FTPID','tryion','fragflag'):
            attack8.append(f)
        elif f in ('malwareid','gethttpid','httpid'):
            attack9.append(f)

    if len(attack1) > len(attack2) and len(attack1) > len(attack3) and len(attack1) > len(attack4) and len(
            attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
            attack1) > len(attack8) and len(attack1) > len(attack9):
        ans = "Ip Fragment Attack"
    elif len(attack2) > len(attack1) and len(attack2) > len(attack3) and len(attack2) > len(attack4) and len(
            attack2) > len(attack5) and len(attack2) > len(attack6) and len(attack2) > len(attack7) and len(
            attack2) > len(attack8) and len(attack2) > len(attack9):
        ans = "TCP Based Attack"
    elif len(attack3) > len(attack2) and len(attack3) > len(attack1) and len(attack3) > len(attack4) and len(
            attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
            attack1) > len(attack8) and len(attack1) > len(attack9):
        ans = "UDP Based Attack"
    elif len(attack4) > len(attack2) and len(attack4) > len(attack3) and len(attack4) > len(attack1) and len(
            attack4) > len(attack5) and len(attack4) > len(attack6) and len(attack4) > len(attack7) and len(
            attack4) > len(attack8) and len(attack4) > len(attack9):
        ans = "Layer Based Attack"
    elif len(attack5) > len(attack2) and len(attack5) > len(attack3) and len(attack5) > len(attack4) and len(
            attack5) > len(attack1) and len(attack5) > len(attack6) and len(attack5) > len(attack7) and len(
            attack5) > len(attack8) and len(attack5) > len(attack9):
        ans = "SYN Floods Attack"
    elif len(attack6) > len(attack2) and len(attack6) > len(attack3) and len(attack6) > len(attack4) and len(
            attack6) > len(attack5) and len(attack6) > len(attack1) and len(attack6) > len(attack7) and len(
            attack6) > len(attack8) and len(attack6) > len(attack9):
        ans = "Slowloris"
    elif len(attack7) > len(attack2) and len(attack7) > len(attack3) and len(attack7) > len(attack4) and len(
            attack7) > len(attack5) and len(attack7) > len(attack6) and len(attack7) > len(attack1) and len(
            attack7) > len(attack8) and len(attack7) > len(attack9):
        ans = "NTP Amplification"
    elif len(attack8) > len(attack2) and len(attack8) > len(attack3) and len(attack8) > len(attack4) and len(
            attack8) > len(attack5) and len(attack8) > len(attack6) and len(attack8) > len(attack7) and len(
            attack8) > len(attack1) and len(attack8) > len(attack9):
        ans = "Ping of Death Attack"
    elif len(attack9) > len(attack2) and len(attack9) > len(attack3) and len(attack9) > len(attack4) and len(
            attack9) > len(attack5) and len(attack9) > len(attack6) and len(attack9) > len(attack7) and len(
            attack9) > len(attack8) and len(attack9) > len(attack1):
        ans = "HTTP Flood Attack"

    else:
        ans = "Unlabed Data"
    ddos_dataset.objects.create(ddos_data=txt,attack_result=ans)
    return render(request,'add_data.html')
def labeled_data(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    obj = ddos_dataset.objects.filter(Q(attack_result='Ip Fragment Attack')|Q ( attack_result='TCP Based Attack') |Q(attack_result='UDP Based Attack') |Q (attack_result='NTP Amplification') |Q (attack_result='HTTP Flood Attack')|Q (attack_result='Layer Based Attack')| Q(attack_result='Slowloris') |Q (attack_result='Ping of Death Attack') |Q (attack_result='SYN Floods Attack'))
    return render(request,'labeled_data.html',{'object':obj})

def unlabeled_data(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    obj = ddos_dataset.objects.filter(attack_result='Unlabed Data')
    return render(request,'unlabeled_data.html',{'object':obj})

def ddos_analysis(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    chart = ddos_dataset.objects.values('attack_result').annotate(dcount=Count('attack_result'))
    return render(request,'ddos_analysis.html',{'objects':chart})

def chart_page(request,chart_type):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")
        
    chart = ddos_dataset.objects.values('attack_result').annotate(dcount=Count('attack_result'))
    return render(request,'chart_page.html',{'chart_type':chart_type,'objects':chart})

def view_profile(request):
    return render(request,"view_profile.html")

def attacks(request):
    
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    return render(request,"attacks.html")

def notifications(request):

    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    return render(request,"notifications.html")

def head_tail(request):
    return render(request,"head_tail.html")

def head2_tail2(request):
    return render(request,"head2_tail2.html")

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return HttpResponseRedirect("/Home")

    #``````````````````````CYBER ATTACKS ````````````````````````````````````````````````````````````

def ddos(request):

    return render(request,"ddos.html")

def man_in_the_middle(request):

    return render(request,"man_in_the_middle.html")

def phishing(request):

    return render(request,"phishing.html")

def keylogger(request):

    return render(request,"phishing.html")

def exploit(request):

    return render(request,"phishing.html")

def adware(request):

    return render(request,"phishing.html")

def infected_usb(request):

    return render(request,"phishing.html")

def ransomeware(request):

    return render(request,"phishing.html")

def sms_sender(request):

    return render(request,"phishing.html")


#----------------------------------------------REPLY_VIEW-------------------------------------------------
def Reply_view(request):
    
    
    
    if(request.session["uname"]==""):
        return HttpResponseRedirect("Home")

    email=request.session.get("uname")
    s="select * from reply_table where `to`='"+email+"' "
    print(s)
    c.execute(s)
    data=c.fetchall()

    return render(request,"reply_view.html",{"data":data})

