# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:48:33 2018

@author: alexa
"""

def calc_investment(initial, annual, time, rate):
   principal = initial + annual
   for i in range(time):
        total = (principal)*((1+rate))
        principal = total+annual
   return round(total, 2)


def salary_div(salary, percent):
    taxRate = 0.7
    afterTax = salary*taxRate
    savings = afterTax*percent
    return savings

calc_investment(10000, salary_div(75000, .1), 10, .06)