# ex-03 — Agrégations par segment marketing

## Contexte

Le marketing souhaite comparer les segments clients.

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER`

## Énoncé

Produisez un tableau avec pour chaque `C_MKTSEGMENT` :

| Métrique | Colonne résultat suggérée |
|----------|---------------------------|
| Nombre de clients | `nb_clients` |
| Solde moyen | `solde_moyen` |
| Solde total | `solde_total` |
| Solde min / max | `solde_min`, `solde_max` |

Triez par `solde_total` décroissant.

## Critères

- `GROUP BY C_MKTSEGMENT`
- Arrondir les montants à 2 décimales (`ROUND(..., 2)`)

## Analogie R

```r
customer %>% group_by(C_MKTSEGMENT) %>%
  summarise(nb_clients = n(), solde_moyen = mean(C_ACCTBAL), ...)
```

## Livrable

`mes-reponses/ex-03.sql`
