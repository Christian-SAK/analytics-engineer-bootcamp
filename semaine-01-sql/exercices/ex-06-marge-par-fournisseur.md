# ex-06 — Marge par fournisseur

## Contexte

Analyse supply chain : revenu vs coût d'achat par fournisseur.

## Tables

- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM`
- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS`
- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PARTSUPP`
- `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER`

## Énoncé

Calculez par fournisseur (`S_NAME`, `S_NATIONKEY`) :

- `ca_brut` : somme de `L_EXTENDEDPRICE * (1 - L_DISCOUNT)`
- `cout_achat` : somme de `L_QUANTITY * PS_SUPPLYCOST` (via PARTSUPP)
- `marge` : `ca_brut - cout_achat`

Affichez le **top 15** fournisseurs par marge décroissante.

## Schéma de jointure

```
LINEITEM → ORDERS (L_ORDERKEY = O_ORDERKEY)
LINEITEM → PARTSUPP (L_PARTKEY = PS_PARTKEY AND L_SUPPKEY = PS_SUPPKEY)
PARTSUPP → SUPPLIER (PS_SUPPKEY = S_SUPPKEY)
```

## Critères

- Jointures explicites (pas de produit cartésien)
- `LIMIT 15` en fin de requête

## Livrable

`mes-reponses/ex-06.sql`
