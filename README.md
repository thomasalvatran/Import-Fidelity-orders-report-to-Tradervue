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
Github can only read csv file for xlsx you need to download and read from Excel <br>
Use template to create your own data: <br>
To create csv for Tradervue download either DailyReport_Template.xlsx (Worksheet) or simple csv DailyReport_Template.csv and replace the old columns Symbol, Status, Order time, Order Type, Trade Description, Quantity with new data. <br>
Templates have the 3 formulas/functions as follows:

<b>Price = VALUE(MID(B5,13,10)) </b>  /*attract the price in the string from 13 takes 10 characters for price replacing B5 to correct cell accordingly to your table */
Time = TIMEVALUE(LEFT(C5, 11) ) /* attract the time in the string start left takes 11 characters for time replacing C5 accordingly */
Quantity = IF((ISNUMBER(SEARCH("Sell",e3))),-1,1)*g3 /* return to quantity with sign operator for example -100 is sell 100, 100 is buy 100 */

Tradervue prefers csv file if using xlsx need to save as svc after creating data from formulas provided.
This is tradervue import 
![image](https://user-images.githubusercontent.com/1938390/171069856-57a01b66-6e1a-4117-b5d6-a4789a16081e.png)

