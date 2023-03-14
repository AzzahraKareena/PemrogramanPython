#!/usr/bin/env python
# coding: utf-8

# In[1]:


panjang = int(input('Masukkan panjang deret : '))

def fibonacci (n):
  if n < 1:
    return [n]

  listSebelumN = fibonacci(n - 1)
  angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
  angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

  print(listSebelumN)
 
  return listSebelumN + [angka1 + angka2]

print(fibonacci(10))


# In[ ]:





# In[ ]:




