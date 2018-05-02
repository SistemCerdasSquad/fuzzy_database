# # Koneksi Database

import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="masrestu",     # password
                     db="fuzzy")   # name of the database


# # Membuat objek sql
sql = db.cursor()


# # Membuat Tabel
from beautifultable import BeautifulTable



# # Data Awal
sql.execute("SELECT * FROM DataHP")


# # Fungsi Fuzzy Harga
def harga_murah(harga):
    if harga <= 50:
        return 1
    if harga >= 150:
        return 0
    if harga > 50 and harga < 150:
        return round(((150 - harga) / 100),3)

def harga_normal(harga):
    if harga <= 50 or harga >= 500:
        return 0
    if harga > 50 and harga < 150:
        return round(((harga - 50)/ 100),3)
    if harga > 150 and harga < 500:
        return round(((500 - harga) / 350),3)
def harga_mahal(harga):
    if harga <= 150:
        return 0
    if harga >= 500:
        return 1
    if harga > 150 and harga < 500:
        return round(((harga - 150) / 350),3)

def predict_Harga(harga):
    murah = harga_murah(harga)
    normal = harga_normal(harga)
    mahal = harga_mahal(harga)

    return murah, normal, mahal


# # Fuzzy Harga
sql.execute("SELECT Type,Harga FROM DataHP")

table_harga = BeautifulTable()

header_harga = ["No","type","harga","murah","normal","mahal"]
table_harga.column_headers = header_harga
nomor = 1
for row in sql.fetchall() :
    murah, normal, mahal = predict_Harga(row[1])
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_harga.append_row([nomor, row[0], row[1], murah, normal, mahal])
    nomor = nomor + 1
print(table_harga)


# # Fungsi Fuzzy Dimensi
def panjang_Pendek(panjang):
    if panjang <= 65:
        return 1
    if panjang >= 100:
        return 0
    if panjang > 65 and panjang < 100:
        return (100 - panjang) / 35
    
def panjang_Normal(panjang):
    if panjang <= 65 or panjang >= 200:
        return 0
    if panjang > 65 and panjang < 100:
        return (panjang - 65) / 35
    if panjang > 100 and panjang < 200:
        return (200 - panjang) / 100
    
def panjang_Panjang(panjang):
    if panjang <= 100:
        return 0
    if panjang >= 200:
        return 1
    if panjang > 100 and panjang < 200:
        return (panjang - 100) / 100

def lebar_Sempit(lebar):
    if lebar <= 20:
        return 1
    if lebar >= 45:
        return 0
    if lebar > 20 and lebar < 45:
        return (45 - lebar) / 7
    
def lebar_Normal(lebar):
    if lebar <= 20 or lebar >= 45:
        return 0
    if lebar > 20 and lebar < 45:
        return (lebar - 20) / 15
    if lebar > 45 and lebar < 80:
        return (80 - lebar) / 35
    
def lebar_Lebar(lebar):
    if lebar <= 45:
        return 0
    if lebar >= 80:
        return 1
    if lebar > 45 and lebar < 80:
        return (lebar - 45) / 35
    

def tebal_Tipis(tebal):
    if tebal <= 10:
        return 1
    if tebal >= 25:
        return 0
    if tebal > 10 and tebal < 25:
        return (25 - tebal) / 15
    
def tebal_Normal(tebal):
    if tebal <= 10 or tebal >= 100:
        return 0
    if tebal > 10 and tebal < 25:
        return (tebal - 10) / 15
    if tebal > 25 and tebal < 100:
        return (100 - tebal) / 75
    
def tebal_Tebal(tebal):
    if tebal <= 25:
        return 0
    if tebal >=100:
        return 1
    if tebal > 25 and tebal < 100:
        return (tebal - 25) / 75
    
def ukuran_kecil(ukuran):
    if ukuran <= 13:
        return 1
    if ukuran >= 112.5:
        return 0
    if ukuran > 13 and ukuran < 112.5:
        return round(((112.5 - ukuran) / 99.5),3)

