# Labo J4 — Hachage des mots de passe : MD5 vs bcrypt

Ce dossier accompagne le labo du J4 (**La Salle du Trésor**). Objectif : comprendre *pourquoi* un mot de passe ne se stocke jamais en clair ni avec un hash rapide, en le vivant plutôt qu'en l'écoutant.

> Les vrais hashes d'OWASP Juice Shop, vous les récupérerez **vous-même** sur votre instance locale pendant le labo. Les fichiers ci-dessous sont un jeu d'**entraînement** pour maîtriser le principe avant.

## Fichiers

| Fichier | Rôle |
|---|---|
| `hashes-juice-shop.txt` | 10 hashes **MD5 non salés** d'entraînement, format `utilisateur:hash`. |
| `wordlist.txt` | 15 mots de passe candidats. Elle couvre 8 des 10 comptes. |
| `comparer-md5-bcrypt.py` | Chronomètre MD5 vs bcrypt et fait une démo de cassage par dictionnaire. |

## Exercice (30 min)

1. **Cassez les MD5.** Lancez le script :
   ```bash
   python3 comparer-md5-bcrypt.py
   ```
   Combien de mots de passe retrouvez-vous ? Pourquoi pas les 10 ? Que faudrait-il pour avoir les deux manquants ?

2. **Mesurez l'écart MD5 / bcrypt.** Installez bcrypt (`pip install bcrypt`) et relancez. Notez les deux débits (hachages/seconde) et le rapport. Transposez : si casser un mot de passe MD5 prend *1 seconde*, combien de temps pour le même en bcrypt ?

3. **Concluez par écrit (quelques lignes).** Pour votre propre application (le rempart du jour) :
   - quel algorithme choisissez-vous (bcrypt, scrypt, argon2) et pourquoi ?
   - pourquoi le **sel** est indispensable même avec un hash lent ?
   - que fait le **facteur de coût** et comment le choisir ?

## Pour aller plus loin (si vous finissez tôt)

Récupérez quelques hashes sur **votre** instance Juice Shop locale et essayez-les avec la même wordlist. Comparez le format (type de hash, présence de sel) à ce que votre application produit. Rien ne sort de `127.0.0.1` : on n'attaque que sa propre machine (charte du J1).

## Rappel

MD5 et SHA-1 ne sont **pas** faits pour les mots de passe : trop rapides, donc trop faciles à attaquer en masse. Pour un mot de passe, on veut un hachage **lent, salé et paramétrable** (bcrypt / scrypt / argon2id).
