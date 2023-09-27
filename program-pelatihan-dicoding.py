print("---------  Selamat datang di program ----------")
print("=" * 46)
print("|          MUHAMMAD IQBAL FIRMANSYAH         |")
print("|                210441100084                |")
print("|          PROJECT PROGRAM PELATIHAN         |")
print("|                  DICODING                  |")
print("=" * 46)
print("")

program = []
nik = int(input("Masukkan NIK : "))
nama = input("Masukkan Nama Lengkap : ")
instansi = input("Masukkan Instansi : ")
alamat = input("Masukkan Alamat Domisili : ")
tlpn = int(input("Nomor Handphone : "))
ijazah = input("Pendidikan Terakhir : ")
email = input("Email : ")

print("=" * 95)
print("PILIHAN PROGRAM PELATIHAN DICODING")
print("1. Belajar Dasar SQL")
print("2. Belajar Dasar PYTHON")
print("3. Belajar Dasar JAVA")
print("4. Belajar Dasar KOTLIN")
print("5. Belajar Dasar LARAVEL")         
print("6. Ikut 2 Program diskon 50%, (Khusus Belajar Dasar SQL, PYTHON, JAVA)")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
print("7. Selesaikan Pembayaran")
print("8. Keluar")
print("=" * 95)
while True:
    user = int(input("Masukkan pilihan: "))
    if user == 8:
        break
    elif user == 1:
        a = 1
        biaya_dsrsql = 159000        
        hasil = a * biaya_dsrsql
        print("Biaya program Belajar Dasar SQL adalah Rp ", hasil)
        print("Apakah Anda Memiliki Kode Voucher?\nMasukkan Kode Voucher dan dapatkan potongan 15%")
        Voucher = "CODINGSQL"
        user = input("Masukkan Kode Voucher: ")
        if user == "CODINGSQL":
            diskon = biaya_dsrsql - (hasil * 15 / 100)
            print("Biaya setelah diskon adalah", diskon)
            print("Berikut adalah invoice pemesanan Anda, silahkan simpan sebagai bukti pendaftaran.")
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t: ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp", diskon)
            
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)
        else:
            print("Biaya program Belajar Dasar SQL adalah Rp ", hasil)
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t : ", ijazah)
            print("Email\t\t\t: ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp ", hasil)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)

    elif user == 2:
        a = 1
        biaya_drspython = 169000
        hasil = a * biaya_drspython
        print("Biaya program Belajar Dasar PYTHON adalah Rp ", hasil)
        print("Apakah Anda Memiliki Kode Voucher?\nMasukkan Kode Voucher dan dapatkan potongan 15%")
        Voucher = "CODINGPYTHON"
        user = input("Masukkan Kode Voucher: ")
        if user == "CODINGPYTHON":
            diskon = biaya_drspython - (hasil * 15 / 100)
            print("Biaya setelah diskon adalah", diskon)
            print("Berikut adalah invoice pemesanan Anda, silahkan simpan sebagai bukti pendaftaran.")
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t: ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp", diskon)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)
        else:
            print("Biaya program Belajar Dasar PYTHON adalah Rp ", hasil)
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t: ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp ", hasil)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)

    elif user == 3:
        a = 1
        b = 179000
        hasil = a * b
        print("Biaya program Belajar Dasar JAVA adalah Rp ", hasil)
        print("Apakah Anda Memiliki Kode Voucher?\nMasukkan Kode Voucher dan dapatkan potongan 5%")
        Voucher = "CODINGJAVA"
        user = input("Masukkan Kode Voucher: ")
        if user == "CODINGJAVA":
            diskon = b - (hasil * 5 / 100)
            print("Biaya setelah diskon adalah", diskon)
            print("Berikut adalah kartu booking program Anda, silahkan simpan sebagai bukti pendaftaran.")
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t:", email)
            print("Total biaya program yang harus dibayarkan adalah Rp", diskon)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)
        else:
            print("Biaya program Belajar Dasar JAVA adalah Rp ", hasil)
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t : ', nik)
            print('Nama Lengkap\t\t : ', nama )
            print('Instansi\t : ', instansi)
            print('Alamat Domisili\t\t : ', alamat)
            print('Nomor Handphone\t\t : ', tlpn)
            print("Pendidikan Terakhir\t : ", ijazah)
            print("Email\t\t\t : ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp ", hasil)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)

    elif user == 4:
        a = 1
        b = 189000
        hasil = a * b
        print("Biaya program Belajar Dasar KOTLIN adalah Rp ", hasil)
        print("Apakah Anda Memiliki Kode Voucher?\nMasukkan Kode Voucher dan dapatkan potongan 20%")
        Voucher = "CODINGKOTLIN"
        user = input("Masukkan Kode Voucher: ")
        if user == "CODINGKOTLIN":
            diskon = b - (hasil * 20 / 100)
            print("Biaya setelah diskon adalah", diskon)
            print("Berikut adalah kartu booking program Anda, silahkan simpan sebagai bukti pendaftaran.")
            print("=" * 95)
            print('\nINVOICE PEMESANAN')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t:", email)
            print("Total biaya program yang harus dibayarkan adalah Rp", diskon)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)

    elif user == 5:
        a = 1
        b = 198000
        hasil = a * b
        print("Biaya program Belajar Dasar LARAVEL adalah Rp ", hasil)
        print("Apakah Anda Memiliki Kode Voucher?\nMasukkan Kode Voucher dan dapatkan potongan 5%")
        Voucher = "COINGLARAVEL"
        user = input("Masukkan Kode Voucher: ")
        if user == "COINGLARAVEL":
            diskon = b - (hasil * 5 / 100)
            print("Biaya setelah diskon adalah", diskon)
            print("Berikut adalah kartu booking program Anda, silahkan simpan sebagai bukti pendaftaran.")
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama)
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t: ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp", diskon)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)
        else:
            print("Biaya program Belajar Dasar LARAVEL adalah Rp ", hasil)
            print("=" * 95)
            print('\nKARTU BOOKING PROGRAM')
            print('NIK\t\t\t: ', nik)
            print('Nama Lengkap\t\t: ', nama )
            print('Instansi\t: ', instansi)
            print('Alamat Domisili\t\t: ', alamat)
            print('Nomor Handphone\t\t: ', tlpn)
            print("Pendidikan Terakhir\t: ", ijazah)
            print("Email\t\t\t: ", email)
            print("Total biaya program yang harus dibayarkan adalah Rp ", hasil)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)

    elif user == 6:
        for a in range(2):
            program.append(input("Tambahkan program: "))

        b = {
            "Belajar Dasar SQL": 159000,
            "Belajar Dasar PYTHON": 169000,
            "Belajar Dasar JAVA": 179000,
        }

        print("Apakah ada program yang ingin diubah?")
        pilih = input("y/t : ").lower()

        if pilih == "y":
            x = input("Pilih program yang ingin diganti : ")
            y = input("Pilih program pengganti: ")

            if x in b and y in b:
                biaya = b[x] + b[y]
                total_biaya = biaya - (biaya * 50 / 100)

                print("Program dipilih adalah", x, "dan", y)
                print("Rincian biaya = Rp", b[x], "+ Rp", b[y], "= Rp", biaya)
                print("Total pembayaran program adalah: Rp", total_biaya)
                print("Berikut adalah kartu booking program Anda, silahkan simpan sebagai bukti pendaftaran.")
                print("=" * 95)
                print("\nKARTU BOOKING PROGRAM")
                print("NIK\t\t\t:", nik)
                print("Nama Lengkap\t:", nama)
                print("Instansi\t:", instansi)
                print("Alamat Domisili\t:", alamat)
                print("Nomor Handphone\t:", tlpn)
                print("Pendidikan Terakhir\t:", ijazah)
                print("Email\t\t\t:", email)
                print("Total biaya program yang harus dibayarkan adalah Rp", total_biaya)
                print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
                print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
                print("=" * 95)
            else:
                print("Program yang Anda pilih tidak valid.")
        else:
            total_biaya = 0
            for program_pilihan in program:
                if program_pilihan in b:
                    total_biaya += b[program_pilihan]

            total_biaya_diskon = total_biaya * 0.5  # Diskon 50%

            print("Program dipilih adalah:", program)
            print("Total biaya program adalah: Rp", total_biaya)
            print("Total pembayaran program adalah: Rp", total_biaya_diskon)
            print("Berikut adalah kartu booking program Anda, silahkan simpan sebagai bukti pendaftaran.")
            print("=" * 95)
            print("\nKARTU BOOKING PROGRAM")
            print("NIK\t\t\t:", nik)
            print("Nama Lengkap\t:", nama)
            print("Instansi\t:", instansi)
            print("Alamat Domisili\t:", alamat)
            print("Nomor Handphone\t:", tlpn)
            print("Pendidikan Terakhir\t:", ijazah)
            print("Email\t\t\t:", email)
            print("Total biaya program yang harus dibayarkan adalah Rp", total_biaya_diskon)
            print("Pembayaran paling lambat 1x24 jam, apabila melebihi batas waktu yang ditentukan maka pendaftaran akan hangus. Silahkan ulangi pendaftaran dari awal.")
            print("Jika sudah melakukan pembayaran, harap konfirmasi ke CP berikut: 089-XXXX-XXXX")
            print("=" * 95)

    elif user == 7:
        print("Apakah yang Anda pesan sudah benar? Apakah Anda ingin mengulang dari awal?")
        pilih = "ya" 
        user = input("y/t: ").lower()

        if user in ["iya", "ya", "y"]:
            program.clear()
            print("Pilihan program Anda telah dihapus. Silakan ulangi dari awal.")
        else:
            print("Selamat! Anda telah berhasil mendaftar. Untuk selanjutnya silahkan selesaikan tahap pembayarannya, terima kasih.")
            break

    else:
        print("Maaf, pilihan Anda tidak sesuai dengan opsi yang ada!")
   


