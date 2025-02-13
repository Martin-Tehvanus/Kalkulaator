import math # impordib math mooduli


class cal(): # teeb cal (kalkulaatori klassi)
    def __init__(self,a,b):             # defineerib cal klassi
        self.a = a # määrab self.a muutujaks a
        self.b = b # määrab self.b muutujaks b

# Kalkulaatori funktsioonid
    def liitmine(self):        # teeb funktsiooni liitmine
        return self.a + self.b # liidab kasutaja poolt sisestatud a ja b ning kuvab tulemuse
    def lahutamine(self):      # teeb funktsiooni lahutamine
        return self.a - self.b # lahutab kasutaja poolt sisestatud arvust a arvu b ning kuvab tulemuse
    def korrutamine(self):     # teeb funktsiooni korrutamine
        return self.a * self.b # korrutab kasutaja poolt sisestatud a arvuga b ning kuvab tulemuse
    def jagamine(self):        # # teeb funktsiooni jagamine
        return self.a / self.b # jagab kasutaja poolt sisestatud a arvuga b ning kuvab tulemuse
    def jaak(self):            # teeb funktsiooni jaak (jääk)
        return self.a % self.b # leiab kasutaja poolt sisestatud a ja b jäägi ning kuvab tulemuse
    def ruutjuur(self):        # teeb funktsiooni ruutjuur
        return math.sqrt(self.a) # leiab kasutaja poolt sisestatud a arvust ruutjuure ning kuvab tulemuse
    def astendamine(self):
        return  self.a ** self.b

# Inputid
a = int(input("Sisesta esimene number: "))          # küsib kasutaja käest arvu a
b = int(input("Sisesta teine number: "))            #küsib kasutaja käest arvu b

kalk = cal(a,b) # määrab calc(a,b) lühendiks kalk, et saaks kalk kasutada ja ei peaks koguaeg välja kirjutama cal()

#Kalkulaatori tulemused
while True: # Kui tõene siis teeb järgmist:
    def menu(): # teeb menu (menüü) funktsiooni
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n7 Astendamine. ') # määrab selle sõne x'i väärtuseks
        print(x) # prindib x väärtuse
    menu() # saadab käsu et käivitada/kuvada menu
    valik = int(input('Sisesta üks valikutest: ')) # küsib kasutaja käest numbrilist inputi
    if valik == 1: # kui valiku arv on 1 siis teeb järgmist
        print("Vastus: ",kalk.liitmine()) # prindib Vastus: (liitmise tulemus)
        break # lõpetab programmi
    elif valik == 2: # kui valitud arv on 2 siis teeb järgmist:
        print("Vastus: ",kalk.lahutamine()) # prindib Vasuts: (vahe/lahutamise tulemus)
        break # lõpetab programmi
    elif valik == 3: # kui valitud arv on 3 siis teeb järgmist:
        print("Vastus: ",kalk.korrutamine()) # prindib Vastus: (korrutamise tulemus)
        break # lõpetab programmi
    elif valik == 4: # kui valitud arv on 4 siis teeb järgmist:
        print("Vastus: ",kalk.jagamine()) # prindib Vasuts: (jagamise tulemus)
        break # lõpetab programmi
    elif valik == 5: # kui valitud arv on 5 siis teeb järgmist:
        print("Vastus: ",kalk.jaak()) # prindib Vasuts: (jäägi tulemuse)
        break # lõpetab programmi
    elif valik == 6: # kui valitud arv on 6 siis teeb järgmist:
        print("Vastus: ",kalk.ruutjuur()) # prindib Vasuts: (esimese arvu ruutjuur)
        break # lõpetab programmi
    elif valik == 7: # # kui valitud arv on 6 siis teeb järgmist:
        print("Vastus", kalk.astendamine()) # prindib Vasuts: (astendamise tulemus)
        break # lõpetab programmi
    elif valik == 0: # kui valitud arv on 0 siis teeb järgmist:
        print('Sisesta uuesti üks liitmise operaator') # prndib Sisesta uuesti üks liitmise operaator
        break # lõpetab programmi




