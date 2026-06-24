# Analytics Engineer Bootcamp — 3 semaines

Parcours intensif pour devenir **Analytics Engineer** : SQL → Snowflake/dbt → Airflow.

## Public cible

Ce bootcamp s'adresse à un profil **Master ESA (Économétrie / Statistique Appliquée)** qui maîtrise déjà :

- La statistique descriptive et inférentielle
- R ou Python pour l'analyse de données
- Les notions de régression, tests d'hypothèses, séries temporelles

**Sans prérequis SQL.** L'approche pédagogique fait des ponts explicites avec R (`dplyr`, `group_by`, `lag`/`lead`) pour accélérer l'apprentissage.

## Objectifs du parcours

À l'issue des 3 semaines, vous serez capable de :

1. **Interroger** des bases relationnelles en SQL (jointures, agrégations, fenêtres)
2. **Modéliser** des données analytiques en schéma en étoile avec **dbt** sur **Snowflake**
3. **Orchestrer** un pipeline de transformation (dbt run + dbt test) avec **Apache Airflow**
4. **Documenter** et **tester** vos modèles comme le ferait un praticien en entreprise

## Fil rouge : analyse e-commerce / retail

Tout le parcours s'appuie sur les données **TPC-H** (benchmark retail) disponibles gratuitement sur Snowflake :

> `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1`

Vous analyserez clients, commandes, articles, fournisseurs et marges — un cas d'usage cohérent du jour 1 au projet final.

## Prérequis

| Prérequis | Détail |
|-----------|--------|
| Compte Snowflake | [Essai gratuit 30 jours](https://signup.snowflake.com/) — région au choix |
| Git | Installé et configuré (`git config user.name`, `user.email`) |
| Python 3.10+ | Pour dbt-core et Airflow (semaine 2-3) |
| 15-20 h/semaine | Rythme intensif recommandé |

Optionnel mais utile : un éditeur SQL (DBeaver, Snowflake Worksheets), VS Code avec extension dbt.

## Structure du dépôt

```
analytics-engineer-bootcamp/
├── README.md                 ← Vous êtes ici
├── PROGRESSION.md            ← Checklist jour par jour
├── semaine-01-sql/           ← SQL fondamental sur TPCH
├── semaine-02-snowflake-dbt/ ← Modélisation dbt + Snowflake
├── semaine-03-airflow-projet/← Orchestration + projet final
├── ressources/               ← Liens, glossaire, datasets
└── solutions/                ← Corrigés (sur demande formateur)
```

## Comment utiliser le parcours

1. **Lisez** `PROGRESSION.md` pour la vue d'ensemble des 3 semaines
2. **Semaine 1** : Suivez `semaine-01-sql/README.md` jour par jour ; faites les exercices dans `exercices/`
3. **Semaine 2** : Configurez Snowflake + dbt (`semaine-02-snowflake-dbt/`) ; transformez TPCH en star schema
4. **Semaine 3** : Déployez Airflow en local (Docker) ; livrez le projet final
5. **Consultez** `ressources/` en cas de blocage (glossaire, liens, guide datasets)

### Conventions

- Les exercices sont numérotés `ex-01`, `ex-02`, … avec un énoncé clair
- Les corrigés ne sont **pas** dans ce dépôt (voir `solutions/`)
- Chaque semaine se termine par des **livrables** et des **critères de validation** (voir `PROGRESSION.md`)

## Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/Christian-SAK/analytics-engineer-bootcamp.git
cd analytics-engineer-bootcamp

# Vérifier l'accès aux données Snowflake (dans une worksheet)
SELECT COUNT(*) FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER;
```

Si la requête retourne un nombre > 0, vous êtes prêt pour la semaine 1.

## Stack technique

| Outil | Rôle |
|-------|------|
| **Snowflake** | Entrepôt de données cloud |
| **dbt** | Transformation SQL, tests, documentation |
| **Airflow** | Orchestration de pipelines |

## Licence et usage

Contenu pédagogique personnel. Les datasets Snowflake sample restent soumis aux conditions d'utilisation Snowflake.

---

**Bon bootcamp !** Commencez par [`PROGRESSION.md`](PROGRESSION.md).
