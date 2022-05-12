import sqlite3, pandas , matplotlib.pyplot as plt
 
conn = sqlite3.connect("data/data_pns.db")


sql = """select jumlah_pns, jabatan from tblJobs group
  by id limit 5"""
 
data = pandas.read_sql(sql, conn)
plt.bar(data.jabatan, data.jumlah_pns)
plt.title("Diagram batang jabatan dan jumlahnya")
plt.show()