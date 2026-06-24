# ex-01 — Filtrer les clients

## Contexte

Vous analysez la base clients TPCH pour un rapport segmentation.

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER`

## Énoncé

1. Affichez les colonnes `C_CUSTKEY`, `C_NAME`, `C_MKTSEGMENT`, `C_ACCTBAL` pour les clients du segment **'BUILDING'**.
2. Combien de clients sont dans ce segment ? (requête séparée ou sous-requête)
3. Quel est le solde compte (`C_ACCTBAL`) moyen de ce segment ?

## Critères

- Utiliser `WHERE` (pas de filtre post-agrégation)
- Résultat trié par solde décroissant, limité aux 20 premiers

## Indice ESA

Filtrer avant d'agréger = restreindre la population, comme exclure des outliers avant un `mean()` en R.

## Livrable

Requête(s) SQL commentée(s) dans `mes-reponses/ex-01.sql`.