def ukuran_normal(ukuran):
    if ukuran <= 13 or ukuran >= 1600:
        return 0
    if ukuran > 13 and ukuran < 99.5:
        return (ukuran - 13) / 99.5
    if ukuran > 99.5 and ukuran < 1600:
        return round(((1600 - ukuran) / 1487.5),3)
    
def ukuran_besar(ukuran):
    if ukuran <= 112.5:
        return 0
    if ukuran >= 1600:
        return 1
    if ukuran > 112.5 and ukuran < 1600:
        return round(((ukuran - 112.5) / 1487.5),3)

def predict_Dimensi(panjang, lebar, tebal):
   
    ukuran = (panjang * lebar * tebal) / 1000
    kecil = ukuran_kecil(ukuran)
    normal = ukuran_normal(ukuran)
    besar = ukuran_besar(ukuran)
    return kecil, normal, besar


# # Fuzzy Dimensi
sql.execute("SELECT Type,P,L,T FROM DataHP")

table_dimensi = BeautifulTable()

header_dimensi = ["No","type","P","L","T","P*L*T","Kecil","Normal","Besar"]
table_dimensi.column_headers = header_dimensi
nomor = 1
for row in sql.fetchall() :
    kecil, normal, besar = predict_Dimensi(panjang=row[1],lebar=row[2],tebal=row[3])
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_dimensi.append_row([nomor, row[0], row[1], row[2], row[3],row[1]*row[2]*row[3], kecil, normal, besar])
    nomor = nomor + 1
print(table_dimensi)


# # Fungsi Fuzzy Berat
def berat_ringan(berat):
    if berat <= 50:
        return 1
    if berat >= 100:
        return 0
    if berat > 50 and berat < 100:
        return round(((100-berat) / 50),3)

def berat_normal(berat):
    if berat <= 50 or berat >= 250:
        return 0
    if berat > 50 and berat < 100:
        return round(((berat - 50) / 50),3)
    if berat > 100 and berat < 250:
        return round(((250 - berat) / 150),3)

def berat_berat(berat):
    if berat <= 100:
        return 0
    if berat >= 250:
        return 1
    if berat > 100 and berat < 250:
        return round(((berat - 100) / 150),3)

def predict_Berat(berat):
    ringan = berat_ringan(berat)
    normal = berat_normal(berat)
    berat = berat_berat(berat)
    return ringan, normal, berat


# # Fuzzy Berat
sql.execute("SELECT Type,Berat FROM DataHP")

table_berat = BeautifulTable()

header_berat = ["No","Type","Berat","Ringan","Normal","Berat"]
table_berat.column_headers = header_berat
nomor = 1
for row in sql.fetchall() :
    ringan, normal, berat = predict_Berat(row[1])
    
    table_berat.append_row([nomor, row[0], row[1],ringan, normal, berat])
    nomor = nomor + 1
print(table_berat)


# # Fungsi Fuzzy Standby Time
def standby_Sebentar(standby):
    if standby <= 50:
        return 1
    if standby >= 200:
        return 0
    if standby > 50 and standby < 200:
        return round(((200 - standby) / 150),3)

def standby_Normal(standby):
    if standby <= 50 or standby >= 500:
        return 0
    if standby > 50 and standby < 200:
        return round(((standby - 50) / 150),3)
    if standby > 200 and standby < 500:
        return round(((500 - standby) / 300),3)

def standby_Lama(standby):
    if standby <= 200:
        return 0
    if standby >= 500:
        return 1
    if standby > 200 and standby < 500:
        return round(((standby - 200) / 300),3)

def predict_Standby(standby):
    sebentar = standby_Sebentar(standby)
    normal = standby_Normal(standby)
    lama = standby_Lama(standby)
    
    return sebentar, normal, lama


