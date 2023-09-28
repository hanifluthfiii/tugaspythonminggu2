def is_even_and_between_10_20(number):
    return 10 <= number <= 20 and number % 2 == 0

bilangan = int(input("Masukkan bilangan yang akan di verifikasi: "))

if is_even_and_between_10_20(bilangan):
    print(f"{bilangan} adalah bilangan genap dan berada di antara 10 hingga 20.")
else:
    print(f"{bilangan} bukan bilangan antara 10 sampai 20 atau bilangan ganjil.")
