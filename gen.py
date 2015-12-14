import csv
import codecs
from nvd3 import multiBarChart, pieChart

with open('STC_2014_STC005_with_ann.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    states = []
    taxes = []
    total_taxes = []
    property_taxes = []
    sale_n_gross_taxes = []
    for row in reader:
        states.append(row['GEO.display-label'])
        taxes.append(row['T001'])
        property_taxes.append(row['T002'])
        sale_n_gross_taxes.append(row['T003'])
    
            
    states.pop(0)
    states.pop(0)

    taxes.pop(0)
    all_tax = taxes.pop(0)
    all = 0

    property_taxes.pop(0)
    property_taxes.pop(0)
    sale_n_gross_taxes.pop(0)
    sale_n_gross_taxes.pop(0)
    
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
    </head>
    <body>
    <center><h1>2014 Annual Survey of State Government Tax Collections</h1></center>
"""

chart = multiBarChart(width=1024, height=768, x_axis_format=None)
chart1 = pieChart(name="test", color_category='category20c', height=800, width=768)

chart1.add_serie(y=total_taxes, x=states, extra={"tooltip": {"y_start": "", "y_end": " %"}})
chart1.buildcontent()

chart.add_serie(name="test", y=total_taxes, x=states)
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
    sale_n_gross_taxes[i] = int(sale_n_gross_taxes[i])/1000000
chart2 = multiBarChart(width=800, height=400, x_axis_format=None)

chart2.add_serie(name="Property Taxes", y=property_taxes, x=states)
chart2.buildcontent()

file.write("<center>")
file.write(chart2.htmlcontent)
file.write("</center>")



file.close() 
