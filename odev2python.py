# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28
mesafe=int(input("Gitmek istediğiniz mesafeyi seçiniz:"))
yakıt=input("Hangi tür yakıt kullandığınızı seçiniz:")
print("-----benzin,dizel,lpg-----")
if(yakıt=="benzin"):
    print("Yakıt masrafınız:"+str(mesafe*39.35)+"TL")
elif(yakıt=="dizel"):
    print("Yakıt masrafınız:"+str(mesafe*41.71)+"TL")
elif(yakıt=="lpg"):
    print("Yakıt masrafınız:"+str(mesafe*20.28)+"TL")
# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC
vize1=int(input("1.vize notunuzu giriniz:"))
vize2=int(input("2.vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))
ortalama=(vize1+vize2+final)/3
if (ortalama>=90 and ortalama<=100):
   print("Harf notunuz:AA")
elif (ortalama>=80 and ortalama<=89):
   print("Harf notunuz:BA")
elif (ortalama>=70 and ortalama<=79):
   print("Harf notunuz:BB")
elif (ortalama>=60 and ortalama<=69):
   print("Harf notunuz:CB")
elif (ortalama>=50 and ortalama<=59):
   print("Harf notunuz:CC")
elif (ortalama>=40 and ortalama<=49):
   print("Harf notunuz:DC")
elif(ortalama>0 and ortalama <=39):
   print("Kaldınız!")