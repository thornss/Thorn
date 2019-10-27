# -*- coding: utf-8 -*-
import itertools

#main_word = ["постельное белье"]
main_word_attributes = ["детское", "1,5 спальное"]
commercial = ["купить", "цена"]
theme = ["star wars", "звездные войны"]
variants = ["yoda", "йода", "darth vader", "дарт вейдер"]


t = itertools.combinations(main_word_attributes + commercial + theme + variants, 1)
for a, *b in t:
    print("постельное белье", a, ' '.join(map(str, b)))
    
t2 =itertools.combinations(commercial + theme + variants, 1)
for a, *b in t2:
    print("комплект детского постельного белья", a, ' '.join(map(str, b)))