# # Fuzzy Standby Time
sql.execute("SELECT Type,StandBy FROM DataHP")

table_standby = BeautifulTable()

header_standby = ["No","Type","Berat","Ringan","Normal","Berat"]
table_standby.column_headers = header_standby
nomor = 1
for row in sql.fetchall() :
    sebentar, normal, lama = predict_Standby(row[1])
    
    table_standby.append_row([nomor, row[0], row[1],sebentar, normal, lama])
    nomor = nomor + 1
print(table_standby)


# # Fungsi Fuzzy Talk Time
def talk_time_Sebentar(talk_time):
    if talk_time <= 50:
        return 1
    if talk_time >= 250:
        return 0
    if talk_time > 50 and talk_time < 250:
        return round(((250 - talk_time) / 200),3)
    
def talk_time_Normal(talk_time):
    if talk_time <= 50 or talk_time >= 250:
        return 0
    if talk_time > 50 and talk_time < 250:
        return round(((talk_time - 50) / 200),3)
    if talk_time > 250 and talk_time < 1000:
        return round(((1000 - talk_time) / 750),3)

def talk_time_Lama(talk_time):
    if talk_time <= 250:
        return 0
    if talk_time >= 1000:
        return 1
    if talk_time > 250 and talk_time < 1000:
        return round(((talk_time - 250) / 750),3)

def predict_Talktime(talk_time):
    sebentar = talk_time_Sebentar(talk_time)
    normal = talk_time_Normal(talk_time)
    lama = talk_time_Lama(talk_time)
    
    return sebentar, normal, lama


# # Fuzzy Talk Time
sql.execute("SELECT Type,TalkTime FROM DataHP")

table_talk_time = BeautifulTable()

header_talk_time = ["No","Type","Berat","Sebentar","Normal","Lama"]
table_talk_time.column_headers = header_talk_time
nomor = 1
for row in sql.fetchall() :
    sebentar, normal, lama = predict_Talktime(row[1])
    
    table_talk_time.append_row([nomor, row[0], row[1],sebentar, normal, lama])
    nomor = nomor + 1
print(table_talk_time)


# # Fungsi Fuzzy Phonebook Memory
def pb_sedikit(phonebook):
    if phonebook <= 50:
        return 1
    if phonebook >= 250:
        return 0
    if phonebook > 50 and phonebook < 250:
        return round(((250 - phonebook) / 200),3)

def pb_sedang(phonebook):
    if phonebook <= 50 or phonebook >= 1000:
        return 0
    if phonebook > 50 and phonebook <= 250:
        return round(((phonebook - 50) / 200),3)
    if phonebook > 250 and phonebook < 1000:
        return round(((1000 - phonebook) / 750),3)

def pb_banyak(phonebook):
    if phonebook <= 250:
        return 0
    if phonebook >= 1000:
        return 1
    if phonebook > 250 and phonebook < 1000:
        return round(((phonebook - 250) / 750),3)

def predict_PhoneBook(phonebook):
    sebentar = pb_sedikit(phonebook)
    normal = pb_sedang(phonebook)
    lama = pb_banyak(phonebook)
    
    return sebentar, normal, lama


# # Fuzzy Phonebook Memory
sql.execute("SELECT Type,PhoneBook FROM DataHP")


table_phonebook = BeautifulTable()

header_phonebook = ["No","Type","Berat","Sedikit","Sedang","Banyak"]
table_phonebook.column_headers = header_phonebook
nomor = 1
for row in sql.fetchall() :
    sedikit, sedang, banyak = predict_PhoneBook(row[1])
    
    table_phonebook.append_row([nomor, row[0], row[1],sedikit, sedang, banyak])
    nomor = nomor + 1
print(table_phonebook)


# # Fungsi Fuzzy Voice Dialing
def voice_Sedikit(voice_dialing):
    if voice_dialing is 0:
        return 1
    if voice_dialing >= 10:
        return 0
    if voice_dialing > 0 and voice_dialing < 10:
        return (10 - voice_dialing) / 10
    
