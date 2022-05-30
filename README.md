# Import-Fidelity-orders-report-to-Tradervue
It allows to import csv file from Fidelity orders report to Tradervue for futher analysis.<br>
<b>HOW TO DELETE a REF CELL in EXCEL spreadsheet WHEN THIS CELL CAUSING A PROBLEM CSV</b> <br>
This procedure shows that reference cell REF can be deleted if it stored in absolute values in memory like Const or Macro in C <br>
Select the cells you need to remove all references, then press Ctrl + C keys, keep these cells selected, right click and select Values under Paste Options section. See screenshot:<br>
![image](https://user-images.githubusercontent.com/1938390/169705426-857070a3-8255-4a06-a69e-e170d9a3f403.png) <br>
When call function or formula in excel reference to another cell to get result but then it cannot delete because its reference
this way allowing to delete reference cell after it has been capture as absolute value. In this case we attract the data
from cell called Order Time has a string AM or PM which causing error when parsing into TraderVue this way we can delete the cell after we are using it. <br>
=MINVALUE(left(N4, 11))   this cell reference to N4 to get result therefore it cannot be delete but if it stored as values
then the reference cell N4 can be deleted

To save pdf click pdf then download <br>
To save csv file<br>
    Go to the file you want to download.<br>
    Click it to view the contents within the GitHub UI.<br>
    In the top right, right click the Raw button.<br>
    Left click in middle of browser Save as...<br>

Input file using csv Output file accordingly <br>
Input file using Worksheet Output file csv since Tradervue only reads csv file format..<br>
Both file mentioned in the PDF file please read it for more details.<br>
