# ex-02 — Tri et exploration

## Contexte

Exploration des commandes par statut logistique.

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS`

## Énoncé

1. Listez les statuts distincts de commande (`O_ORDERSTATUS`) avec le nombre de commandes par statut.
2. Pour le statut le plus fréquent, affichez les 10 commandes les plus récentes (`O_ORDERDATE`) avec `O_ORDERKEY`, `O_CUSTKEY`, `O_TOTALPRICE`.
3. Calculez le montant total (`O_TOTALPRICE`) de toutes les commandes.

## Critères

- Question 1 : une seule requête avec agrégation
- Question 2 : `ORDER BY O_ORDERDATE DESC` et `LIMIT 10`

## Colonnes utiles

| Colonne | Description |
|---------|-------------|
| `O_ORDERKEY` | ID commande |
| `O_ORDERSTATUS` | Statut (ex. 'F' = fulfilled) |
| `O_ORDERDATE` | Date commande |
| `O_TOTALPRICE` | Montant total |

## Livrable

`mes-reponses/ex-02.sql`
