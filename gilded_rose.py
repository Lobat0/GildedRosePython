# -*- coding: utf-8 -*-

#Criação de uma clase updater para gerenciar melhor cada um dos itens

class Updater:
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def normal_item(self, item):
        depreciation = -1 if item.sell_in > 0 else -2
        item.quality = max(item.quality + depreciation, self.MIN_QUALITY)
        item.sell_in -= 1

    def aged_brie(self, item):
        appreciation = 1 if item.sell_in > 0 else 2
        item.quality = min(item.quality + appreciation, self.MAX_QUALITY)
        item.sell_in -= 1

    def sulfuras(self, item):
        pass

    def backstage_passes(self, item):
        if item.sell_in > 10:
            appreciation = 1
        elif item.sell_in > 5:
            appreciation = 2
        elif item.sell_in > 0:
            appreciation = 3
        else:
            item.quality = 0
            item.sell_in -= 1
            return
        
        item.quality = min(item.quality + appreciation, self.MAX_QUALITY)
        item.sell_in -= 1

    def conjured(self, item):
        depreciation = -2 if item.sell_in > 0 else -4
        item.quality = max(item.quality + depreciation, self.MIN_QUALITY)
        item.sell_in -= 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.updater = Updater()

    
    #Com a logica na classe updater, agora é deixar essa classe menor e facil de manutenção
    def update_quality(self):
        for item in self.items:            
            if item.name == "Aged Brie":
                self.updater.aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.updater.backstage_passes(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.updater.sulfuras(item)
            elif "Conjured" in item.name:
                self.updater.conjured(item)
            else:
                self.updater.normal_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)




