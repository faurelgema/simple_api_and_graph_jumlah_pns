import sqlite3, pandas , matplotlib.pyplot as plt
 
conn = sqlite3.connect("data/data_pns.db")


sql = """select jabatan, sum(jumlah_pns) as sum_pns from tblJobs group by id limit 5"""
 
data = pandas.read_sql(sql, conn)
 
plt.plot(data.jabatan,data.sum_pns, label = "Jumlah Pns")
plt.legend()
plt.title("Grafik jumlah pns perjabatan")
plt.show()
