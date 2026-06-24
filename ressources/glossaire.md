# Glossaire Analytics Engineer (FR)

Termes du métier et de la stack, en français, avec équivalents anglais courants.

---

## Rôles & organisation

| Terme FR | EN | Définition |
|----------|-----|------------|
| Analytics Engineer | Analytics Engineer | Profil entre data engineer et analyst : transforme les données brutes en modèles analytiques fiables |
| Data Engineer | Data Engineer | Construit pipelines ingest, infra, qualité opérationnelle |
| Analyste data | Data Analyst | Consomme les données, dashboards, insights business |
| Stakeholder | Stakeholder | Partie prenante métier consommatrice des chiffres |

---

## Modélisation

| Terme | Définition |
|-------|------------|
| **Entrepôt de données** (Data Warehouse) | Base optimisée pour l'analyse (OLAP), séparée des systèmes opérationnels (OLTP) |
| **Schéma en étoile** (Star schema) | Table de faits centrale + dimensions autour (client, date, produit…) |
| **Grain** | Niveau de détail d'une table de faits (ex. 1 ligne = 1 ligne de commande) |
| **Staging** | Couche intermédiaire proche de la source, nettoyage minimal |
| **Mart** | Table analytique finale orientée métier (finance, marketing…) |
| **Dimension** | Table descriptive (qui, quoi, où, quand) |
| **Faits** (Facts) | Mesures numériques événementielles (montant, quantité) |
| **Clé surrogate** | Identifiant technique artificiel (hash, séquence) |
| **SCD** (Slowly Changing Dimension) | Gestion historique des changements dimension |

---

## SQL & transformation

| Terme | Définition |
|-------|------------|
| **CTE** (Common Table Expression) | Bloc `WITH ... AS` nommé, améliore lisibilité |
| **Fonction fenêtre** (Window function) | Calcul sur un ensemble de lignes sans collapse (ROW_NUMBER, LAG…) |
| **Jointure** (JOIN) | Combinaison de tables par clé |
| **Agrégation** | Réduction via GROUP BY (SUM, COUNT…) |
| **Idempotent** | Rejouer N fois = même résultat (important pour dbt) |

---

## dbt

| Terme | Définition |
|-------|------------|
| **Modèle** (model) | Fichier SQL versionné transformé en table/vue |
| **Source** | Table externe déclarée (non gérée par dbt) |
| **Ref** | Macro `{{ ref('model') }}` — dépendance entre modèles |
| **Test** | Assertion qualité (unique, not_null, relationships…) |
| **Seed** | CSV chargé par dbt |
| **Macro** | Fonction Jinja réutilisable |
| **Lineage** | Graphe de dépendances entre modèles |
| **Materialization** | Table, view, incremental, ephemeral… |

---

## Snowflake

| Terme | Définition |
|-------|------------|
| **Account** | Identifiant compte cloud Snowflake |
| **Warehouse** | Cluster compute (facturation à l'usage) |
| **Database / Schema** | Hiérarchie logique namespace |
| **Role** | Permissions RBAC |
| **Virtual warehouse** | Ressource CPU/RAM pour exécuter requêtes |
| **Time travel** | Historique versions tables (rétention) |
| **Stage** | Zone stockage fichiers (internal/external) |

---

## Airflow

| Terme | Définition |
|-------|------------|
| **DAG** | Directed Acyclic Graph — workflow |
| **Task** | Étape unitaire |
| **Operator** | Type de tâche (Bash, Python…) |
| **Scheduler** | Planifie exécution DAGs |
| **Executor** | Moteur d'exécution des tasks |
| **Sensor** | Task en attente d'une condition |
| **Hook / Connection** | Credentials externalisés |

---

## Qualité & gouvernance

| Terme | Définition |
|-------|------------|
| **Data quality** | Fiabilité, complétude, cohérence des données |
| **Observabilité** | Monitoring, logs, alertes pipeline |
| **Catalogue de données** | Inventaire datasets + métadonnées |
| **Lineage** | Traçabilité origine → transformation → consommation |
| **SLA** | Engagement niveau de service (fraîcheur, dispo) |

---

## Analogies R / Python

| SQL / AE | R / stats |
|----------|-----------|
| GROUP BY | `dplyr::group_by()` |
| LAG / LEAD | `dplyr::lag()`, `lead()` |
| Window SUM | cumsum par groupe |
| JOIN | merge() avec clé |
| DISTINCT | unique() |
| WHERE avant agrégat | filter avant summarise |
