while True:
    print("Введи isikukood ниже: ")
    kod=input()
    pol=kod[0]
    date=kod[1:7] # берется от первой строки до 7-ой строки
    if int(pol)>=1 and int(pol) <=6 and len(kod)==11 and kod.isdigit():  # Проверка состоит ли строка из цифр
        year = int(date[0] + date[1])
        month = int(date[2] + date[3])
        day = int(date[4] + date[5])
        if int(pol) <= 4:
            year += 1900
        else:
            year += 2000
        if month > 12:
            date= "Ошибка"
        elif day > 31:
            date= "Ошибка"
        elif month == 2 and day > 29:
            date= "Ошибка"
        elif month % 2 == 1 and day > 30:
            date= "Ошибка"
        date= f"{day}/{month}/{year}"
        if int(pol) == 1 or int(pol) == 3 or int(pol) == 5:
            pol= "Мужской,"
        elif int(pol) == 2 or int(pol) == 4 or int(pol) == 6:
            pol= "Женский,"
        else:
            pol= "Неопределенный"
        print(f"Пол: {pol} родился {date}")
        controllisumm=kod[-1] # берет с конца
        n=1
        summa=0
        nomer=kod[0:10]
        for i in nomer:
            summa+=n*int(i)
            n+=1
            n%=10
            if n==0: n=1
        b=summa/11
        b=int(b)
        b*=11
        inm = int(kod[-4:-1])
        realkontrollisumm=summa-b
        if realkontrollisumm == int(controllisumm):
            print("Исикукод правильный")
        else: print("Исикукод неправильный")
        if inm >= 1 and inm <= 10:
            print("Kuressaare Haigla")
        elif inm >= 11 and inm <= 19:
            print("Tartu Ülikooli Naistekliinik, Tartumaa, Tartu")
        elif inm >= 21 and inm <= 220:
            print("Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla)")
        elif inm >= 221 and inm <= 270:
            print("Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)")
        elif inm >= 271 and inm <= 370:
            print("Narva Haigla")
        elif inm >= 371 and inm <= 420:
            print("Pärnu Haigla")
        elif inm >= 421 and inm <= 490:
            print("Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla")
        elif inm >= 491 and inm <= 520:
            print("Järvamaa Haigla (Paide)")
        elif inm >= 521 and inm <= 570:
            print("Rakvere, Tapa haigla")
        elif inm >= 571 and inm <= 600:
            print("Valga Haigla")
        elif inm >= 601 and inm <= 650:
            print("Viljandi Haigla")
        elif inm >= 651 and inm <= 700:
            print("Lõuna-Eesti Haigla (Võru), Põlva Haigla")
        else:
            print("Неизвестный род. дом!")
            

