#!/usr/bin/env python
# coding: utf-8

# In[7]:


def hitung_huruf_besar(teks):
    
    jumlah_huruf_besar = 0
    for karakter in teks:
        if karakter.isupper():
            jumlah_huruf_besar += 1
    return jumlah_huruf_besar

