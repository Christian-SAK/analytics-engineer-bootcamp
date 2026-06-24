{{
    config(
        materialized='table'
    )
}}

/*
  Grain : une ligne = une ligne de commande (lineitem)
  Permet analyses produit / marge au niveau le plus fin
*/

with lineitems as (
    select * from {{ ref('stg_tpch__lineitem') }}
),

orders as (
    select * from {{ ref('stg_tpch__orders') }}
),

parts as (
    select * from {{ ref('stg_tpch__part') }}
),

joined as (
    select
        {{ dbt_utils.generate_surrogate_key(['lineitems.order_id', 'lineitems.line_number']) }} as order_line_id,
        lineitems.order_id,
        lineitems.line_number,
        orders.customer_id,
        orders.order_date,
        orders.order_status,
        lineitems.part_id,
        parts.part_name,
        parts.manufacturer,
        lineitems.quantity,
        lineitems.extended_price,
        lineitems.discount,
        lineitems.net_revenue
    from lineitems
    inner join orders on lineitems.order_id = orders.order_id
    inner join parts on lineitems.part_id = parts.part_id
)

select * from joined
