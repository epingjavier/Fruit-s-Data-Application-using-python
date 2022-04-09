
import mysql.connector
myDB = {
    'user' : 'root',
    'password' : '*******',
    'host' : 'localhost',
    'database' : 'finance'
}
conn = mysql.connector.connect(**myDB)
Cr = conn.cursor(buffered = True)


def Menulogin():
    print("====== Selamat Datang di Aplikasi BuahLapak ======")
    print("1. Register")
    print ("2. Login")
    print ("3. Exit")

    opsi = input("Masukan opsi:")
    if opsi == '1':
        MenuRegister()
    elif opsi == '2':
        login()
    elif opsi == '3':
        print("Terimakasih sudah menggunakan Aplikasi Buah Lapak, Sampai Jumpa :*")
        exit(0)
    else:
        print("Kode yang anda masukan salah")
        Menulogin()

def MenuRegister():
    print("1. Registrasi Data")
    print("2. Kembali ke Menu Awal")
    opsi = input("Masukan opsi:")
    if opsi == '1':
        register()
    elif opsi == '2':
        Menulogin()
    else:
        print("Kode yang anda masukan salah")
        MenuRegister()

def register():
    query = "SELECT * FROM data_user"
    Cr.execute(query)
    data_user = Cr.fetchall()
    kodeuser=[]
    for i in data_user:
        kodeuser.append(i[0])
        continue
    userID = input("Masukan User Id:")
    if userID in kodeuser:
        print("Data yang anda masukan sudah terdaftar")
        MenuRegister()
    else:
        if userID.isalnum() and len(list(userID)) >= 6 and len(list(userID)) <= 20:
            password = input("Masukan password:")
            if len(list(password)) >= 8:
                email = input("Masukan email:")
                if email.count("@") > 1:
                    print ("Email anda salah, jumlah @ tidak boleh dari 2")
                else:
                    email1=email.split("@")
                    Username=email1[0]
                    username1 = Username.replace("_","").replace(".","").replace(" ","")
                    if username1.isalnum():
                        x=email1[1]
                        email2=x.split(".")
                        Hosting=email2[0]
                        Hosting1 = Hosting.replace("_","").replace(".","").replace(" ","")
                        if Hosting1.isalnum():
                            if x.count(".")!=0:
                                Ekstensi=email2[1]
                                Ekstensi1=len(list(Ekstensi))
                                if Ekstensi1 <= 5:
                                    if Ekstensi.count(".")<2:
                                        nama = input("Masukan nama:").title()
                                        nama1 = nama.replace(" ","")
                                        if nama1.isalpha():
                                            gender = input("Masukan gender (Pria/Wanita):").capitalize()
                                            if gender.isalpha() and gender == "Pria" or gender == "Wanita":
                                                usia = input("Masukan usia:")
                                                usia1 = int(usia)
                                                if usia.isdigit() and usia1 >=17 or usia1 <=80:
                                                    pekerjaan = input("Masukan pekerjaan:").title().replace(" ","")
                                                    if pekerjaan.isalpha():
                                                        hobi = input("Masukan hobi:").title()
                                                        if hobi.isalpha():
                                                            nomor = input("Masukan Nomor Telephon:")
                                                            if nomor.isdigit and len(list(nomor))>=11 and len(list(nomor))<=13:
                                                                alamat = input("Masukan Alamat:").title().replace(" ","").replace(".","").replace("-","").replace("_","")
                                                                if alamat.isalnum():
                                                                    y = 1
                                                                    while y <3 :
                                                                        opsi1 = input("Simpan data(Y/N):").upper()
                                                                        if opsi1 == "Y":
                                                                            y = 5
                                                                            sql = "INSERT INTO data_user VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
                                                                            val = (userID, password, email, nama, gender , usia1 , pekerjaan, hobi, nomor, alamat)
                                                                            Cr.execute(sql, val)
                                                                            conn.commit()
                                                                            # datauser[userID] = datauser_tambahan
                                                                            # print(f"User ID : {userID}, {datauser_tambahan}, {dataalamat_tambahan},{datageo_tambahan}")
                                                                            print("Data berhasil disimpan")
                                                                            MenuRegister()
                                                                        else:
                                                                            if opsi1 == "N":
                                                                                y = 5
                                                                                print("Data tidak ditambahkan")
                                                                                MenuRegister()
                                                                            else:
                                                                                y=1
                                                                    #                 else:
                                                                    #                     return("Longitude yang anda masukan salah"), MenuRegister()
                                                                    #             else:
                                                                    #                 return("Latitude yang anda masukan salah"), MenuRegister()
                                                                    #         else:
                                                                    #             return("Zipcode yang anda masukan salah"), MenuRegister()
                                                                    #     else:
                                                                    #         return("RT yang anda masukan salah"), MenuRegister()
                                                                    # else:
                                                                    #     return("RT yang anda masukan salah"), MenuRegister()
                                                                else:
                                                                    return("Alamat yang anda masukan salah"), MenuRegister()
                                                            else:
                                                                return("Nomor yang anda masukan salah"), MenuRegister()
                                                        else:
                                                            return("Hobi yang anda masukan salah, harus berupa huruf"), MenuRegister()
                                                    else:
                                                        return("Pekerjaan yang anda masukan salah, harus berupa huruf"), MenuRegister()
                                                else:
                                                    return("Usia yang anda masukan salah, harus berupa angka"), MenuRegister()
                                            else:
                                                return("Gender yang anda masukan salah atau tidak sesuai ketentuan"), MenuRegister()
                                        else:
                                            return("Nama yang anda masukan salah, nama hanya bisa huruf"),MenuRegister()
                                    else:
                                        return("Email anda salah, terlalu banyak (.)"), MenuRegister()
                                else:
                                    return("Email anda salah, format ekstensi salah"), MenuRegister()
                            else:
                                return("Email anda salah, ekstensi anda kosong"), MenuRegister()
                        else:
                            return ("Email anda salah, format hosting salah"), MenuRegister()
                    else:
                        return ("Email anda salah, format username salah"), MenuRegister()
            else:
                return("password harus berupa huruf dan angka dan karakter spesial"), MenuRegister()
        else:
            return("Data yang anda masukan salah, User ID hanya bisa huruf dan angka, minimal 6 karakter"), MenuRegister

