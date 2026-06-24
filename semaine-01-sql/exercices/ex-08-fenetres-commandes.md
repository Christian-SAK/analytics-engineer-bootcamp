# ex-08 — Fonctions fenêtre : historique commandes

## Contexte

Analyser la cadence d'achat par client (rétention / réachat).

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS`

## Énoncé

Pour chaque client (`O_CUSTKEY`), sur ses commandes ordonnées par date :

1. `num_commande` : numéro de commande (1, 2, 3…) via `ROW_NUMBER()`
2. `jours_depuis_precedente` : écart en jours avec la commande précédente (`LAG(O_ORDERDATE)`)
3. `ca_cumule_client` : CA cumulé (`SUM(O_TOTALPRICE) OVER (...)`)

Filtrez finalement les clients ayant **au moins 5 commandes** (utilisez une CTE ou sous-requête).

## Critères

- `PARTITION BY O_CUSTKEY ORDER BY O_ORDERDATE`
- Afficher un échantillon : `LIMIT 50` après filtrage

## Analogie R

```r
orders %>% arrange(O_CUSTKEY, O_ORDERDATE) %>%
  group_by(O_CUSTKEY) %>%
  mutate(num = row_number(), lag_date = lag(O_ORDERDATE))
```

## Livrable

`mes-reponses/ex-08.sql`
