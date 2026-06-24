# ex-dbt-02 — Modèle staging supplier

## Énoncé

Créez `models/staging/stg_tpch__supplier.sql` :

- Source : `{{ source('tpch', 'supplier') }}`
- Colonnes renommées : `supplier_id`, `supplier_name`, `nation_id`, etc.
- Pattern identique aux autres staging

## Validation

- `dbt run --select stg_tpch__supplier` OK
- Modèle visible dans le lineage (`dbt docs generate`)

## Livrable

Fichier SQL staging + entrée dans `sources.yml` si manquante.