def voice_Sedang(voice_dialing):
    if voice_dialing >= 25:
        return 0
    if voice_dialing >= 0 and voice_dialing <= 10:
        return (voice_dialing / 10)
    if voice_dialing >= 10 and voice_dialing < 25:
        return (25 - voice_dialing) / 15
    
def voice_Banyak(voice_dialing):
    if voice_dialing <= 10:
        return 0
    if voice_dialing >= 25:
        return 1
    if voice_dialing > 10 and voice_dialing < 25:
        return (voice_dialing - 10) / 15
    
def predict_VoiceDailing(voice_dailing):
    sedikit = voice_Sedikit(voice_dailing)
    sedang = voice_Sedang(voice_dailing)
    banyak = voice_Banyak(voice_dailing)
    
    return sedikit, sedang, banyak


# # Fuzzy Voice Dialing

sql.execute("SELECT Type,VoiceDailing FROM DataHP")

table_voicedailing = BeautifulTable()

header_voicedailing = ["No","Type","Berat","Sedikit","Sedang","Banyak"]
table_voicedailing.column_headers = header_voicedailing
nomor = 1
for row in sql.fetchall() :
    sedikit, sedang, banyak = predict_VoiceDailing(row[1])
    
    table_voicedailing.append_row([nomor, row[0], row[1],sedikit, sedang, banyak])
    nomor = nomor + 1
print(table_voicedailing)


# # Fungsi Fuzzy Jumlah Games
def games_Sedikit(jumlah_games):
    if jumlah_games is 0:
        return 1
    if jumlah_games > 0 and jumlah_games < 5:
        return (5-jumlah_games)/5
    if jumlah_games >= 5:
        return 0
    
def games_Sedang(jumlah_games):
    if jumlah_games >= 10:
        return 0
    if jumlah_games >= 0 and jumlah_games <= 5:
        return (jumlah_games / 5)
    if jumlah_games > 5 and jumlah_games < 10:
        return (10 - jumlah_games) / 5
    
def games_Banyak(jumlah_games):
    if jumlah_games <= 5:
        return 0
    if jumlah_games > 5 and jumlah_games < 10:
        return (jumlah_games-5)/5
    if jumlah_games >= 10:
        return 1

def predict_Games(jumlah_games):
    sedikit = games_Sedikit(jumlah_games)
    sedang = games_Sedang(jumlah_games)
    banyak = games_Banyak(jumlah_games)
    
    return sedikit, sedang, banyak


# # Fuzzy Games
sql.execute("SELECT Type,Games FROM DataHP")

table_games = BeautifulTable()

header_games = ["No","Type","Berat","Sedikit","Sedang","Banyak"]
table_games.column_headers = header_games
nomor = 1
for row in sql.fetchall() :
    sedikit, sedang, banyak = predict_Games(row[1])
    
    table_games.append_row([nomor, row[0], row[1],sedikit, sedang, banyak])
    nomor = nomor + 1
print(table_games)

# # Fungsi Fuzzy Message Length
def message_Pendek(message_length):
    if message_length <=100:
        return 1
    if message_length >=200:
        return 0
    if message_length > 100 and message_length < 200:
        return (200-message_length)/100
    
def message_Normal(message_length):
    if message_length >100 or message_length < 750:
        return 0
    if message_length >100 and message_length > 200:
        return (message_length-100)/100
    if message_length >200 and message_length > 750:
        return (750-message_length)/550
    
def message_Panjang(message_length):
    if message_length <=200:
        return 0
    if message_length >200 and message_length < 750:
        return (message_length-200)/550
    if message_length >=750:
        return 1

def predict_Message(message_length):
    pendek = message_Pendek(message_length)
    normal = message_Normal(message_length)
    panjang = message_Panjang(message_length)
    
    return pendek, normal, panjang


