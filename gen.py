import csv
import codecs
from nvd3 import multiBarChart, pieChart

with open('STC_2014_STC005_with_ann.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    states = []
    taxes = []
    total_taxes = []
    property_taxes = []
    sale_general_taxes = []
    sale_selective_taxes = []
    sale_1 = []
    sale_2 = []
    sale_3 = []
    sale_4 = []
    sale_5 = []
    sale_6 = []
    sale_7 = []
    sale_8 = []
    license_1 = []
    license_2 = []
    license_3 = []
    license_4 = []
    license_5 = []
    license_6 = []
    license_7 = []
    license_8 = []
    license_9 = []
    income_1 = []
    income_2 = []
    other_1 = []
    other_2 = []
    other_3 = []
    other_4 = []
    
    for row in reader:
        states.append(row['GEO.display-label'])
        taxes.append(row['T001'])
        property_taxes.append(row['T002'])
        sale_general_taxes.append(row['T004'])
        sale_selective_taxes.append(row['T005'])
        sale_1.append(row['T006'])
        sale_2.append(row['T007'])
        sale_3.append(row['T008'])
        sale_4.append(row['T009'])
        sale_5.append(row['T010'])
        sale_6.append(row['T011'])
        sale_7.append(row['T012'])
        sale_8.append(row['T013'])
        license_1.append(row['T015'])
        license_2.append(row['T016'])
        license_3.append(row['T017'])
        license_4.append(row['T018'])
        license_5.append(row['T019'])
        license_6.append(row['T020'])
        license_7.append(row['T021'])
        license_8.append(row['T022'])
        license_9.append(row['T023'])
        income_1.append(row['T025'])
        income_2.append(row['T026'])
        other_1.append(row['T028'])
        other_2.append(row['T029'])
        other_3.append(row['T030'])
        other_4.append(row['T031'])
            
    states.pop(0)
    states.pop(0)

    taxes.pop(0)
    all_tax = taxes.pop(0)
    all = 0

    property_taxes.pop(0)
    property_taxes.pop(0)
    sale_general_taxes.pop(0)
    sale_general_taxes.pop(0)
    sale_selective_taxes.pop(0)
    sale_selective_taxes.pop(0)
    sale_1.pop(0)
    sale_1.pop(0)
    sale_2.pop(0)
    sale_2.pop(0)
    sale_3.pop(0)
    sale_3.pop(0)
    sale_4.pop(0)
    sale_4.pop(0)
    sale_5.pop(0)
    sale_5.pop(0)
    sale_6.pop(0)
    sale_6.pop(0)
    sale_7.pop(0)
    sale_7.pop(0)
    sale_8.pop(0)
    sale_8.pop(0)
    license_1.pop(0)
    license_1.pop(0)
    license_2.pop(0)
    license_2.pop(0)
    license_3.pop(0)
    license_3.pop(0)
    license_4.pop(0)
    license_4.pop(0)
    license_5.pop(0)
    license_5.pop(0)
    license_6.pop(0)
    license_6.pop(0)
    license_7.pop(0)
    license_7.pop(0)
    license_8.pop(0)
    license_8.pop(0)
    license_9.pop(0)
    license_9.pop(0)
    income_1.pop(0)
    income_1.pop(0)
    income_2.pop(0)
    income_2.pop(0)
    other_1.pop(0)
    other_1.pop(0)
    other_2.pop(0)
    other_2.pop(0)
    other_3.pop(0)
    other_3.pop(0)
    other_4.pop(0)
    other_4.pop(0)
    
    
    for data in taxes:
        total_taxes.append((int(data))/(int(all_tax))*100)
    
file = codecs.open("index.html","w", "utf-8")
headhtml = """<!DOCTYPE html>
<html lang="th">
    <head>
        <meta charset="utf-8" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.7.0/nv.d3.min.css" rel="stylesheet" />
        <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.7.0/nv.d3.min.js"></script>
        <title>2014 Annual Survey of State Government Tax Collections</title>
    </head>
    <body>
    <center><h1>2014 Annual Survey of State Government Tax Collections</h1></center>
"""

pattern = {"tooltip": {"y_start": "", "y_end": " Million USD"}}

chart = multiBarChart(width=1024, height=768, x_axis_format=None)
chart1 = pieChart(name="chart1", color_category='category20c', height=800, width=768)

chart1.add_serie(y=total_taxes, x=states, extra={"tooltip": {"y_start": "", "y_end": " %"}})
chart1.buildcontent()

chart.add_serie(name="chart", y=total_taxes, x=states)
chart.buildcontent()

file.write(headhtml)

file.write("<center><h2>All Tax Collections By States</h2></center>")
file.write("<center>")
file.write(chart1.htmlcontent)
file.write("</center>")
file.write("<center><h2>State Government Tax CollectionsTax Collections By Category</h2></center>")

for i in range(0 ,len(property_taxes)):
    if property_taxes[i] == 'X':
        property_taxes[i] = 0
    else:
        property_taxes[i] = int(property_taxes[i])/1000000

    if sale_general_taxes[i] == 'X':
        sale_general_taxes[i] = 0
    else:
        sale_general_taxes[i] = int(sale_general_taxes[i])/1000000

    if sale_selective_taxes[i] == 'X':
        sale_selective_taxes[i] = 0
    else:
        sale_selective_taxes[i] = int(sale_selective_taxes[i])/1000000

    if sale_1[i] == 'X':
        sale_1[i] = 0
    else:
        sale_1[i] = int(sale_1[i])/1000000

    if sale_2[i] == 'X':
        sale_2[i] = 0
    else:
        sale_2[i] = int(sale_2[i])/1000000

    if sale_3[i] == 'X':
        sale_3[i] = 0
    else:
        sale_3[i] = int(sale_3[i])/1000000

    if sale_4[i] == 'X':
        sale_4[i] = 0
    else:
        sale_4[i] = int(sale_4[i])/1000000

    if sale_5[i] == 'X':
        sale_5[i] = 0
    else:
        sale_5[i] = int(sale_5[i])/1000000

    if sale_6[i] == 'X':
        sale_6[i] = 0
    else:
        sale_6[i] = int(sale_6[i])/1000000

    if sale_7[i] == 'X':
        sale_7[i] = 0
    else:
        sale_7[i] = int(sale_7[i])/1000000

    if sale_8[i] == 'X':
        sale_8[i] = 0
    else:
        sale_8[i] = int(sale_8[i])/1000000

    if license_1[i] == 'X':
        license_1[i] = 0
    else:
        license_1[i] = int(license_1[i])/1000000

    if license_2[i] == 'X':
        license_2[i] = 0
    else:
        license_2[i] = int(license_2[i])/1000000

    if license_3[i] == 'X':
        license_3[i] = 0
    else:
        license_3[i] = int(license_3[i])/1000000

    if license_4[i] == 'X':
        license_4[i] = 0
    else:
        license_4[i] = int(license_4[i])/1000000

    if license_5[i] == 'X':
        license_5[i] = 0
    else:
        license_5[i] = int(license_5[i])/1000000

    if license_6[i] == 'X':
        license_6[i] = 0
    else:
        license_6[i] = int(license_6[i])/1000000

    if license_7[i] == 'X':
        license_7[i] = 0
    else:
        license_7[i] = int(license_7[i])/1000000

    if license_8[i] == 'X':
        license_8[i] = 0
    else:
        license_8[i] = int(license_8[i])/1000000

    if license_9[i] == 'X':
        license_9[i] = 0
    else:
        license_9[i] = int(license_9[i])/1000000

    if income_1[i] == 'X':
        income_1[i] = 0
    else:
        income_1[i] = int(income_1[i])/1000000

    if income_2[i] == 'X':
        income_2[i] = 0
    else:
        income_2[i] = int(income_2[i])/1000000

    if other_1[i] == 'X':
        other_1[i] = 0
    else:
        other_1[i] = int(other_1[i])/1000000

    if other_2[i] == 'X':
        other_2[i] = 0
    else:
        other_2[i] = int(other_2[i])/1000000

    if other_3[i] == 'X':
        other_3[i] = 0
    else:
        other_3[i] = int(other_3[i])/1000000

    if other_4[i] == 'X':
        other_4[i] = 0
    else:
        other_4[i] = int(other_4[i])/1000000
        
chart2 = multiBarChart(name="chart2", width=800, height=400, x_axis_format=None)

chart2.add_serie(name="Property Taxes", y=property_taxes, x=states, extra=pattern)
chart2.buildcontent()


chart3 = multiBarChart(name="chart3" ,width=800, height=400, x_axis_format=None)
chart3.add_serie(name="General", y=sale_general_taxes, x=states, extra=pattern)
chart3.add_serie(name="Selective", y=sale_selective_taxes, x=states, extra=pattern)
chart3.buildcontent()

chart4 = multiBarChart(name="chart4" ,width=1024, height=400, x_axis_format=None)
chart4.add_serie(name="Alcoholic Beverages Sales Tax", y=sale_1, x=states, extra=pattern)
chart4.add_serie(name="Amusements Sales Tax", y=sale_2, x=states, extra=pattern)
chart4.add_serie(name="Insurance Premiums Sales Tax", y=sale_3, x=states, extra=pattern)
chart4.add_serie(name="Motor Fuels Sales Tax", y=sale_4, x=states, extra=pattern)
chart4.add_serie(name="Pari-mutuels Sales Tax", y=sale_5, x=states, extra=pattern)
chart4.add_serie(name="Public Utilities Sales Tax", y=sale_6, x=states, extra=pattern)
chart4.add_serie(name="Tobacco Products Sales Tax", y=sale_7, x=states, extra=pattern)
chart4.add_serie(name="Other Selective Sales and Gross Receipts Taxes", y=sale_8, x=states, extra=pattern)
chart4.buildcontent()

chart5 = multiBarChart(name="chart5" ,width=1024, height=400, x_axis_format=None)
chart5.add_serie(name="Alcoholic Beverages License", y=license_1, x=states, extra=pattern)
chart5.add_serie(name="Amusements License", y=license_2, x=states, extra=pattern)
chart5.add_serie(name="Corporations in General License", y=license_3, x=states, extra=pattern)
chart5.add_serie(name="Hunting and Fishing License", y=license_4, x=states, extra=pattern)
chart5.add_serie(name="Motor Vehicle License", y=license_5, x=states, extra=pattern)
chart5.add_serie(name="Motor Vehicle Operators License", y=license_6, x=states, extra=pattern)
chart5.add_serie(name="Public Utilities License", y=license_7, x=states, extra=pattern)
chart5.add_serie(name="Occupation and Business License, NEC", y=license_8, x=states, extra=pattern)
chart5.add_serie(name="Other License Taxes", y=license_9, x=states, extra=pattern)
chart5.buildcontent()

chart6 = multiBarChart(name="chart6" ,width=800, height=400, x_axis_format=None)
chart6.add_serie(name="Individual Income Taxes", y=income_1, x=states, extra=pattern)
chart6.add_serie(name="Corporation Net Income Taxes", y=income_2, x=states, extra=pattern)
chart6.buildcontent()

chart7 = multiBarChart(name="chart7" ,width=1024, height=400, x_axis_format=None)
chart7.add_serie(name="Death and Gift Taxes", y=other_1, x=states, extra=pattern)
chart7.add_serie(name="Documentary and Stock Transfer Taxes", y=other_2, x=states, extra=pattern)
chart7.add_serie(name="Severance Taxes", y=other_3, x=states, extra=pattern)
chart7.add_serie(name="Taxes, NEC", y=other_4, x=states, extra=pattern)
chart7.buildcontent()


file.write("<center><h2>Property Taxes</h2></center>")
file.write("<center>")
file.write(chart2.htmlcontent)
file.write("</center>")

file.write("<center><h2>Sales and Gross Receipts Taxes</h2></center>")
file.write("<center>")
file.write(chart3.htmlcontent)
file.write("</center>")

file.write("<center><h2>Selective Sales and Gross Receipts Taxes</h2></center>")
file.write("<center>")
file.write(chart4.htmlcontent)
file.write("</center>")

file.write("<center><h2>License Taxes</h2></center>")
file.write("<center>")
file.write(chart5.htmlcontent)
file.write("</center>")

file.write("<center><h2>Income Taxes</h2></center>")
file.write("<center>")
file.write(chart6.htmlcontent)
file.write("</center>")

file.write("<center><h2>Other Taxes</h2></center>")
file.write("<center>")
file.write(chart7.htmlcontent)
file.write("</center>")

file.write("<center>")
file.write("<p>PSIT Project</p>")
file.write("<p>Chsysnon Nikornpornudom 57070024</p>")
file.write("<p>Sirawich Phonsukkarn 57070131</p>")
file.write("</center>")

file.close() 