def login():
    query = "SELECT * FROM data_user"
    Cr.execute(query)
    data_user = Cr.fetchall()
    kodeuser=[]
    passworduser=[]
    emailuser=[]
    for i in data_user:
        kodeuser.append(i[0])
        passworduser.append(i[1])
        emailuser.append(i[2])
        continue
    x = 1
    angka = 6
    while x < 3:
        userID = input("Masukan User ID:")
        password = input("Masukan password:")
        if userID in kodeuser or userID in emailuser:
            if password in passworduser:
                if kodeuser.index(userID) == passworduser.index(password):
                    x = 5
                    print("Selamat Datang di Aplikasi BuahLapak")
                    Menu()
                else:
                    angka -= 1
                    print(f"UserID/email dan Password tidak sesuai, kesempatan {angka}")
                    if angka == 0:
                        x = 5
                        print("Kesempatan anda habis")
                        Menulogin()
            else:
                if password not in passworduser:
                    angka -= 1
                    print(f"Password anda salah, kesempatan {angka}")
                    if angka == 0:
                        x = 5
                        print("Kesempatan anda habis")
                        Menulogin()
        else:
            if userID not in kodeuser or userID not in emailuser :
                angka -= 1
                x = 1
                print(f"User ID atau email yang anda masukan salah, kesempatan {angka}")   
                if angka == 0:
                    x=5
                    print("Kesempatan anda habis")
                    Menulogin()

def Menu():
    print("================= MENU BuahLapak =================")
    print("="*50)
    print("1. Baca Data Buah")
    print("2. Tambah Data Buah")
    print("3. Update Data Buah")
    print("4. Hapus Data Buah")
    print("5. Exit")
    print("="*50)
    print(" ")

    Option = input("Masukan option:")
    if Option == "1":
        print(" ")
        print("================= Menu Data Buah ================")
        MenuRead()
    elif Option == "2":
        print(" ")
        print("============== Menu Tambah Data Buah =============")
        MenuTambah()
    elif Option == "3":
        print(" ")
        print("============== Menu Update Data Buah =============")
        MenuUpdate()
    elif Option == "4":
        print(" ")
        print("============== Menu Hapus Data Buah ==============")
        MenuDelete()
    elif Option == "5":
        x = 1
        while x < 3:
            tanya = input("Apakah anda yakin akan keluar (Y/N): ").upper()
            if tanya == "Y":
                x = 5
                print("============= Logged Out Successfully ============")
                Menulogin()
            else:
                if tanya == "N":
                    x = 5
                    Menu()
                else:
                    x = 1
    else:
        print("Kode yang anda masukan salah")
        Menu()

def MenuRead():
    print("1. All data")
    print("2. Data tertentu")
    print("3. Kembali ke menu utama")  
    Option = input("Masukan option:")
    if Option == "1":
        print("================= Menu Data buah =================")
        ReadAll()
    elif Option == "2":
        Read()
    elif Option == "3":
        Menu()
    else:
        print("Kode yang anda masukan salah")
        MenuRead()

