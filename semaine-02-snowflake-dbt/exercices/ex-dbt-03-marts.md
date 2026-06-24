# ex-dbt-03 — Dimension fournisseur

## Énoncé

Créez `models/marts/dim_supplier.sql` :

- Basé sur `stg_tpch__supplier`
- Jointure optionnelle à `stg_tpch__nation` (à créer) pour enrichir avec le nom du pays
- Grain : 1 ligne = 1 fournisseur

Ajoutez les tests dans `schema.yml` : `unique` + `not_null` sur `supplier_id`.

## Validation

- `dbt run --select dim_supplier`
- `dbt test --select dim_supplier`

## Livrable

Modèle + tests documentés.
