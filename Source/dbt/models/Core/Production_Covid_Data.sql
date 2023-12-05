{{ config(
    materialized='table',
    partition_by={
      "field": "date",
      "data_type": "timestamp",
      "granularity": "day"
    }
)}}

with covid_data as (
    select *, 
    from {{ ref('stg_covid') }}
    where (country is not null) and (continent is not null) and (new_cases_per_million is not null) and (new_cases is not null)
)

select 
    covid_data.date, 
    covid_data.new_cases as total_cases,
    covid_data.new_cases_per_million as total_cases_per_million,
    covid_data.continent,
    covid_data.country

 from covid_data

{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  where date > (select max(date) from {{ this }})

{% endif %}

-- {% if var('is_test_run', default=true) %}

--   limit 100

-- {% endif %}