# 📊 dbt + Snowflake + Airflow (Cosmos) Demo

This project demonstrates an **end-to-end ELT pipeline** using:
- **dbt** for SQL-based transformations and testing
- **Snowflake** as the cloud data warehouse
- **Airflow (via Astronomer Cosmos)** for scheduling and orchestration

The pipeline loads seed data, transforms it into staging and marts models, validates results with dbt tests, and schedules everything through Airflow.

---

## 🚀 Project Overview

- **Database**: `DBT_DB`  
- **Schema**: `DBT_SCHEMA`  
- **Role**: `DBT_ROLE`  

### Workflow
1. **Seed Data** → CSVs loaded into Snowflake (`dbt seed`)  
2. **Staging Models** → clean + standardize raw data (`models/staging/`)  
3. **Marts Models** → transform staging into business-level facts/dimensions (`models/marts/`)  
4. **Business Views** → exposed to BI/analytics tools  
5. **Validation** → dbt schema + custom tests  
6. **Orchestration** → Airflow DAG (`dbt_dag`) runs the dbt workflow on a schedule  

---

## 📂 Repo Structure

### Data Flow in Snowflake

```mermaid
flowchart TD
  subgraph Snowflake["Snowflake: DBT_DB.DBT_SCHEMA"]
    V1[View: STG_TPCH_ORDERS]
    V2[View: STG_TPCH_LINE_ITEMS]
    T1[Table: INT_ORDER_ITEM]
    T2[Table: INT_ORDER_ITEMS_SUMMARY]
    T3[Table: FCT_ORDERS]
  end

  subgraph Airflow["Airflow DAG: dbt_dag"]
    S[dbt seed]
    ST[dbt run staging]
    M[dbt run marts]
    TE[dbt test]
  end

  S --> ST --> M --> TE
  ST --> V1
  ST --> V2
  M --> T1
  M --> T2
  M --> T3


```