def ReadAll():
    query = "SELECT * FROM buah"
    Cr.execute(query)
    data_buah=[]
    data_index=0
    for i in range (1):
        for j in Cr:
            data_buah.append([j])
            if len(list(data_buah)) == 0:
                print("Data masih Kosong")
                MenuRead()
            else:
                if len(list(data_buah)) > 0:
                    i += 1
                    print("{}.Kode : {}, Nama Buah: {}, Stok :{}, Harga :{},Asal Kota : {} ".format(i,j[0],j[1],j[2],j[3],j[4]))
    MenuRead() 

def Read():
    query = "SELECT * FROM buah"
    Cr.execute(query)
    data_buah = Cr.fetchall()
    kodebuah = []
    for i in data_buah:
        kodebuah.append(i[0])
        continue
    data_index = 0

    if len(data_buah) == 0:
        print ("Data masih Kosong"), MenuRead()
    else:
        kode = input("Masukan Kode Buah:").upper()
        query = "SELECT kode, nama, stok, harga,asal_kota FROM buah where kode = %s"
        val = (kode,)
        Cr.execute(query,val)
        databuah_tertentu = Cr.fetchall()
        if kode in kodebuah:
            print(f"Data buah dengan kode : {kode}"),print("1.Kode Buah: {}, Nama: {}, Stok:{}, Harga:{},Satuan:{} ".format(kode, databuah_tertentu[0][1], databuah_tertentu[0][2], databuah_tertentu[0][3], databuah_tertentu[0][4]))
            MenuRead()   
        else: 
            if kode not in kodebuah:
                print("Data yang anda masukan tidak tersedia"), print(" ")
                MenuRead() 
                            
def MenuTambah():
    print("1. Tambah Data Buah")
    print("2. Kembali ke menu utama")  
    Option = input("Masukan option:")
    if Option == "1":
        print(" ")
        print("======Menu Tambah Data Buah=====")
        print(" ")
        Tambah()
    elif Option == "2":
        Menu()
    else:
        print("Kode yang anda masukan salah")
        print(" ")
        MenuTambah()

def Tambah():
    query = "SELECT * FROM buah"
    Cr.execute(query)
    data_buah = Cr.fetchall()
    kodebuah=[]
    for i in data_buah:
        kodebuah.append(i[0])
        continue
    kode = input("Masukan Kode Buah:").upper()
    if kode in kodebuah:
        print("Kode yang anda masukan sudah terdaftar")
        MenuTambah()
    else:
        if kode.isalnum():
            nama=input("Masukan Nama buah:").replace(" ","").title()
            if nama.isalpha():
                stok = input("Masukan Jumlah Stok:")
                if stok.isdigit():
                    harga = input("Masukan Harga Buah:")
                    if harga.isdigit():
                        asal = input("Masukan Asal Buah:").title()
                        if asal.isalpha():
                            x = 1
                            while x < 3:
                                tambah=input("Apakah data ingin ditambahkan(Y/N)? ").upper()
                                if tambah == "Y":
                                    x = 5
                                    sql = "INSERT INTO Buah VALUES (%s, %s, %s, %s, %s)"
                                    val = (kode, nama, int(stok), int(harga),asal)
                                    Cr.execute(sql, val)
                                    conn.commit()
                                    print("Data berhasil ditambahkan")
                                    MenuTambah()
                                else:
                                    if tambah == "N":
                                        x = 5
                                        print("Data tidak ditambahkan")
                                        MenuTambah()
                                    else:
                                        x = 1
                        else:
                            print("Asal yang anda masukan salah, asal harus berupa huruf"), MenuTambah()
                    else:
                        print("Harga yang anda masukan salah, harga harus berupa angka"), MenuTambah()
                else:
                    print("Stok yang anda masukan salah, stok harus berupa angka"), MenuTambah()
            else:
                print("Nama yang anda masukan salah, nama harus huruf"), MenuTambah()
        else:
            print("Kode yang anda masukan salah"), MenuTambah()

def MenuUpdate():
    print("1. Perbaharui Data Buah")
    print("2. Kembali ke menu utama")  

    Option = input("Masukan option:")
    if Option == "1":
        print(" ")
        print("======Menu Update Data Buah=====")
        print(" ")
        Update()
    elif Option == "2":
        Menu()
    else:
        print("Kode yang anda masukan salah")
        MenuUpdate()