# # Fuzzy Message Length
sql.execute("SELECT Type,MessegeLength FROM DataHP")

table_message = BeautifulTable()

header_message = ["No","Type","Berat","Sedikit","Sedang","Banyak"]
table_message.column_headers = header_message
nomor = 1
for row in sql.fetchall() :
    pendek, normal, panjang = predict_Message(row[1])
    
    table_message.append_row([nomor, row[0], row[1],pendek, normal, panjang])
    nomor = nomor + 1
print(table_message)


# # Murah Semua
sql.execute("SELECT Type,Harga FROM DataHP")

table_harga_murah = BeautifulTable()

header_harga_murah = ["No","type","harga","rekomendasi"]
table_harga_murah.column_headers = header_harga_murah
nomor = 1
for row in sql.fetchall() :
    murah, normal, mahal = predict_Harga(row[1])
    
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_harga_murah.append_row([nomor, row[0], row[1], max(murah, normal, mahal)])
    nomor = nomor + 1
print(table_harga_murah)


# # Query 3
sql.execute("SELECT NamaHP,Type,Harga,P,L,T,MessegeLength from JenisHP "+
            "INNER JOIN DataHP on DataHP.Kode=JenisHP.Kode WHERE JenisHP.NamaHP='Nokia'")
table_query3 = BeautifulTable()

header_query3 = ["No","Merk","type","harga","kecil","panjang","Fire Strength"]
table_query3.column_headers = header_query3
nomor = 1
for row in sql.fetchall() :
    #murah, normal, mahal = predict_Harga(row[2])
    kecil, normal, besar = predict_Dimensi(panjang=row[3],lebar=row[4],tebal=row[5])
    pendek, normal, panjang = predict_Message(row[6])
    
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_query3.append_row([nomor, row[0], row[1],row[2],kecil,panjang,min(kecil,panjang)])
    nomor = nomor + 1
print(table_query3)


# # Query 4
sql.execute("SELECT NamaHP,Type,Harga,P,L,T from JenisHP "+
           "INNER JOIN DataHP on DataHP.Kode=JenisHP.Kode")
table_query4 = BeautifulTable()

header_query4 = ["No","Merk","type","harga","murah","kecil","Fire Strength"]
table_query4.column_headers = header_query4
nomor = 1
for row in sql.fetchall() :
    #murah, normal, mahal = predict_Harga(row[2])
    kecil, normal, besar = predict_Dimensi(panjang=row[3],lebar=row[4],tebal=row[5])
    murah, normal, mahal = predict_Harga(row[2])
    
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_query4.append_row([nomor, row[0], row[1],row[2],murah,kecil,max(kecil,murah)])
    nomor = nomor + 1
print(table_query4)


# # Query 5
sql.execute("SELECT NamaHP,Type,Harga,P,L,T,Berat,MessegeLength from JenisHP "+
           "INNER JOIN DataHP on DataHP.Kode=JenisHP.Kode")
table_query5 = BeautifulTable()

header_query5 = ["No","Merk","type","harga","murah","kecil","ringan","panjang","Fire Strength"]
table_query5.column_headers = header_query5
nomor = 1
for row in sql.fetchall() :
    #murah, normal, mahal = predict_Harga(row[2])
    kecil, normal, besar = predict_Dimensi(panjang=row[3],lebar=row[4],tebal=row[5])
    
    murah, normal, mahal = predict_Harga(row[2])
    
    ringan, normal, berat = predict_Berat(row[6])
    
    pendek, normal, panjang = predict_Message(row[7])
    
    #print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", muda, " ", parobaya, " ", tua)
    table_query5.append_row([nomor, row[0], row[1],row[2],murah,kecil,ringan,panjang,max(min(murah,kecil),min(murah,ringan),min(murah,panjang))])
    nomor = nomor + 1
print(table_query5)

