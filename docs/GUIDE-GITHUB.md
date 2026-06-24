# Guide GitHub — Fork, clone et Pull Request

Ce guide vous accompagne pas à pas pour **contribuer au bootcamp** : rendre vos exercices, partager vos livrables et proposer des améliorations — sans avoir besoin d'être développeur·se.

> **Objectif** : travailler sur **votre copie** du dépôt, puis proposer vos changements au dépôt principal via une **Pull Request** (PR).

---

## C'est quoi un fork ?

Imaginez un **cahier d'exercices officiel** dans une bibliothèque. Vous ne pouvez pas écrire directement dedans.

Un **fork**, c'est **photocopier ce cahier et le ramener chez vous**. Vous y notez vos réponses tranquillement. Quand vous voulez rendre votre travail, vous demandez au bibliothécaire (le dépôt **upstream**) de **relire votre copie** et d'en intégrer les bonnes parties.

En résumé :

| Terme | Signification simple |
|-------|----------------------|
| **Upstream** | Le dépôt original (`Christian-SAK/analytics-engineer-bootcamp`) |
| **Origin** | **Votre** fork sur GitHub (ex. `SON-PSEUDO/analytics-engineer-bootcamp`) |
| **Fork** | Votre copie personnelle du dépôt sur GitHub |
| **Pull Request (PR)** | Demande : « Pouvez-vous intégrer mes changements dans le dépôt principal ? » |

---

## Prérequis

Avant de commencer, vérifiez que vous avez :

