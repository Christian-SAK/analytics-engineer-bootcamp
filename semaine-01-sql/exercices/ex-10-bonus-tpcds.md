# ex-10 — Bonus : introduction TPC-DS (optionnel)

## Contexte

Snowflake expose aussi **TPC-DS** (retail plus riche, modèle dimensionnel). Exploration optionnelle si vous terminez la semaine en avance.

## Tables

- Schéma : `SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL`
- Exemples : `STORE_SALES`, `DATE_DIM`, `CUSTOMER`, `ITEM`

## Énoncé

1. Vérifiez l'accès : `SELECT COUNT(*) FROM SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.STORE_SALES;`
2. CA total par année (`D_YEAR` via jointure `DATE_DIM`)
3. Comparez la structure TPC-DS (tables `DATE_DIM`, `ITEM`) vs TPCH — quelle est plus proche d'un entrepôt analytique ?

## Critères

- Documentez vos observations dans un commentaire
- Pas obligatoire pour valider la semaine 1

## Livrable

`mes-reponses/ex-10-bonus-tpcds.sql` (optionnel)
