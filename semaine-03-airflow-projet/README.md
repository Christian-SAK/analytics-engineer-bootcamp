# Semaine 3 — Airflow + projet final

Orchestrer un pipeline analytics de bout en bout et produire un livrable **portfolio**.

## Objectifs

- Comprendre DAG, Task, Operator, Scheduler, Executor
- Lancer Airflow en local via **Docker Compose**
- Enchaîner `dbt run` → `dbt test` dans un DAG
- Livrer un projet documenté pour entretien

## Concepts Airflow

| Concept | Description |
|---------|-------------|
| **DAG** | Graphe acyclique de tâches (= pipeline) |
| **Task** | Unité de travail (bash, Python, SQL…) |
| **Operator** | Modèle de tâche (`BashOperator`, `PythonOperator`) |
| **Schedule** | Cron ou `@daily` — quand le DAG s'exécute |
| **XCom** | Échange de métadonnées entre tasks (usage limité) |

## Setup Docker (recommandé)

Prérequis : Docker + Docker Compose installés.

```bash
cd semaine-03-airflow-projet

# Créer les dossiers attendus par l'image officielle
mkdir -p airflow/dags airflow/logs airflow/plugins

# Variables d'environnement (exemple — adapter UID)
export AIRFLOW_UID=$(id -u)

# Télécharger le docker-compose officiel (option) ou utiliser notre minimal
# Voir : https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

docker compose up airflow-init   # première fois
docker compose up -d             # démarrer scheduler + webserver
```

Interface web : http://localhost:8080 (identifiants par défaut selon compose — voir doc Airflow).

### Intégration dbt

Montez le projet dbt en volume :

```yaml
volumes:
  - ../semaine-02-snowflake-dbt/dbt-project:/opt/dbt/ae_bootcamp
```

Passez `profiles.yml` via secret Docker ou variable d'environnement — **jamais** dans Git.

## DAG fourni

[`airflow/dags/retail_analytics_pipeline.py`](airflow/dags/retail_analytics_pipeline.py) — squelette :

1. `check_snowflake` (optionnel / placeholder)
2. `dbt_run`
3. `dbt_test`

## Programme

| Jour | Focus |
|------|-------|
| J15 | Lire doc Airflow, lancer stack Docker |
| J16 | Activer le DAG exemple, explorer l'UI |
| J17 | Brancher chemins dbt réels |
| J18 | Gestion échecs, retries, alerting email (optionnel) |
| J19-21 | Projet final — voir [`projet-final/SPEC.md`](projet-final/SPEC.md) |

## Projet final

Spécification complète dans [`projet-final/SPEC.md`](projet-final/SPEC.md).

En résumé : pipeline orchestré TPCH → dbt → tests, README portfolio, schéma d'architecture.

## Git & portfolio

1. Repo GitHub dédié ou ce monorepo — README avec badges (dbt, Airflow)
2. Captures : lineage dbt + graphe DAG Airflow
3. Section « Ce que j'ai appris » — 5 bullet points
4. Pitch 5 minutes : problème → solution → stack → résultats

## Dépannage

| Problème | Piste |
|----------|-------|
| DAG invisible | Vérifier syntaxe Python, logs scheduler |
| dbt not found | Installer dbt dans l'image Docker ou utiliser BashOperator avec venv monté |
| Connexion Snowflake | Vérifier `profiles.yml` dans le conteneur |

## Livrable

Voir [`PROGRESSION.md`](../PROGRESSION.md).