| Prérequis | Comment vérifier / obtenir |
|-----------|----------------------------|
| **Compte GitHub** | Créez-en un sur [github.com](https://github.com/signup) si besoin |
| **Git installé** | Ouvrez un terminal et tapez `git --version` — une version doit s'afficher |
| **Accès Internet** | Pour fork, clone et push |

### Installer Git (si nécessaire)

- **Windows** : [git-scm.com/download/win](https://git-scm.com/download/win)
- **macOS** : `xcode-select --install` ou [git-scm.com/download/mac](https://git-scm.com/download/mac)
- **Linux (Debian/Ubuntu)** : `sudo apt update && sudo apt install git`

---

## Vue d'ensemble du flux

```
  Dépôt upstream (Christian-SAK)          Votre fork (SON-PSEUDO)
  ┌─────────────────────────┐             ┌─────────────────────────┐
  │ analytics-engineer-     │   Fork      │ analytics-engineer-     │
  │ bootcamp (original)     │ ──────────► │ bootcamp (votre copie)  │
  └───────────▲─────────────┘             └───────────┬─────────────┘
              │                                       │
              │         Pull Request (PR)               │ git push
              │    « Merci d'intégrer mes changements »│
              └───────────────────────────────────────┘
                                    ▲
                                    │
                          Votre machine (clone local)
                          branche → commit → push
```

---

## Étape 1 — Forker le dépôt

1. Ouvrez le dépôt principal : **[github.com/Christian-SAK/analytics-engineer-bootcamp](https://github.com/Christian-SAK/analytics-engineer-bootcamp)**
2. Cliquez sur le bouton **Fork** (en haut à droite)
3. Choisissez **votre compte** GitHub comme destination
4. Attendez quelques secondes : GitHub crée `https://github.com/SON-PSEUDO/analytics-engineer-bootcamp`

> Remplacez `SON-PSEUDO` par **votre** identifiant GitHub partout dans ce guide.

---

## Étape 2 — Cloner **votre** fork (pas l'upstream)

Sur **votre machine**, clonez **votre fork** — pas le dépôt de Christian-SAK.

```bash
git clone https://github.com/SON-PSEUDO/analytics-engineer-bootcamp.git
cd analytics-engineer-bootcamp
```

Vérifiez que `origin` pointe bien vers **votre** fork :

```bash
git remote -v
```

Vous devez voir quelque chose comme :

```
origin  https://github.com/SON-PSEUDO/analytics-engineer-bootcamp.git (fetch)
origin  https://github.com/SON-PSEUDO/analytics-engineer-bootcamp.git (push)
```

---

## Étape 3 — Configurer Git (une seule fois)

Git a besoin de savoir **qui** commit. À faire **une fois** par machine :

```bash
git config --global user.name "Votre Prénom Nom"
git config --global user.email "votre.email@exemple.com"
```

Utilisez l'**adresse e-mail associée à votre compte GitHub** (Settings → Emails).

Vérification :

```bash
git config --global user.name
git config --global user.email
```

---

## Étape 4 — Travailler sur une branche

Ne travaillez **pas** directement sur `main`. Créez une **branche** par exercice, semaine ou livrable.

### 4.1 Créer et basculer sur une branche

```bash
git checkout -b semaine-01-ex-03
```

Nommez la branche de façon claire, par exemple :

- `semaine-01-ex-03`
- `semaine-02-dbt-staging`
- `projet-final-livrable`

### 4.2 Faire vos modifications

Éditez les fichiers (exercices, réponses SQL, captures, etc.) dans votre éditeur habituel.

### 4.3 Enregistrer vos changements (commit)

```bash
# Voir ce qui a changé
git status

# Ajouter les fichiers modifiés
git add semaine-01-sql/exercices/mes-reponses/

# Ou ajouter un fichier précis
git add semaine-01-sql/exercices/mes-reponses/ex-03.sql

# Créer un commit avec un message clair
git commit -m "Semaine 1 — exercice 03 : agrégations par segment"
```

### 4.4 Envoyer la branche vers **votre** fork

```bash
git push -u origin semaine-01-ex-03
```

La première fois sur une branche, `-u origin nom-branche` mémorise le lien pour les prochains `git push`.

---

## Étape 5 — Ouvrir une Pull Request vers upstream

1. Allez sur **votre fork** : `https://github.com/SON-PSEUDO/analytics-engineer-bootcamp`
2. GitHub affiche souvent une bannière **Compare & pull request** après un push — cliquez dessus
3. Sinon : onglet **Pull requests** → **New pull request**
4. Vérifiez la direction :
   - **base** (destination) : `Christian-SAK/analytics-engineer-bootcamp` → branche `main`
   - **compare** (source) : `SON-PSEUDO/analytics-engineer-bootcamp` → **votre branche**
5. Rédigez un titre et une description clairs (ex. « Semaine 1 — ex-03 agrégations »)
6. Cliquez sur **Create pull request**

Vous avez demandé une relecture / intégration de votre travail. C'est normal si la PR reste ouverte un moment.

---

## Étape 6 — Rester synchronisé avec upstream

Le dépôt principal évolue (nouveaux exercices, corrections). Pour récupérer ces mises à jour **sans perdre votre travail** :

### 6.1 Ajouter upstream (une seule fois)

```bash
git remote add upstream https://github.com/Christian-SAK/analytics-engineer-bootcamp.git
git remote -v
```

Vous devez maintenant voir `origin` (votre fork) **et** `upstream` (l'original).

### 6.2 Récupérer et fusionner les nouveautés

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

Ensuite, sur **votre branche de travail** :

```bash
git checkout semaine-01-ex-03
git merge main
# Résolvez les conflits si Git vous le demande, puis :
git push origin semaine-01-ex-03
```

> **Astuce** : synchronisez `main` depuis upstream **régulièrement** (début de semaine) pour éviter les gros conflits.

---

## Erreurs fréquentes

| Message / symptôme | Cause probable | Solution |
|--------------------|----------------|----------|
| `Permission denied (publickey)` ou `Authentication failed` | Clé SSH absente ou mauvais identifiants HTTPS | Utilisez l'URL HTTPS et un **Personal Access Token** (GitHub → Settings → Developer settings → Tokens), ou configurez une clé SSH |
| `remote: Repository not found` | URL de clone incorrecte ou dépôt privé sans accès | Vérifiez que vous clonez **votre fork** : `SON-PSEUDO/analytics-engineer-bootcamp` |
| `Updates were rejected` au push | La branche distante a des commits que vous n'avez pas | `git pull origin nom-branche` puis corrigez les conflits et `git push` |
| PR créée depuis le mauvais dépôt | Vous avez poussé sur upstream au lieu de origin | Vous ne pouvez pas pousser sur upstream sans droits ; clonez **votre fork** et poussez vers `origin` |
| `Please tell me who you are` | `user.name` / `user.email` non configurés | Étape 3 ci-dessus |
| `fatal: not a git repository` | Vous n'êtes pas dans le dossier du projet | `cd analytics-engineer-bootcamp` |
| Conflits au merge | Même ligne modifiée upstream et chez vous | Ouvrez les fichiers marqués, choisissez la bonne version, `git add`, puis `git commit` |

---

## Bonnes pratiques pour le bootcamp

- **Une branche par livrable** (exercice, semaine, projet final) — plus simple à relire et à corriger
- **Messages de commit explicites** : « Semaine 2 — ex-dbt-02 staging orders » plutôt que « fix » ou « update »
- **Petits commits réguliers** plutôt qu'un seul gros commit en fin de semaine
- **Synchronisez upstream** avant de démarrer une nouvelle semaine
- **Ne commitez pas** de mots de passe Snowflake, tokens ou clés API — utilisez des fichiers `.example` ou des variables d'environnement locales

---

## Récapitulatif des commandes essentielles

```bash
# Setup (une fois)
git clone https://github.com/SON-PSEUDO/analytics-engineer-bootcamp.git
cd analytics-engineer-bootcamp
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"
git remote add upstream https://github.com/Christian-SAK/analytics-engineer-bootcamp.git

# Boucle de travail
git checkout -b ma-branche
# ... modifications ...
git add .
git commit -m "Description claire du changement"
git push -u origin ma-branche
# → Ouvrir une PR sur GitHub

# Rester à jour
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

---

**Vous bloquez ?** Reprenez depuis l'étape indiquée dans le message d'erreur, ou demandez de l'aide en citant la commande exacte et le message complet. Chaque apprenant·e a commencé par un premier `git clone` — vous y arriverez.
