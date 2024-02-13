from tabulate import tabulate
from math import sqrt

class Membership():
    # definisikan username, income, dan expense
    def __init__(self, username, monthly_income, monthly_expense):
        self.username = username
        self.monthly_income = monthly_income
        self.monthly_expense = monthly_expense
        self.membership = None

    # tunjukkan benefit dari masing-masing membership
    def show_benefit(self):
        rows = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"]
        ]

        columns = ["Membership", "Discount", "Another Benefit"]

        print(tabulate(rows, columns))

    # tunjukkan requirements dari masing-masing membership
    def show_requirements(self):
        rows = [
            ["Platinum", "8", "15"],
            ["Gold", "6", "10"],
            ["Silver", "5", "7"]
        ]

        columns = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]

        print(tabulate(rows, columns))

    # prediksi membership
    def predict(self):
        dict_tiers = {
            "Silver": [5, 7],
            "Gold": [6, 10],
            "Platinum": [8, 15]
        }
        distances = {} #simpan ke dalam key/value ke karena key = membership dan value = expense dan income

        for info_tier, requirements in dict_tiers.items():
            # hitung dengan menggunakan euclid distance (cek slide)
            dist = sqrt(
                ((self.monthly_expense - requirements[0])**2) + 
                ((self.monthly_income - requirements[1])**2)
            )
            # simpan ke dalam info_tier untuk key nya
            distances[info_tier] = dist
            print(f"Iterasi {info_tier} dan menghasilkan jarak {dist}.")

        # sort nilainya dari jarak terkecil untuk mendapatkan membership
        telah_diurutkan = sorted(distances)
        # ambil membership dari indeks pertama yang paling kecil
        self.membership = telah_diurutkan[0]

        print(f"Hasil prediksi adalah masuk ke tier {self.membership}")  

    # hitung kalkulasi pembelian barang
    def calculate_price(self, harga_barang):
        total_price = sum(harga_barang) #jumlahkan semua nilai yang ada pada harga_barang dengan method sum() karena harga_barang merupakan array
        # kategorikan masing-masing membership dan bonusnya (cek di slide)
        if(self.membership == "Silver"):
            total_price = (total_price - (total_price * 0.08))
        elif(self.membership == "Gold"):
            total_price = (total_price - (total_price * 0.10))
        elif(self.membership == "Platinum"):
            total_price = (total_price - (total_price * 0.15))
        elif(self.membership == None):
            total_price = (total_price - (total_price * 0.00))
        else:
            print("Membership invalid.")

        print(f"Anda masuk ke tier membership {self.membership}, total harga adalah Rp {total_price},-.")