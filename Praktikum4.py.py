isi_nama  = []
isi_nim   = []
isi_tugas = []
isi_uts   = []
isi_uas   = []
ratarata  = []

a = 0
while True:
    isi_nama.append(str(input("Masukan nama:  ")))
    isi_nim.append(int(input("Masukan NIM:  ")))
    tugas = int(input("Masukan nilai tugas:  "))
    isi_tugas.append(tugas)
    uts   = int(input("Masukan nilai UTS:  "))
    isi_uts.append(uts)
    uas   = int(input("Masukan nilai UAS:  "))
    isi_uas.append(uas)
    ratarata.append(tugas * 30/100 + uts * 35/100 + uas * 35/100)
    n = input("Lanjut (Y/T):  ")
    if n == "t" or n == "T" :
        break

    print()

    print(60*"=")
    print("| {0:0} | {1:1} | {2:2} | {3:3} | {4:4} | {5:5} | {6:6} | ".format('NO' , 'NAMA' , 'NIM' , 'TUGAS' , 'UTS' , 'UAS' , 'AKHIR'))
    print(60*"=")

    no = 0
    for nama, nim, tugas, uts, uas, akhir in zip (isi_nama, isi_nim, isi_tugas, isi_uts, isi_uas, ratarata):
        no += 1
        print ("| {0:0} | {1:1} | {2:2} | {3:3} | {4:4} | {5:5} | {6:6} | ".format(no,nama,nim,tugas,uts,uas,akhir))
        print(60*'=')
    
    
