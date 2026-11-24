#!/usr/bin/env python3
"""Chronomètre MD5 vs bcrypt — labo J4, Sécurité des applications.

But pédagogique : SENTIR la différence de coût entre un hash rapide (MD5) et un
hash lent conçu pour les mots de passe (bcrypt). Ce n'est PAS un outil de craquage
industriel : la partie « cassage » ne fait qu'une recherche par dictionnaire sur
le petit fichier d'entraînement fourni.

Usage :
    python3 comparer-md5-bcrypt.py           # chronométrage + démo de cassage
    pip install bcrypt                       # pour la partie bcrypt (sinon ignorée)
"""
import hashlib
import time
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))


def chrono_md5(n=200_000):
    t = time.perf_counter()
    for i in range(n):
        hashlib.md5(f"mot{i}".encode()).hexdigest()
    d = time.perf_counter() - t
    return n, d, n / d


def chrono_bcrypt(n=50):
    try:
        import bcrypt
    except ImportError:
        return None
    sel = bcrypt.gensalt(rounds=10)
    t = time.perf_counter()
    for i in range(n):
        bcrypt.hashpw(f"mot{i}".encode(), sel)
    d = time.perf_counter() - t
    return n, d, n / d


def casser_md5(hashes_path, wordlist_path):
    """Recherche par dictionnaire sur les MD5 d'entraînement (démonstration)."""
    mots = [l.strip() for l in open(wordlist_path, encoding="utf-8") if l.strip()]
    table = {hashlib.md5(m.encode()).hexdigest(): m for m in mots}
    trouves, total = 0, 0
    for ligne in open(hashes_path, encoding="utf-8"):
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or ":" not in ligne:
            continue
        total += 1
        user, h = ligne.split(":", 1)
        if h in table:
            trouves += 1
            print(f"   {user:10s} -> {table[h]}")
        else:
            print(f"   {user:10s} -> (hors dictionnaire)")
    return trouves, total


def main():
    print("== Chronométrage ==")
    n, d, r = chrono_md5()
    print(f"MD5    : {n:,} hachages en {d:.3f}s  ->  {r:,.0f} hachages/seconde")

    bc = chrono_bcrypt()
    if bc is None:
        print("bcrypt : module absent. `pip install bcrypt` pour cette mesure.")
        print("         (Attendu : quelques dizaines à centaines de hachages/seconde,")
        print("          soit ~1 million de fois plus lent que MD5.)")
    else:
        n2, d2, r2 = bc
        print(f"bcrypt : {n2} hachages en {d2:.3f}s  ->  {r2:,.1f} hachages/seconde")
        print(f"\n   Rapport de vitesse : bcrypt est ~{r / r2:,.0f}x plus lent que MD5.")
        print("   Autrement dit, une attaque par force brute qui prend 1 seconde")
        print(f"   sur du MD5 prendrait ~{r / r2 / 86400:,.0f} JOURS sur du bcrypt.")

    print("\n== Démonstration de cassage (dictionnaire, sur le jeu d'entraînement) ==")
    hp = os.path.join(ICI, "hashes-juice-shop.txt")
    wp = os.path.join(ICI, "wordlist.txt")
    if not (os.path.exists(hp) and os.path.exists(wp)):
        print("   Fichiers d'entraînement introuvables à côté du script.")
        return
    t, tot = casser_md5(hp, wp)
    print(f"\n   {t}/{tot} mots de passe retrouvés avec la wordlist fournie.")
    print("   Les non-retrouvés ne sont pas dans la wordlist : une fuite n'est")
    print("   jamais cassée à 100 %. C'est la force de la liste qui compte, pas l'outil.")
    print("\n   À retenir : contre MD5, le dictionnaire suffit. Contre bcrypt, le même")
    print("   dictionnaire deviendrait impraticable — c'est pour ça qu'on hache lent.")


if __name__ == "__main__":
    sys.exit(main())
