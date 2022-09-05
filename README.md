# Python Invoice Generator

<hr>

### Run without build
    ./invoice-generator.py SELLER CLIENT INVOICE_TYPE
    ./invoice-generator.py me SuperDuperClient e

### Build 
     docker build -t invoice_generator .     

### Run
    docker run -it -v $PWD:/app invoce-generator me SuperDuperClient e


### Logic
    1. Get data from remote json files
    2. Read template.xls 
    3. Parse information and write data
    4. Save new file with format "invoice_DATETIME.xls"     




<div align="center">
    <h2>Design</h2>
    <img src="design.png" width="400" height="500">
</div>

<br>

<div align="center">
     <h2>Example</h2>
    <img src="example.png">
</div>

<br>

<div align="center">
     <h2>Result</h2>
   <img src="invoice-generated.png" width="400" height="500">
</div>
    
