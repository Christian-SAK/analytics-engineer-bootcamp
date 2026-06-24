# Progression — 3 semaines

Checklist jour par jour, livrables et critères de validation.

---

## Semaine 1 — SQL fondamental

**Objectif** : Maîtriser SELECT, JOIN, GROUP BY, sous-requêtes et fonctions fenêtre sur TPCH.

| Jour | Thème | Checklist |
|------|-------|-----------|
| **J1** | Découverte Snowflake + SELECT/FROM/WHERE | [ ] Compte Snowflake actif [ ] Première requête sur `CUSTOMER` [ ] `ex-01`, `ex-02` |
| **J2** | Agrégations (GROUP BY, HAVING) | [ ] Comprendre GROUP BY vs filter [ ] `ex-03`, `ex-04` |
| **J3** | Jointures (INNER, LEFT) | [ ] Joindre ORDERS ↔ CUSTOMER [ ] `ex-05` |
| **J4** | Jointures multiples + TPCH | [ ] LINEITEM ↔ ORDERS ↔ PART [ ] `ex-06` |
| **J5** | Sous-requêtes et CTE | [ ] Réécrire une sous-requête en WITH [ ] `ex-07` |
| **J6** | Fonctions fenêtre | [ ] ROW_NUMBER, RANK, LAG [ ] `ex-08` |
| **J7** | Consolidation + mini-projet | [ ] `ex-09`, `ex-10` [ ] Livrable S1 |

### Livrables semaine 1

- Fichier `semaine-01-sql/exercices/mes-reponses/` (ou gist) avec vos requêtes commentées
- **Rapport SQL** (1-2 pages) : 5 insights retail sur TPCH (CA par segment, top clients, etc.)

### Critères de validation S1

- [ ] Requêtes exécutables sans erreur sur Snowflake
- [ ] Au moins 2 jointures maîtrisées (INNER + LEFT)
- [ ] Au moins 1 CTE et 1 fonction fenêtre utilisées correctement
- [ ] Résultats interprétés (pas seulement du code)

---

## Semaine 2 — Snowflake + dbt

**Objectif** : Modéliser TPCH en star schema, tests et documentation dbt.

| Jour | Thème | Checklist |
|------|-------|-----------|
| **J8** | Architecture Snowflake (warehouse, rôle, schéma) | [ ] WH créé [ ] `profiles.yml` configuré (local, non commité) |
| **J9** | Init dbt + sources | [ ] `dbt debug` OK [ ] `sources.yml` TPCH |
| **J10** | Staging models | [ ] `stg_tpch__*` créés [ ] `dbt run` staging |
| **J11** | Marts (dimensions + facts) | [ ] `dim_customer`, `fct_orders` [ ] star schema |
| **J12** | Tests dbt | [ ] unique, not_null, relationships [ ] `dbt test` vert |
| **J13** | Documentation | [ ] descriptions dans schema.yml [ ] `dbt docs generate` |
| **J14** | Exercices dbt + consolidation | [ ] Exercices semaine 2 [ ] Livrable S2 |

### Livrables semaine 2

- Projet dbt fonctionnel dans `semaine-02-snowflake-dbt/dbt-project/`
- Capture ou export `dbt docs` (lineage)
- Schéma mermaid ou diagramme star schema (README ou fichier dédié)

### Critères de validation S2

- [ ] `dbt run` et `dbt test` passent sans erreur
- [ ] Au moins 3 modèles staging + 1 dim + 1 fact
- [ ] Tests sur clés primaires et relations FK
- [ ] Sources documentées avec références TPCH exactes

---

## Semaine 3 — Airflow + projet final

**Objectif** : Orchestrer dbt, livrer un pipeline documenté pour portfolio.

| Jour | Thème | Checklist |
|------|-------|-----------|
| **J15** | Concepts Airflow (DAG, Task, Operator) | [ ] Lire README S3 [ ] Docker Compose up |
| **J16** | Premier DAG | [ ] DAG exemple visible dans UI [ ] TaskGroup ou séquence |
| **J17** | Intégration dbt | [ ] BashOperator `dbt run` [ ] Variables/env |
| **J18** | dbt test dans le DAG | [ ] Échec DAG si test KO [ ] alerting basique |
| **J19** | Projet final — spec | [ ] Lire `projet-final/SPEC.md` [ ] Plan d'architecture |
| **J20** | Projet final — implémentation | [ ] DAG complet [ ] README projet |
| **J21** | Portfolio + rétrospective | [ ] Repo GitHub public/privé [ ] Post LinkedIn ou README portfolio |

### Livrables semaine 3

- DAG `retail_analytics_pipeline` (ou équivalent) dans `airflow/dags/`
- Dossier `projet-final/` avec README, schéma architecture, instructions run
- (Optionnel) Branche GitHub `portfolio` avec captures Airflow + dbt docs

### Critères de validation S3

- [ ] Pipeline exécutable de bout en bout (dbt run → dbt test)
- [ ] Documentation claire pour reproduire en local
- [ ] Pas de secrets dans le dépôt
- [ ] Projet présentable en entretien (5 min de pitch)

---

## Vue synthétique

```
Semaine 1          Semaine 2              Semaine 3
─────────          ─────────              ─────────
SQL / TPCH    →    dbt / Star schema  →   Airflow / Orchestration
     │                    │                      │
     └─ Rapport SQL       └─ dbt docs            └─ Projet final portfolio
```

## Suivi recommandé

- Cochez les cases au fur et à mesure
- Bloquez 2h minimum par jour « cours » + 1-2h exercices
- En cas de retard : priorisez livrables et critères de validation plutôt que 100 % des exercices bonus

## Contact formateur

Corrigés détaillés : voir `solutions/` ou demande directe au formateur.
