import sqlite3, pandas , matplotlib.pyplot as plt
 
conn = sqlite3.connect("data/data_pns.db")


sql = """select sum(jumlah_pns) as sum_pns from tblJobs group
  by tahun limit 3"""
 
data = pandas.read_sql(sql, conn)
mylabels = ["2020", "2017", "2016"]
plt.pie(data.sum_pns, labels = mylabels)
plt.title("Diagram Lingkaran tahunan dari jumlah pns")
plt.show()