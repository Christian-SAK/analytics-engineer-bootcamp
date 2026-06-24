{{
    config(
        materialized='table'
    )
}}

with customers as (
    select * from {{ ref('stg_tpch__customer') }}
)

select
    customer_id,
    customer_name,
    market_segment,
    nation_id,
    account_balance,
    phone
from customers
