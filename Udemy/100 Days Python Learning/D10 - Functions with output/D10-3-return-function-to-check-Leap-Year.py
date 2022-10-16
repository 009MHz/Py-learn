#1 ganti if statement yg tadinya merupakan printing result menjadi True or False argument dengan command return
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month): #2 penambahan parameter ke dalam fungsi yang sudah dipanggil sebagai argumen dari coding line 24 & 25
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #3 parameter awal sebelum fungsi untuk mencari leap year dilakukan
    if is_leap(year): #4 kondisi yang diminta untuk mengganti bulan februari menjadi 29 apabila leap year  sudah benar, penambahan == True or "is True" menjadi opsional karena sudah didefine dari resolving nomor 1 
        month_days[1] = 29 #5 fungsi untuk mengganti list nomor 2 (februari) yang tadinya 28 => 29, jika syarat sebelumnya terpenuhi
    return month_days [month -1] #6 kondisi jika syarat 4 tidak terpenuhi
    # jika kondisi 6 tidak diberikan => akan printing "none"
    # tanpa menggunakan [list] yg detail(return month_days) => printing semua value dari month_days [31,28...31]
    # menggunakan [month] tanpa -1 => printing list data setelah line 25 diinput (i.e: 2 => akan memanggil list nomor 3) karena list python dimulai dari 0 instead 1
        
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)