# 2-misol
class MenuItem:
    def __init__(self, nomi):
        self.nomi = nomi

    def tayyorlash_vaqti(self):
        raise NotImplementedError

    def narx_hisoblash(self, miqdor):
        raise NotImplementedError

    def allergiya_tekshirish(self, ingredient):
        return False     


class Ovqat(MenuItem):
    def __init__(self, nomi, asosiy_ingredientlar):
        super().__init__(nomi)
        self.ingredientlar = asosiy_ingredientlar

    def tayyorlash_vaqti(self):
        return 20  # daqiqa

    def narx_hisoblash(self, miqdor):
        return miqdor * 30000

    def allergiya_tekshirish(self, ingredient):
        return ingredient.lower() in [i.lower() for i in self.ingredientlar]


class Ichimlik(MenuItem):
    def tayyorlash_vaqti(self):
        return 5

    def narx_hisoblash(self, miqdor):
        return miqdor * 10000


class Desert(MenuItem):
    def tayyorlash_vaqti(self):
        return 10

    def narx_hisoblash(self, miqdor):
        return miqdor * 15000


def buyurtma_hisobla(menyu, buyurtmalar):
    """
    buyurtmalar -> { nomi: miqdor }
    menyu -> MenuItem obyektlari ro'yxati
    """
    umumiy_vaqt = 0
    umumiy_narx = 0

    for item in menyu:
        if item.nomi in buyurtmalar:
            miqdor = buyurtmalar[item.nomi]
            umumiy_vaqt += item.tayyorlash_vaqti()
            umumiy_narx += item.narx_hisoblash(miqdor)

    return umumiy_vaqt, umumiy_narx


menyu = [
    Ovqat("Lagman", ["go'sht", "un", "tuz"]),
    Ichimlik("Cola"),
    Desert("Cheesecake")
]

buyurtma = {
    "Lagman": 2,
    "Cola": 3,
    "Cheesecake": 1
}

vaqt, narx = buyurtma_hisobla(menyu, buyurtma)

print("Umumiy tayyorlash vaqti:", vaqt, "daq")
print("Umumiy narx:", narx, "so'm")

# Allergiya tekshiruvi test
print("Lagman allergiya (tuz):", menyu[0].allergiya_tekshirish("tuz"))
print("Cola allergiya (shakar):", menyu[1].allergiya_tekshirish("shakar"))
