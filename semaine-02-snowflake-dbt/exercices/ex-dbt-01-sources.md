# ex-dbt-01 — Sources et fraîcheur

## Énoncé

1. Vérifiez que `sources.yml` référence bien toutes les tables TPCH utilisées par le projet.
2. Ajoutez la table `supplier` dans `sources.yml` avec description et colonnes clés.
3. (Bonus) Ajoutez un test `source freshness` sur `orders` si vous avez une colonne date de chargement — sinon documentez pourquoi ce n'est pas applicable sur sample data.

## Validation

- `dbt parse` sans erreur
- `dbt source freshness` (ou justification écrite)

## Livrable

Modification de `models/staging/sources.yml` + commentaire dans un commit message ou note.
