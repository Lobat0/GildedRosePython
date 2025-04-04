# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

#Implementando Testes TDD


def updater(obj: GildedRose, times: int = 1):
    for _ in range(times):
        obj.update_quality()

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_decreases_quality(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        updater(gilded_rose)

        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        updater(gilded_rose)

        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        updater(gilded_rose)

        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        updater(gilded_rose)

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_increases_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        updater(gilded_rose)

        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        #gilded_rose.update_quality()
        updater(gilded_rose)

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    #Criando teste para classe nova conjured que irá falhar

    def test_conjured_items_decrease_quality(self):
        items = [Item("Conjured Item", 3, 6)]
        gilded_rose = GildedRose(items)
    
        updater(gilded_rose)

        assert items[0].sell_in == 2
        assert items[0].quality == 4


"""
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)
"""
        
if __name__ == '__main__':
    unittest.main()
