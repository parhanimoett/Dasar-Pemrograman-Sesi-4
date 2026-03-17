# 1. Operator Aritmatika
print("======== Operator Aritmatika ========")
apel_budi = 12
dibagi = 4
apel_tambahan = 8
print("Budi memiliki", apel_budi,"apel dan dibagikan ke 4 temannya secara merata: ")
print("=", apel_budi, "/", dibagi)
print("=", int(apel_budi/dibagi), "apel/org")
sisa_apel = apel_budi % dibagi
print("Jml apel budi sekarang setelah dibagikan ke temannya :", sisa_apel)
print("-----------------------------------------------------------")

print("lalu budi mendapat 8 apel tambahan: ")
print("=", sisa_apel, "+", apel_tambahan)
print("Apel budi sekarang =", sisa_apel + apel_tambahan)

# 2. Operator Perbandingan
print("\n======== Operator Perbandingan ========")
siti = 160
andi = 165
print("Tinggi siti:", siti)
print("Tinggi andi:", andi)
if siti > andi:
    print("Perbandingan: Siti lebih tinggi dari andi")
else:
    print("Perbandingan: Andi lebih tinggi dari siti")

# 3. Operator Logika
print("\n======== Operator Logika ========")
print("Jika cuaca cerah dan pr selesai maka budi boleh bermain")
cuaca_cerah = True
pr_selesai = True
print("cuaca cerah:", cuaca_cerah)
print("pr selesai:", pr_selesai)

if cuaca_cerah and pr_selesai:
    print("Status: Budi bisa bermain")
else:
    print("Status: Budi tidak boleh bermain")

# 4. Operator Bitwise
print("\n======== Operator Bitwise ========")
a = 0b0110
b = 0b0011
print("======== AND ========")
c = a & b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== OR ========")
c = a | b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== XOR ========")
c = a ^ b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== Shift Kiri ========")
c = a << b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== Shift Kanan ========")
c = a >> b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

# 5. Operator Penugasan
print("\n======== Operator Penugasan ========")
saldo_awal = 50000
isi_ulang = 20000
paket_internet = 30000

print("Saldo awal pulsa:", saldo_awal)
print("Isi ulang pulsa:", isi_ulang)
saldo_awal += isi_ulang
print("Total Saldo setelah isi ulang:", saldo_awal, "\n")

print("Beli paket internet:", paket_internet)
saldo_awal -= paket_internet
print("Sisa saldo pulsa:", saldo_awal)

# 6. Operator Keanggotaan
print("\n======== Operator Keanggotaan ========")
dftr_peserta = ["Andi", "Budi", "Citra", "Dewi"]
cek_peserta = "Eka"
print("Daftar peserta lomba:", dftr_peserta)
print("Cek peserta:", cek_peserta)
if cek_peserta in dftr_peserta:
    print("Status: Eka ada dalam list peserta lomba coding")
else:
    print("Status: Eka tidak ada dalam list peserta lomba coding\n")

kalimat = "Saya suka belajar Python"
cek_kata = "Python"
print("Kalimat:",kalimat)
print("Kata yang dicari:", cek_kata)
if cek_kata in kalimat:
    print("Status: kata tersebut terdapat pada kalimat")
else:
    print("Status: kata tersebut tidak terdapat pada kalimat")

# 7. Operator Identitas
print("\n======== Operator Identitas ========")
a = 5
b = 5
print("Nilai a :", a, ", id:", hex(id(a)))
print("Nilai b :", b, ", id:", hex(id(b)))
print("Apakah a is b :", a is b, "\n")

c = ["Ucup", "Budi", "Siti"]
d = ["Ucup", "Budi", "Siti"]
print("Nilai c :", c, ", id:", hex(id(c)))
print("Nilai d :", d, ", id:", hex(id(d)))
print("Apakah c is d :", c is d)
print("Apakah c == d :", c == d)

# 8. Operator Ternary
print("\n======== Operator Ternary ========")
angka = 120
print("angka:", angka)
hasil = "Lebih dari 100" if angka > 100 else "Tidak lebih dari 100"
print("Status:", angka, hasil,"\n")

nilai = 80
print("nilai:", nilai)
status = "Lulus" if nilai > 70 else "Tidak Lulus"
print("Status:", status)