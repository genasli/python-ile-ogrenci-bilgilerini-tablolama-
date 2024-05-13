Liste = []
Adı = "Adı"
Soyadı = "Soyadı"
Numarası = "Numarası"
Notu = "Notu"
while True:
    adı = input("Öğrencinin adını giriniz : ")
    soyadı = input("Öğrencinin soyadını giriniz : ")
    numarası = input("Öğrencinin numarasını giriniz : ")
    notu = input("Öğrencinin notunu giriniz : ")
    demet = (adı,soyadı,numarası,notu)
    Liste.append(demet)
    i = input("Öğrenci bilgisi girmeye devam etmek istiyormusun ? (evet/hayır) : ")
    i.lower()
    if i == "hayır":
        break
print("{:->73s}".format("-"))
print("| {:^15s} | {:^15s} | {:<15s} | {:^15s} |".format(Adı,Soyadı,Numarası,Notu))
print("{:->73s}".format("-"))
        
for i,j,k,l in Liste: 
    
    print("| {:^15s} | {:^15s} | {:<15s} | {:^15s} |".format(i,j,k,l))
    print("{:->73s}".format("-"))
        
