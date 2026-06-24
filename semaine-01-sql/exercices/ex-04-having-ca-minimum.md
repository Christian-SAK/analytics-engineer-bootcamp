# ex-04 — HAVING : segments à fort CA

## Contexte

On ne retient que les segments « significatifs » côté volume client.

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER`

## Énoncé

1. Affichez les segments (`C_MKTSEGMENT`) ayant **strictement plus de 30 000 clients**.
2. Pour ces segments uniquement, affichez aussi le solde moyen.

## Critères

- Différencier `WHERE` (filtre lignes) et `HAVING` (filtre groupes)
- Une seule requête

## Question de réflexion

Pourquoi ne peut-on pas écrire `WHERE COUNT(*) > 30000` ?

## Livrable

`mes-reponses/ex-04.sql` + réponse courte en commentaire SQL.
