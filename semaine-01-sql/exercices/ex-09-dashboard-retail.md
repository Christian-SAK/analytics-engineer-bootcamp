# ex-09 — Mini-dashboard retail (consolidation)

## Contexte

Synthèse semaine 1 : 5 requêtes pour un one-pager analytique.

## Tables

TPCH_SF1 (libre choix)

## Énoncé

Rédigez **5 requêtes SQL** répondant chacune à une question business :

1. **KPI** : CA total et nombre de commandes sur toute la période
2. **Segmentation** : CA par segment marketing (`C_MKTSEGMENT`)
3. **Produits** : top 10 articles (`P_NAME`) par quantité vendue
4. **Géographie** : CA par nation (via CUSTOMER → NATION)
5. **Tendance** : CA mensuel (`DATE_TRUNC('month', O_ORDERDATE)`)

Pour chaque requête, ajoutez un commentaire `-- Insight:` avec une interprétation en 1 phrase.

## Critères

- Au moins 3 jointures différentes utilisées sur l'ensemble
- Au moins 1 CTE ou fenêtre dans le lot
- Requêtes exécutables sans modification

## Livrable

- `mes-reponses/ex-09-dashboard.sql`
- `mes-reponses/ex-09-rapport.md` (5 insights rédigés, 1 paragraphe chacun max)
