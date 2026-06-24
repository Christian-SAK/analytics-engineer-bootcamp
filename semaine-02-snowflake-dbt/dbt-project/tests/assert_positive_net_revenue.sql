-- Test singular exemple : revenu net toujours positif ou nul
select *
from {{ ref('fct_order_lines') }}
where net_revenue < 0
