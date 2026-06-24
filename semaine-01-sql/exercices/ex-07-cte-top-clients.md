# ex-07 — CTE : top 10 clients par CA

## Contexte

Identifier les clients VIP pour un programme fidélité.

## Tables

- `ORDERS`, `CUSTOMER` (TPCH_SF1)

## Énoncé

1. Avec une **CTE** `ca_client`, calculez le CA total par `C_CUSTKEY` (somme des `O_TOTALPRICE`).
2. Joignez à `CUSTOMER` pour obtenir `C_NAME`, `C_MKTSEGMENT`, `ca_total`.
3. Retenez le **top 10** par `ca_total`.
4. **Bonus** : même résultat avec une sous-requête dans `FROM` au lieu d'une CTE — laquelle est plus lisible ?

## Critères

- Structure `WITH ca_client AS (...)` obligatoire pour la version principale
- Exclure les clients sans commande (INNER JOIN suffit)

## Livrable

`mes-reponses/ex-07.sql`
