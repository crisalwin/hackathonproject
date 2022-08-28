from django.shortcuts import render

from django.shortcuts import render
import openpyxl


# Create your views here.




def index(request):
    if "GET" == request.method:
        return render(request, 'excel.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()


        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:

                    row_data.append(str(cell.value))


            excel_data.append(row_data)


        for i in excel_data:
            global a
            if i[0] == ('ctc'):
                a=int(i[1])
        dict={'Basic Salary':[],'HRA':[],'Special Allowance':[],'Employer PF':[],'Employer ESI':[],'Base Salary':[],'Annual Short-Term Bonus':[],'Other Allowance (Internet)':[]}
        row=list()
        for i in excel_data:
            global bs
            if i[0]==('Basic Salary'):
                a1=int(i[1])
                p1=(a1*100)/a
                bs=(a*p1)/100
                dict['Basic Salary'].append(bs)
        for i in excel_data:
            global hra
            if i[0]==('HRA'):
                a2=int(i[1])
                p2=(a2*100)/a
                hra=(a*p2)/100
                dict['HRA'].append(hra)
        for i in excel_data:
            global sa
            if i[0]==('Special Allowance'):
                a3=int(i[1])
                p3=(a3*100)/a
                sa=(a*p3)/100
                dict['Special Allowance'].append(sa)
        for i in excel_data:
            global pf
            if i[0]==('Employer PF'):
                a4=int(i[1])
                p4=(a4*100)/a
                pf=(a*p4)/100
                dict['Employer PF'].append(pf)
        for i in excel_data:
            global esi
            if i[0]==('Employer ESI'):
                a5=int(i[1])
                p5=(a5*100)/a
                esi=(a*p5)/100
                dict['Employer ESI'].append(esi)
        total=esi + pf + sa + hra
        dict['Base Salary'].append(total)
        for i in excel_data:
            if i[0]==('Annual Short-Term Bonus'):
                a7=int(i[1])
                p7=(a7*100)/a
                astb=(a*p7)/100
                dict['Annual Short-Term Bonus'].append(astb)
        for i in excel_data:
            if i[0]==('Other Allowance (Internet)'):
                a8=int(i[1])
                p8=(a8*100)/a
                oa=(a*p8)/100
                dict['Other Allowance (Internet)'].append(oa)


        row.append(dict)
        mlist=row

        return render(request, 'excel.html', {"mlist":mlist})



# print(i[0], i[1], i[2])
                    # a = i[1]
                    #
                    # b = (float(a) * 47.3484) / 100
                    # c = (float(a) * 23.6742) / 100
                    # d = (float(a) * 21.6289) / 100
                    # e = (float(a) * 2.04545) / 100
                    # print('basic salary:', b, '\nHRA:', c, '\nSP:', d, '\nPF:', e)