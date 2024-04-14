from django.shortcuts import render
def add(request):
    if request.method=="POST":
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        if request.POST.get("operation") == "sum":
            sum=int(num1)+int(num2)
            return render(request,"wadmin/add.html",{"result":sum})
        elif request.POST.get("operation") == "diff":
            diff=int(num1)-int(num2)
            return render(request,"wadmin/add.html",{"result":diff})
        elif request.POST.get("operation") == "mul":
            mul=int(num1)*int(num2)
            return render(request,"wadmin/add.html",{"result":mul})
        elif  request.POST.get("operation") == "div":
            div=int(num1)/int(num2)
            return render(request,"wadmin/add.html",{"result":div})
        else:
            return render(request,"wadmin/add.html")
    else:
        return render(request,"wadmin/add.html")

def largest(request):
     if request.method=="POST":
         num1=request.POST.get("number1")
         num2=request.POST.get("number2")
         num3=request.POST.get("number3") 
         if num1 > num2 and num1 > num3:
          return render(request,"wadmin/largest.html",{"result":num1})
         elif num2 > num1 and num2 > num3:
          return render(request,"wadmin/largest.html",{"result":num2})
         else:
            return render(request,"wadmin/largest.html",{"result":num3})
     else:
        return render(request,"wadmin/largest.html")
     

def mark(request):
      if request.method=="POST":
        name=request.POST.get("name")
        
        dept=request.POST.get("operation")
        mark1=request.POST.get("mark1")
        mark2=request.POST.get("mark2")
        mark3=request.POST.get("mark3")
        total=float(mark1) + float(mark2) + float(mark3)
        avg=total / 3 
        if (float(avg)>=90):
            Grade ="A+"
        elif(float(avg)<90 and float(avg) > 80):
            Grade = "A"
        elif(float(avg)<80 and float(avg)> 70):
            Grade = "B+"
        elif(float(avg)<70 and float(avg)> 60):
            Grade = "B"
        elif(float(avg)<60 and float(avg)>50):
            Grade = "C+"
        elif(float(avg)<50 and float(avg)>40):
            Grade = "C"
        else:
            Grade = "Failed"
        return render(request,"wadmin/mark.html",{"name":name,"dept":dept,"mark1":mark1,"mark2":mark2,"mark3":mark3,"avg":avg,"grade":Grade})
      else:
        return render(request,"wadmin/mark.html")

def salary(request):
    if request.method=="POST":
        fname=request.POST.get("txt_fname")
        lname=request.POST.get("txt_lname")
        gen=request.POST.get("rdo_gender")
        mar=request.POST.get("rdo_marital")
        dept=request.POST.get("ddl_dept")
        bs=request.POST.get("txt_salary")
        if (int(bs)>=10000):
            ta=(40/100)*int(bs)
            da=(35/100)*int(bs)
            hra=(30/100)*int(bs)
            lic=(25/100)*int(bs)
            pf=(20/100)*int(bs)
        elif (int(bs)>=5000 and int(bs)<10000):
            ta=(35/100)*int(bs)
            da=(30/100)*int(bs)
            hra=(25/100)*int(bs)
            lic=(20/100)*int(bs)
            pf=(15/100)*int(bs)
        else:
            ta=(30/100)*int(bs)
            da=(25/100)*int(bs)
            hra=(20/100)*int(bs)
            lic=(15/100)*int(bs)
            pf=(10/100)*int(bs)
        dec=int(lic)+int(pf)
        net=int(bs)+int(ta)+int(da)+int(hra)-(int(lic)+int(pf))
        return render(request,"wadmin/Salary.html",{"fname":fname,"lname":lname,"gen":gen,"mar":mar,"dept":dept,"bs":bs,"ta":ta,"da":da,"hra":hra,"lic":lic,"pf":pf,"dec":dec,"net":net})
    else:
        return render(request,"wadmin/salary.html")

# Create your views here.
