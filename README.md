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

flowchart LR
  subgraph SF["Snowflake: DBT_DB"]
    RAW[Seeds / Raw Data]:::raw
    STG[DBT_SCHEMA.STAGING]:::stg
    MARTS[DBT_SCHEMA.MARTS]:::mart
    VIEWS[Business Views for Analytics/BI]:::view
  end

  subgraph AF["Airflow (Cosmos DAG)"]
    DAG[dbt_dag]
  end

  RAW --> STG --> MARTS --> VIEWS
  DAG -- "dbt seed" --> RAW
  DAG -- "dbt run (staging)" --> STG
  DAG -- "dbt run (marts)" --> MARTS
  DAG -- "dbt test" --> VIEWS

  classDef raw fill=#f2f2f2,stroke=#555,color=#000;
  classDef stg fill=#cce5ff,stroke=#004085,color=#004085;
  classDef mart fill=#d4edda,stroke=#155724,color=#155724;
  classDef view fill=#fff3cd,stroke=#856404,color=#856404;
