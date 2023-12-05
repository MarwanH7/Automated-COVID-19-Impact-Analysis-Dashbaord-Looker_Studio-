
{{ config(
    materialized='incremental',
    partition_by={
      "field": "date",
      "data_type": "timestamp",
      "granularity": "day"
    }
)}}


with covid_data as
(
  select *,
  from {{ source('staging','Covid_data') }}
)

select
-- strings
CAST(iso_code as STRING) as iso_code,
CAST(continent as STRING) as continent,
CAST(country as STRING) as country,

-- timestamp
CAST(date as timestamp) as date,

-- integers
CAST(total_cases as INTEGER) as total_cases,
CAST(new_cases as INTEGER) as new_cases,
CAST(total_deaths as INTEGER) as total_deaths,
CAST(new_deaths as INTEGER) as new_deaths,
CAST(total_tests as INTEGER) as total_tests,
CAST(total_vaccinations as INTEGER) as total_vaccinations,
CAST(people_vaccinated as INTEGER) as people_vaccinated,
CAST(people_fully_vaccinated as INTEGER) as people_fully_vaccinated,

-- floats
CAST(total_cases_per_million as INTEGER) as total_cases_per_million,
CAST(new_cases_per_million as INTEGER) as new_cases_per_million,
CAST(total_deaths_per_million as INTEGER) as total_deaths_per_million,
CAST(new_deaths_per_million as INTEGER) as new_deaths_per_million,
CAST(total_tests_per_thousand as INTEGER) as total_tests_per_thousand,
CAST(people_vaccinated_per_hundred as INTEGER) as people_vaccinated_per_hundred,
CAST(people_fully_vaccinated_per_hundred as INTEGER) as people_fully_vaccinated_per_hundred,

from covid_data

{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  where CAST(date as timestamp) > (select max(date) from {{ this }})

{% endif %}

-- {% if var('is_test_run', default=true) %}

--   limit 100

-- {% endif %}
