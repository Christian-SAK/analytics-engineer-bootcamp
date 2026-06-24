# ex-05 — Jointure ORDERS ↔ CUSTOMER

## Contexte

Relier chaque commande au nom et segment de son client.

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS`
- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER`

## Énoncé

1. **INNER JOIN** : pour chaque commande de 1995, affichez `O_ORDERKEY`, `O_ORDERDATE`, `O_TOTALPRICE`, `C_NAME`, `C_MKTSEGMENT`.
2. **LEFT JOIN** : combien de commandes n'ont **pas** de client correspondant ? (devrait être 0 sur TPCH — vérification d'intégrité)
3. CA total (`SUM(O_TOTALPRICE)`) par segment marketing pour l'année 1995.

## Clé de jointure

```sql
ORDERS.O_CUSTKEY = CUSTOMER.C_CUSTKEY
```

## Critères

- Filtrer dates : `YEAR(O_ORDERDATE) = 1995` ou `O_ORDERDATE BETWEEN '1995-01-01' AND '1995-12-31'`
- Alias de tables obligatoires (`o`, `c`)

## Livrable

`mes-reponses/ex-05.sql`