def Update():
    query = "SELECT * FROM buah"
    Cr.execute(query)
    data_buah = Cr.fetchall()
    kodebuah=[]
    for i in data_buah:
        kodebuah.append(i[0])
        continue
    kode= input("Masukan Kode Buah:").upper()
    query = "SELECT kode, nama, stok, harga,asal_kota FROM buah where kode = %s"
    val = (kode,)
    Cr.execute(query,val)
    databuah_tertentu = Cr.fetchall()
    if kode not in kodebuah:
        print("Data tidak terdaftar")
        MenuUpdate()
    else:
        if kode in kodebuah:
            sql = "SELECT kode, nama, stok, harga, asal_kota FROM buah where kode = %s"
            val = (kode,)
            Cr.execute(sql,val)
            print(f"Data buah dengan kode : {kode}"),print("1.Kode Buah: {}, Nama: {}, Stok:{}, Harga:{}, Asal Kota:{} ".format(kode, databuah_tertentu[0][1], databuah_tertentu[0][2], databuah_tertentu[0][3], databuah_tertentu[0][4]))
            x = 1
            while x < 3:
                Opsi= input("Apakah data ingin diperbarui?(Y/N):").upper()
                if Opsi == "Y":
                    x = 5
                    kolom = input("Masukan Kolom/Keterangan yang ingin di edit(Nama/Stok/Harga/Asal):").title()
                    if kolom in (['Nama','Stok','Harga','Asal' ]):
                        val = input(f" Masukan {kolom} Baru: ").title()
                        x1 = 1
                        while x1 < 3:
                            opsi1=input("Apakah data akan diupdate? (Y/N):").upper()
                            if opsi1 == "Y":
                                if kolom == "Nama":
                                    x1 = 5
                                    sql = "Update buah set nama = %s where kode = %s "
                                    val1 = (val, kode)
                                    Cr.execute(sql, val1)
                                    conn.commit()
                                    print ("=====>Data berhasil diupdate<====="), MenuUpdate()
                                elif kolom == "Stok":
                                    x1 = 5
                                    sql = "Update buah set stok = %s where kode = %s "
                                    val1 = (int(val), kode)
                                    Cr.execute(sql, val1)
                                    conn.commit()
                                    print ("=====>Data berhasil diupdate<====="), MenuUpdate()
                                elif kolom == "Harga":
                                    x1 = 5
                                    sql = "Update buah set harga = %s where kode = %s "
                                    val1 = (int(val), kode)
                                    Cr.execute(sql, val1)
                                    conn.commit()
                                    print ("=====>Data berhasil diupdate<====="), MenuUpdate()
                                elif kolom == "Asal":
                                    x1 = 5
                                    sql = "Update buah set asal_kota = %s where kode = %s "
                                    val1 = (val, kode)
                                    Cr.execute(sql, val1)
                                    conn.commit()
                                    print ("=====>Data berhasil diupdate<====="), MenuUpdate()
                                else:
                                    x = 1
                            else:
                                if opsi1 == "N":
                                    x1 = 5
                                    print("=====x Terimakasih data anda tidak diupdate x====="), MenuUpdate()
                                else:
                                    x1 =1
                    else:
                        return print("Data tidak tersedia"), MenuUpdate ()
                else:
                    if Opsi == "N":
                        x = 5
                        print("=====x Data anda tidak diupdate x====")
                        print(" ")
                        MenuUpdate()
                    else:
                        x = 1
        else:
            return print("Data yang anda masukan tidak valid"), MenuUpdate()

def MenuDelete():
    print("1. Hapus Data Buah")
    print("2. Kembali ke menu utama")  

    Option = input("Masukan option:")
    if Option == "1":
        print(" ")
        print("======Menu Hapus Data Buah=====")
        print(" ")
        Delete()
    elif Option == "2":
        Menu()
    else:
        MenuDelete()

def Delete():
    query = "SELECT * FROM buah"
    Cr.execute(query)
    data_buah = Cr.fetchall()
    kodebuah=[]
    for i in data_buah:
        kodebuah.append(i[0])
        continue
    if len(data_buah)>0:
        kode = input("Masukan Kode Buah:").upper()
        if kode not in kodebuah:
            print("Data yang anda masukan tidak terdaftar")
            MenuDelete()
        else:
            x = 1
            while x < 3:
                opsi= input(f"Apakah anda yakin untuk menghapus data NIM {kode} ini?(Y/N):").upper()
                if opsi == "Y":
                    x = 5
                    query1 = "DELETE FROM buah WHERE Kode = %s"
                    val = (kode,)
                    Cr.execute(query1,val)
                    conn.commit()
                    print(f"=====> Data Kode Buah {kode} berhasil dihapus! <=====")
                    MenuDelete()
                else:
                    if opsi == "N":
                        x = 5
                        print("=====x Data tidak dihapus x====="), MenuDelete()
                    else:
                        x = 1
   
Menulogin()
  
