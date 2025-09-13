## 🔄 Workflow

This project uses **dbt** to model data in Snowflake, following a typical `staging → marts → business views` pattern.

1. **Seed & Raw Layer**
   - CSV seeds are loaded into **DBT_DB.DBT_SCHEMA** using `dbt seed`.
   - These represent raw transactional data.

2. **Staging Layer (`models/staging/`)**
   - `stg_tpch_orders.sql`: cleans and standardizes order data.
   - `stg_tpch_line_items.sql`: normalizes line item data.
   - Together, these form the **cleaned staging layer** for downstream modeling.

3. **Marts Layer (`models/marts/`)**
   - `fct_orders.sql`: fact table of orders with metrics such as order count, revenue, and discounts.
   - `int_order_items_summary.sql`: intermediate model summarizing line items at the order level.
   - `int_order_item.sql`: joins staging tables to prepare enriched fact data.

4. **Business Views**
   - dbt builds **business-friendly views** on top of marts, exposed to analytics tools and BI dashboards.
   - These serve KPIs such as total revenue, order discount rates, and item counts.

5. **Tests & Validation**
   - Schema tests (`generic_tests.yml`, `tpch_sources.yml`) ensure columns are `not_null`, `unique`, and valid.
   - Custom tests (`fct_orders_data_valid.sql`, `fct_orders_discount.sql`) enforce business rules.

6. **Orchestration**
   - Airflow (with Cosmos) generates a DAG that runs:
     - `dbt seed` → `dbt run (staging)` → `dbt run (marts)` → `dbt test`
   - Scheduled refresh keeps Snowflake marts and views always up to date.
