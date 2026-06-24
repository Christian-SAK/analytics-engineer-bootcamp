# Semaine 1 — SQL fondamental

Apprendre SQL en pratiquant sur un cas **retail / e-commerce** réaliste : le benchmark **TPC-H** hébergé gratuitement sur Snowflake.

## Données utilisées

Base : `SNOWFLAKE_SAMPLE_DATA`  
Schéma : `TPCH_SF1` (scale factor 1 — ~6 M lignes dans LINEITEM)

| Table | Description | Lignes (approx.) |
|-------|-------------|------------------|
| `CUSTOMER` | Clients | 150 000 |
| `ORDERS` | Commandes | 1 500 000 |
| `LINEITEM` | Lignes de commande | 6 000 000 |
| `PART` | Articles / SKU | 200 000 |
| `SUPPLIER` | Fournisseurs | 10 000 |
| `PARTSUPP` | Stock fournisseur × article | 800 000 |
| `NATION` | Pays | 25 |
| `REGION` | Régions | 5 |

Vérification rapide :

```sql
USE DATABASE SNOWFLAKE_SAMPLE_DATA;
USE SCHEMA TPCH_SF1;
SELECT 'CUSTOMER' AS t, COUNT(*) AS n FROM CUSTOMER
UNION ALL SELECT 'ORDERS', COUNT(*) FROM ORDERS
UNION ALL SELECT 'LINEITEM', COUNT(*) FROM LINEITEM;
```

## Programme jour par jour

### Jour 1 — Premiers pas

- Créer un compte Snowflake trial si ce n'est pas fait
- Ouvrir **Worksheets** (ou SQL client)
- Concepts : `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`
- Types : VARCHAR, NUMBER, DATE
- **Analogie ESA** : `SELECT col FROM table WHERE ...` ≈ `df %>% select(col) %>% filter(...)`

**Exercices** : `exercices/ex-01-filtrer-clients.md`, `ex-02-tri-et-limites.md`

### Jour 2 — Agrégations

- `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- `GROUP BY`, `HAVING`
- **Analogie R** : `GROUP BY segment` ≈ `group_by(segment) %>% summarise(n = n())`

**Exercices** : `ex-03-agregations-segment.md`, `ex-04-having-ca-minimum.md`

### Jour 3 — Jointures simples

- `INNER JOIN`, `LEFT JOIN`
- Clés : `O_CUSTKEY`, `L_ORDERKEY`, etc.
- **Attention** : toujours qualifier les colonnes (`c.C_NAME`)

**Exercices** : `ex-05-join-orders-customer.md`

### Jour 4 — Jointures multiples

- Chaîne ORDERS → LINEITEM → PART
- Calcul marge : `(L_EXTENDEDPRICE * (1 - L_DISCOUNT)) - coût`
- Cardinalité : 1-N (commande → lignes)

**Exercices** : `ex-06-marge-par-fournisseur.md`

### Jour 5 — Sous-requêtes et CTE

- Sous-requête dans `WHERE` et `FROM`
- `WITH ... AS (...)` — **préféré en production**
- **Analogie** : CTE ≈ objet intermédiaire nommé en R

**Exercices** : `ex-07-cte-top-clients.md`

### Jour 6 — Fonctions fenêtre

- `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`
- `LAG()`, `LEAD()`, `SUM() OVER (PARTITION BY ... ORDER BY ...)`
- **Analogie R** : `lag(x, 1)` dans `dplyr::lag`

**Exercices** : `ex-08-fenetres-commandes.md`

### Jour 7 — Consolidation

- Mini-projet : dashboard SQL (5 requêtes liées)
- Révision jointures + fenêtres

**Exercices** : `ex-09-dashboard-retail.md`, `ex-10-bonus-tpcds.md`

## Modèle de données (simplifié)

```
CUSTOMER ──< ORDERS ──< LINEITEM >── PART
                              │
                         PARTSUPP >── SUPPLIER
NATION <── CUSTOMER / SUPPLIER
REGION <── NATION
```

## Conseils pratiques

1. **Toujours** `LIMIT 100` pendant l'exploration
2. Utiliser `DESCRIBE TABLE CUSTOMER;` pour voir les colonnes
3. Commenter vos requêtes (`-- insight recherché`)
4. Sauvegarder vos scripts dans `exercices/mes-reponses/`

## Ressources

- [`../ressources/datasets.md`](../ressources/datasets.md) — accès détaillé aux tables
- [`../ressources/glossaire.md`](../ressources/glossaire.md) — vocabulaire AE
- [`cours/`](cours/) — fiches mémo (à compléter au fil de l'eau)

## Livrable fin de semaine

Voir [`PROGRESSION.md`](../PROGRESSION.md) : rapport SQL 5 insights + dossier requêtes commentées.
