#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:25:14 2020

@author: gmagroune
"""
from datetime import datetime
 
 
def proclamer():
    print( "[%s] Sam et Max, c'est bien", datetime.now())
 
 
if __name__ == "__main__":
    proclamer()