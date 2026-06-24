# Guide des jeux de données

Stratégie du bootcamp : **priorité aux samples Snowflake** (zéro ingest), complément local optionnel avec DuckDB.

---

## 1. Snowflake Sample Data (principal)

### Accès sur compte trial

1. Connectez-vous à Snowflake (Snowsight)
2. Menu **Data** → **Databases**
3. La database **`SNOWFLAKE_SAMPLE_DATA`** est disponible par défaut sur la plupart des comptes trial / standard
4. Si absente : exécutez en ACCOUNTADMIN :

```sql
-- Accorder l'accès aux shared samples (souvent déjà fait)
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE_SAMPLE_DATA TO ROLE PUBLIC;
-- ou à votre rôle utilisateur
```

5. Vérification :

```sql
SHOW DATABASES LIKE 'SNOWFLAKE%';
SELECT COUNT(*) FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER;
```

### TPCH — Fil rouge du bootcamp

Database : `SNOWFLAKE_SAMPLE_DATA`  
Schéma : **`TPCH_SF1`** (scale factor 1)

| Table complète | Rôle analytique | Colonnes clés |
|----------------|-----------------|---------------|
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER` | Clients | `C_CUSTKEY`, `C_NAME`, `C_MKTSEGMENT`, `C_ACCTBAL`, `C_NATIONKEY` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS` | Commandes | `O_ORDERKEY`, `O_CUSTKEY`, `O_ORDERDATE`, `O_TOTALPRICE`, `O_ORDERSTATUS` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM` | Lignes commande | `L_ORDERKEY`, `L_PARTKEY`, `L_SUPPKEY`, `L_QUANTITY`, `L_EXTENDEDPRICE`, `L_DISCOUNT` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PART` | Articles | `P_PARTKEY`, `P_NAME`, `P_MFGR`, `P_RETAILPRICE` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER` | Fournisseurs | `S_SUPPKEY`, `S_NAME`, `S_NATIONKEY` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PARTSUPP` | Offre fournisseur | `PS_PARTKEY`, `PS_SUPPKEY`, `PS_SUPPLYCOST`, `PS_AVAILQTY` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION` | Pays | `N_NATIONKEY`, `N_NAME`, `N_REGIONKEY` |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.REGION` | Régions | `R_REGIONKEY`, `R_NAME` |

**Volumes approximatifs (SF1)** : CUSTOMER 150K, ORDERS 1.5M, LINEITEM 6M.

#### Requêtes de découverte

```sql
USE DATABASE SNOWFLAKE_SAMPLE_DATA;
USE SCHEMA TPCH_SF1;

DESCRIBE TABLE CUSTOMER;
SELECT C_MKTSEGMENT, COUNT(*) FROM CUSTOMER GROUP BY 1;

-- Intégrité référentielle (devrait retourner 0)
SELECT COUNT(*)
FROM ORDERS o
LEFT JOIN CUSTOMER c ON o.O_CUSTKEY = c.C_CUSTKEY
WHERE c.C_CUSTKEY IS NULL;
```

#### Autres scale factors TPCH (optionnel)

| Schéma | Taille relative |
|--------|-----------------|
| `TPCH_SF10` | 10× |
| `TPCH_SF100` | 100× |
| `TPCH_SF1000` | 1000× |

Même structure de tables — utile pour tester performance, pas pour apprendre.

---

### TPC-DS — Retail enrichi (semaine 1 bonus / approfondissement)

Schéma : **`TPCDS_SF10TCL`**

| Table | Description |
|-------|-------------|
| `SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.STORE_SALES` | Ventes magasin |
| `SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.WEB_SALES` | Ventes web |
| `SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.DATE_DIM` | Dimension date |
| `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER` | — |
| `SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.ITEM` | Référentiel produit |

```sql
SELECT COUNT(*) FROM SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.STORE_SALES;
```

