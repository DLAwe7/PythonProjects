import openpyxl as xl
import CalculoEconomico as cl

wb = xl.load_workbook("Calculo economico.xlsx")
sheet = wb["Feuille1"]

cl.del_specific_currency("mmg")