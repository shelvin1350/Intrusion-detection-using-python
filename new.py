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

#`