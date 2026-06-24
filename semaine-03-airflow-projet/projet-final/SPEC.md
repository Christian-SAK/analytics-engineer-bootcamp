# Spécification — Projet final

## Contexte

Vous êtes **Analytics Engineer** dans une équipe data d'un retailer. Les analysts ont besoin d'un entrepôt fiable sur les données TPCH (proxy e-commerce B2B).

## Objectif

Livrer un pipeline **documenté, testé et orchestré** :

```
[Sources TPCH Snowflake] → [dbt staging/marts] → [tests] → [orchestration Airflow]
```

## Périmètre fonctionnel

### Must have

1. **Modèles dbt** (minimum)
   - 4 staging : customer, orders, lineitem, part
   - 2 marts : `dim_customer`, `fct_order_lines` (ou équivalent documenté)
2. **Tests dbt** : PK unique/not_null, au moins 1 relationship
3. **DAG Airflow** : enchaînement `dbt run` → `dbt test` avec échec si tests KO
4. **Documentation**
   - README projet (installation, run, architecture)
   - Diagramme (mermaid ou image) du star schema
   - 3 KPIs SQL documentés (ex. CA total, panier moyen, top segment)

### Should have

- `dim_supplier` ou dimension géographique (nation/region)
- Test singular métier (ex. revenus ≥ 0)
- Capture d'écran lineage dbt + UI Airflow

### Could have

- Ingestion simulée (copy TPCH → schéma perso)
- Slack/email notification on failure
- CI GitHub Actions `dbt run` (sans secrets — dry parse only)

## KPIs attendus (exemples de requêtes sur marts)

Documentez les requêtes et résultats approximatifs :

```sql
-- CA total
SELECT SUM(net_revenue) FROM marts.fct_order_lines;

-- Panier moyen (par commande)
SELECT AVG(order_total) FROM (
  SELECT order_id, SUM(net_revenue) AS order_total
  FROM marts.fct_order_lines
  GROUP BY 1
);

-- Top segment
SELECT c.market_segment, SUM(f.net_revenue) AS ca
FROM marts.fct_order_lines f
JOIN marts.dim_customer c USING (customer_id)
GROUP BY 1 ORDER BY 2 DESC LIMIT 5;
```

## Structure livrable

```
projet-final/
├── README.md           # Votre doc principale
├── ARCHITECTURE.md     # Schéma + choix techniques
├── screenshots/        # docs + airflow (gitignore si lourd)
└── demo/               # script run local optionnel
```

## Critères d'évaluation

| Critère | Poids |
|---------|-------|
| Pipeline exécutable | 30 % |
| Qualité modélisation (grain, nommage) | 25 % |
| Tests & documentation | 25 % |
| Présentation portfolio | 20 % |

## Contraintes

- **Aucun secret** dans Git
- Code commenté en français ou anglais (cohérent)
- Justifier le grain de la table de faits

## Pitch entretien (5 min)

1. Problème business (1 min)
2. Architecture (2 min)
3. Démo rapide dbt docs + DAG (1 min)
4. Difficultés et apprentissages (1 min)

## Date limite

Fin de semaine 3 — voir [`PROGRESSION.md`](../../PROGRESSION.md).
