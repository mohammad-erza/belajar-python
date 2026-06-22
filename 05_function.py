def celcius_ke_fahrenheit(celcius):
  fahrenheit = (celcius * 1.8) + 32
  return fahrenheit
celcius = int(input("Masukkan suhu dalam celcius: "))
hasil1 = celcius_ke_fahrenheit(celcius)
print(hasil1)

def luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
hasil = luas_segitiga(10, 5)
print(hasil)