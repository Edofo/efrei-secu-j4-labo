# Exercice — La clé enfouie (labo J4)

Un développeur a commité une clé d'API en dur, puis l'a « retirée » dans un commit suivant. Mais Git n'oublie rien : la clé vit toujours dans l'historique. Votre mission : la retrouver, puis expliquer quoi faire.

> Archive : `depot-cle-enfouie.tar.gz`. Elle contient le dépôt **avec son `.git`** — c'est l'historique qui compte, pas seulement les fichiers.

## Mise en place

```bash
tar xzf depot-cle-enfouie.tar.gz
cd depot-cle-enfouie
git log --oneline        # 5 commits
cat config.js            # la version actuelle ne contient PLUS la clé
```

La version courante lit la clé depuis l'environnement : tout semble propre. Pourtant la clé a existé dans le code. Retrouvez-la.

## À faire

1. **Retrouver la clé** avec, au choix :
   - un scanner de secrets :
     ```bash
     gitleaks detect --source . --no-banner
     ```
   - ou, sans rien installer, Git lui-même :
     ```bash
     git log -p | grep -n "sk_test"      # montre la ligne dans les diffs
     git log -S "sk_test" --oneline       # montre QUELS commits l'ont touchée
     git show <commit>                    # affiche le commit fautif
     ```
   La clé est de la forme `sk_test_EXERCICE_…` (clé d'exercice, inoffensive).

2. **Identifier** le commit qui l'a introduite et celui qui l'a « retirée ». La retirer de la version courante a-t-il suffi à la protéger ? Non — expliquez pourquoi.

3. **Rédiger la remédiation (quelques lignes).** Dans le bon ordre :
   - **révoquer / faire tourner** la clé côté fournisseur *d'abord* (une clé poussée un jour sur un dépôt est compromise, même privé, même supprimée ensuite) ;
   - purger l'historique si nécessaire (`git filter-repo`, BFG) — mais ça ne remplace pas la rotation ;
   - prévenir la récidive : secret hors du code (variables d'environnement / coffre), `.gitignore` sur `.env`, et un scanner de secrets en pre-commit ou en CI.

## À retenir

« Supprimer » un secret dans un commit ne le supprime pas de l'historique. La seule mesure qui protège vraiment, c'est **la rotation** : on considère la clé comme brûlée dès qu'elle a touché un dépôt.
