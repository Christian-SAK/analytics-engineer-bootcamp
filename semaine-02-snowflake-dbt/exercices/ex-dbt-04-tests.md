# ex-dbt-04 — Tests avancés

## Énoncé

1. Ajoutez un test **singular** dans `tests/` : aucune ligne de `fct_order_lines` ne doit avoir `net_revenue < 0`.
2. Ajoutez un test `accepted_values` sur `order_status` dans staging orders (valeurs TPCH : 'O', 'F', 'P').
3. Documentez la différence entre test schema vs test singular.

## Exemple singular

```sql
-- tests/assert_positive_net_revenue.sql
select *
from {{ ref('fct_order_lines') }}
where net_revenue < 0
```

## Validation

- `dbt test` — tous verts (ou tests skipped documentés)

## Livrable

Fichiers dans `tests/` + entrées `schema.yml`.
