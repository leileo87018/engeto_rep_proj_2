"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Leoš Leitgeb
email: leitgebl@seznam.cz
"""

# Program >>>
# 1. Pozdrav a tisk úvodního textu

print(f"""Hi there!
{47 * '-'}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game
{47 * '-'}
Enter a number:
{47 * '-'}""")

# 2. Vytvoření tajného čísla
"""
Náhodné generování 4 jedinečných číslic, nezačínající 0,
použití knihovny random, výstupem řetězec obsahující nahodne_cislo
"""

import random

while True:
    nahodne_cislo = ''.join(random.sample('0123456789', 4))
    if nahodne_cislo[0] != '0':
      break

# print(f"nahodne_cislo: {nahodne_cislo} \n{47 * '-'}") # kontrolní tisk

# 3. Zadání čísla s ověřením požadovaného formátu
"""
Viz docstring (dokumentační řetězec) u funkce zadani_s_overenim() níže
"""

def zadani_s_overenim():
  """
  Výzva k zadání čísla s ověřením zadání 4 jedinečných číslic, nezačínající 0

  Funkce bez parametrů pro zadání čísla s ověřením požadovaného formátu,
  vrací pouze správnou hodnotu. Pokud je zadán chybný formát, funkce oznámí
  chybu a opakuje výzvu k zadání čísla, dokud není zadán správný formát.

  Ověření formátu:
    1. kontrola délky
    2. počátečního znaku s 0
    3. typu číslo
    4. jedinečnosti čísel

  Návratová hodnota:
    tip: řetězec čísel splňující parametry zadání
  """
  while True:
    tip = input(">>> ")
    if len(tip) != 4 or tip[0] == '0' or not tip.isdigit() or len(set(tip)) != 4:
      print(
      "Incorrect, enter a unique four-digit number \nnot starting with zero"
      )
      print(47 * "-")
    else:
      break
  return tip

# 4a. Ověření počtu shody čísla a umístění - Bulls
"""
Viz docstring (dokumentační řetězec) u funkce spocitej_bulls níže
"""
def spocitej_bulls(nahodne_cislo, tip_final):
  """
  Výpočet počtu shody čísla a umístění číslic

  Funkce přijímá dva číselné řetězce jako vstupní parametry a provede
  porovnání na shodu číslic a umístění. Pro vyhodnocení tzv "Bulls".

  Parametry:
    nahodne_cislo_t: 1. řetězec k porovnání
    tip_final: 2. řetězec k porovnání

  Návratová hodnota:
    bulls: počet shod číslic a umístění
  """
  bulls = 0

  for index_b, x in enumerate(nahodne_cislo):
    if tip_final[index_b] == x:
      bulls += 1
  return bulls

# 4b. Ověření počtu výskytu čísla bez umístění - Cows
"""
Viz docstring (dokumentační řetězec) u funkce spocitej_cows níže
"""

def spocitej_cows (nahodne_cislo, tip_final):
  """
  Výpočet počtu shody čísla bez umístění číslic

  Funkce přijímá dva číselné řetězce jako vstupní parametry a
  porovná je na shodu číslic. Pro vyhodnocení tzv "Cows".

  Parametry:
    nahodne_cislo: 1. řetězec k porovnání
    tip_final: 2. řetězec k porovnání

  Návratová hodnota:
    cows: počet shod výskutu číslic
  """
  cows = 0

  for cislo in tip_final:
    if cislo in nahodne_cislo:
      cows += 1
  return cows

  # 5. Vyhodnocení shody s náhodným číslem, či Bulls/Cows s počítáním pokusů
"""
Použití smyčky while , volání funkcí zadani_s_overenim, ověření přímé shody,
funkcí spocitej_bulls a spocitej_cows, s počítáním pokusů guesses
tisk shody, či počtu bulls/cows výstupem z uživatelských funkcí
"""
guesses = 0

while True:
  guesses += 1
  tip_final = zadani_s_overenim()
  if tip_final == nahodne_cislo:
    print(f"Correct, you've guessed the right number\nin {guesses} guesses!")
    print(47 * '-')
    break
  else:
    bulls_final = spocitej_bulls(nahodne_cislo, tip_final)
    cows_final = spocitej_cows(nahodne_cislo, tip_final)
    print(f"{bulls_final} bull{'s' if bulls_final != 1 else ''}, " \
          f"{cows_final} cow{'s' if cows_final != 1 else ''}")
    print(47 * '-')
print("That's amazing!")