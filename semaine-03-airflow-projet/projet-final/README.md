# Projet final — README template

Complétez ce fichier pour votre livrable portfolio.

## Titre

Pipeline Retail Analytics — TPCH / dbt / Airflow

## Auteur

[Votre nom]

## Résumé

[2-3 phrases : objectif, stack, résultat]

## Prérequis

- Snowflake trial
- Python 3.10+, dbt-snowflake
- Docker (Airflow)

## Installation

```bash
# dbt
cd semaine-02-snowflake-dbt/dbt-project
pip install dbt-snowflake
cp profiles.yml.example ~/.dbt/profiles.yml
# éditer credentials

dbt deps && dbt run && dbt test
```

```bash
# Airflow
cd semaine-03-airflow-projet
docker compose up -d
```

## Architecture

[Insérer diagramme mermaid ou image]

## KPIs

| KPI | Valeur | Requête |
|-----|--------|---------|
| CA total | | |
| Panier moyen | | |
| Top segment | | |

## Captures

- Lineage dbt
- DAG Airflow

## Apprentissages

1.
2.
3.