Modèle plus proche d'un **entrepôt dimensionnel** (Kimball) que TPCH.

---

### SNOWFLAKE_LEARNING_DB

Sur certains comptes récents, Snowflake propose **`SNOWFLAKE_LEARNING_DB`** avec des datasets pédagogiques.

```sql
SHOW DATABASES LIKE '%LEARNING%';
```

Si présent, explorez les schémas via `SHOW SCHEMAS IN DATABASE SNOWFLAKE_LEARNING_DB`. Contenu variable selon région et version de compte — **TPCH reste la référence stable** du bootcamp.

---

### Autres databases partagées utiles

| Database | Usage |
|----------|-------|
| `SNOWFLAKE_SAMPLE_DATA` | TPCH, TPC-DS, Weather, etc. |
| `SNOWFLAKE` | Métriques usage compte (account usage) — plutôt semaine avancée |

Liste complète :

```sql
SHOW DATABASES;
```

---

## 2. Jeux open source (complément local)

À utiliser si pas d'accès Snowflake temporaire ou pour prototyper hors cloud.

### DuckDB — exemples intégrés

```bash
pip install duckdb
duckdb -c "SELECT * FROM tpch.sf1.customer LIMIT 5;"
```

Extension TPCH chargée dans DuckDB — même logique métier, syntaxe SQL similaire.

### NYC Taxi (DuckDB / MotherDuck)

- Dataset public, pas d'inscription complexe
- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- Chargement DuckDB documenté : [duckdb.org — full stack benchmark](https://duckdb.org/docs/extensions/full_text_search)

Exemple :

```sql
INSTALL httpfs;
LOAD httpfs;
-- URLs parquet publics (vérifier disponibilité)
```

**Non utilisé dans le fil rouge** — réserve pour projet personnel post-bootcamp.

### autres

| Dataset | Accès | Note |
|---------|-------|------|
| [data.gov](https://data.gov) | Open | CSV variés, ingest manuelle |
| Kaggle | Compte requis | Évité en semaine 1 |
| BigQuery public datasets | GCP account | Hors stack bootcamp |

---

## 3. Stratégie par semaine

| Semaine | Dataset | Mode |
|---------|---------|------|
| S1 SQL | `SNOWFLAKE_SAMPLE_DATA.TPCH_SF1` | Lecture directe Snowflake |
| S2 dbt | Idem via `sources.yml` | dbt lit les sources partagées |
| S3 Airflow | Idem | Orchestration dbt — pas de nouvelle source |

### Copie vers schéma personnel (optionnel)

Pour simuler un vrai environnement dev :

```sql
CREATE DATABASE IF NOT EXISTS AE_BOOTCAMP;
CREATE SCHEMA IF NOT EXISTS AE_BOOTCAMP.RAW;

CREATE OR REPLACE TABLE AE_BOOTCAMP.RAW.ORDERS AS
SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS;
```

Mettre à jour `vars` dans `dbt_project.yml` :

```yaml
tpch_database: AE_BOOTCAMP
tpch_schema: RAW
```

---

## 4. Dépannage accès

| Symptôme | Solution |
|----------|----------|
| Database `SNOWFLAKE_SAMPLE_DATA` invisible | Demander à ACCOUNTADMIN `GRANT IMPORTED PRIVILEGES` |
| Permission denied | Vérifier rôle actif : `SELECT CURRENT_ROLE();` |
| Schéma TPCH_SF1 absent | Lister : `SHOW SCHEMAS IN DATABASE SNOWFLAKE_SAMPLE_DATA;` |
| Requête lente sur LINEITEM | Utiliser warehouse dimensionné (XS suffit en trial) + `LIMIT` en exploration |

---

## 5. Références officielles

- [Using sample data in Snowflake](https://docs.snowflake.com/en/user-guide/sample-data-using)
- [TPC-H specification](http://www.tpc.org/tpch/)
- [TPC-DS specification](http://www.tpc.org/tpcds/)
