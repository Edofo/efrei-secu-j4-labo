# Jour 4 · La Salle du Trésor

**Objectif du jour** : protéger les données, en transit, au repos, et dans le dépôt.

## Au programme

- **Le matin** : hacher, chiffrer, encoder (Base64 n'est pas du chiffrement), MD5 contre bcrypt, le chiffrement au repos en AES-256-GCM, HTTPS et les certificats, les en-têtes de sécurité, CORS, les secrets dans Git, la SSRF, le RGPD.
- **L'après-midi** : vous passez votre application en HTTPS local, ajoutez les en-têtes, et chiffrez votre champ sensible.

## Le labo du jour

Dans `labo/` : des hachages à casser et un comparateur MD5 / bcrypt, et un dépôt où une clé est cachée dans l'historique Git (à retrouver avec gitleaks ou `git log`). Suivez le README du labo.

## Le défi du jour

**La Fuite** (`/fuite` sur la cible). Un dump fictif a fuité : craquez le maximum de mots de passe, puis rédigez la notification à la CNIL (nature, DPO, conséquences, mesures).
