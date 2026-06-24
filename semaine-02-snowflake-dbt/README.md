# Semaine 2 — Snowflake + dbt

Passer de requêtes ad hoc à un **projet de transformation** versionné, testé et documenté.

## Objectifs

- Comprendre l'architecture Snowflake (compte, warehouse, database, schema, rôle)
- Initialiser un projet **dbt** pointant vers TPCH (ou une copie dans votre schéma)
- Construire un **star schema** retail : dimensions + table de faits
- Écrire des **tests** (`unique`, `not_null`, `relationships`)
- Générer la **documentation** (`dbt docs`)

## Architecture cible

```
Sources (TPCH)          Staging (dbt)           Marts (dbt)
──────────────          ─────────────           ────────────
CUSTOMER         →      stg_tpch__customer  →   dim_customer
ORDERS           →      stg_tpch__orders    →   fct_orders
LINEITEM         →      stg_tpch__lineitem  →   (dans fct)
PART             →      stg_tpch__part      →   dim_part
```

## Programme jour par jour

| Jour | Contenu |
|------|---------|
| J8 | Compte Snowflake, warehouse `COMPUTE_WH`, rôles. Copier vs lire directement `SNOWFLAKE_SAMPLE_DATA` |
| J9 | `pip install dbt-snowflake`, `dbt init`, `profiles.yml`, `dbt debug` |
| J10 | Modèles staging : 1 fichier = 1 source, colonnes renommées en snake_case |
| J11 | `dim_customer`, `fct_orders` (grain : 1 ligne = 1 lineitem ou 1 order selon choix documenté) |
| J12 | `schema.yml` : tests PK/FK |
| J13 | Descriptions + `dbt docs generate && dbt docs serve` |
| J14 | Exercices + revue |

## Setup Snowflake

### Option A — Lire directement les samples (recommandé pour démarrer)

Pas de copie : dbt lit `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1` via `sources.yml`.

Accordez à votre rôle utilisateur `IMPORTED PRIVILEGES` sur la database sample (souvent déjà actif sur trial).

### Option B — Copier dans votre schéma dev

```sql
CREATE DATABASE AE_BOOTCAMP;
CREATE SCHEMA AE_BOOTCAMP.RAW;
CREATE TABLE AE_BOOTCAMP.RAW.CUSTOMER AS
  SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER;
-- Répéter pour ORDERS, LINEITEM, PART...
```

Utile si vous voulez simuler un vrai flux ingest.

## Setup dbt

```bash
cd semaine-02-snowflake-dbt/dbt-project
python -m venv .venv && source .venv/bin/activate
pip install dbt-snowflake

# Copier et remplir (NE PAS COMMITER profiles.yml)
cp profiles.yml.example ~/.dbt/profiles.yml
# Éditer account, user, password, role, warehouse

dbt debug
dbt deps   # si packages
dbt run
dbt test
```

## Projet fourni

Le squelette est dans [`dbt-project/`](dbt-project/) :

- `dbt_project.yml` — config projet
- `models/staging/` — modèles `stg_tpch__*`
- `models/marts/` — `dim_customer`, `fct_order_lines`
- `models/staging/sources.yml` — sources TPCH
- `models/marts/schema.yml` — tests

## Exercices

| Fichier | Sujet |
|---------|-------|
| [`exercices/ex-dbt-01-sources.md`](exercices/ex-dbt-01-sources.md) | Déclarer sources + freshness |
| [`exercices/ex-dbt-02-staging.md`](exercices/ex-dbt-02-staging.md) | Compléter staging manquant |
| [`exercices/ex-dbt-03-marts.md`](exercices/ex-dbt-03-marts.md) | Créer `dim_supplier` |
| [`exercices/ex-dbt-04-tests.md`](exercices/ex-dbt-04-tests.md) | Tests custom + singular |
| [`exercices/ex-dbt-05-docs.md`](exercices/ex-dbt-05-docs.md) | Documentation métier |

## Bonnes pratiques AE

1. **Staging** : renommer colonnes, caster types, pas de jointures lourdes
2. **Marts** : grain explicite dans le README ou description dbt
3. **Tests** : toute PK `unique` + `not_null`, FK `relationships`
4. **Matérialisation** : `view` en dev, `table` en prod (config dans `dbt_project.yml`)

## Livrable

Voir [`PROGRESSION.md`](../PROGRESSION.md) : projet dbt green + docs + diagramme star schema.
