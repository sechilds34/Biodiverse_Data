#Queries Used in national_parks.py

queries = {
    "1": ("Total Parks",
          """select count(*) as total_parks from parks;"""),
    "2": ("Total Species",
          """select count(*) as total_species from species;"""),
    "3":("Species Per Park",
         """select park_name, count(*) as species_count
            from species 
            group by park_name
            order by species_count desc;
            """),
    "4": ("Nation Average of Species Per Park",
        """
        -- Gets the species count
        with park_name as (
            select park_name, count(*) as species_count
            from species
            group by park_name
            order by species_count desc
        )
        -- Does the avg of amount of species/ amount of parks
        select avg(species_count) as navg_species_count
        from park_name;
        """),
    "5": ("Average of Species Per Park", 
        """
        -- Count of species for each park
        with per_park as(
            select park_code, park_name,
            count(*) as species_count
            from species
            group by park_code, park_name
        ),
        -- Does avg of species per park
        avg_val as (
            select avg(species_count) as avg_species
            from per_park
        )
        -- does math for the difference in the per park number and the total average
        -- use cross join bc its single column joining bigger table
        select
            p.park_code,
            p.park_name,
            p.species_count,
            a.avg_species,
            round(p.species_count - a.avg_species, 2) as diff_from_avg
        from per_park p
        cross join avg_val a
        order by diff_from_avg desc;
        """),
    "6":("Amount of Species By Conservation Status",
        """
        select conservation_status, count(*) as cs_species
        from species
        group by conservation_status
        order by cs_species desc; 
        """),
    "7": ("Amount of At-Risk Species",
        """
        select p.park_name, p.park_code, count(*) as at_risk_count
        from species s
        join parks p on p.park_code = s.park_code
        where s.conservation_status is not null
            and s.conservation_status <> ''
            and s.conservation_status <> 'None'
        group by p.park_code, p.park_name
        order by at_risk_count desc;
        """),
    "8":("Percentage of At-Risk Species Per Park",
        """
        -- gets the count of at risk species
        with at_risk_count as (
        select 
            s.park_code, count(*) as at_risk
        from species s
        where s.conservation_status is not null
            and TRIM(s.conservation_status) <> ''
            and s.conservation_status <> 'none'
        group by s.park_code 
        ),
        total_species as (
        select 
            s.park_code, count(*) as total
        from species s 
        group by s.park_code
        )
        select
            p.park_code,
            p.park_name,
            ts.total as species_count,
            coalesce(arc.at_risk, 0) as at_risk_count,
            round(coalesce(arc.at_risk, 0) * 100.0 / nullif(ts.total, 0), 2) as percent_at_risk
        from parks p
        join total_species ts
            on ts.park_code = p.park_code
        left join at_risk_count arc
            on arc.park_code = p.park_code
        order by percent_at_risk desc, at_risk_count desc;
        """),
    "9":("Distribution of Categorization of At-Risk Species",
        """
        select s.category, count(*) as amount,
            round(100 * count(*) / (select count(*) from species
                                    where conservation_status is not null
                                        and conservation_status <> ''
                                        and conservation_status <> 'None'), 2) as percent
        from species s
        where s.conservation_status is not null
            and s.conservation_status <> ''
            and s.conservation_status <> 'None'
        group by s.category
        order by amount desc;
        """),
    "10":("Native Species Per Park",
        """
        select p.park_code, p.park_name, count(*) as native_count
        from species s
        join parks p on p.park_code = s.park_code
        where s.nativeness = "Native"
        group by p.park_code, p.park_name 
        order by native_count desc;
        """),
    "11":("Non-Native Species Per Park",
        """
        select p.park_code, p.park_name, count(*) as non_native_count
        from species s
        join parks p on p.park_code = s.park_code
        where s.nativeness = "Not Native"
        group by p.park_code, p.park_name
        order by non_native_count desc;
        """),
    "12":("Percent of Non-Native Species Per Park",
        """
        -- Need total amount species per park & total non-native then do math
        with non_native_per_park as(
            select s.park_code, count(*) as non_native_count
            from species s
            where s.nativeness = "Not Native"
            group by s.park_code
        ),
        total_species as (
            select 
                s.park_code, count(*) as total
            from species s 
            group by s.park_code
        )
        select
            p.park_code,
            p.park_name,
            round(coalesce(nnpp.non_native_count, 0) * 100.0 / nullif(ts.total, 0), 2) as percent_non_native
        from parks p
        join total_species ts
            on ts.park_code = p.park_code
        left join non_native_per_park nnpp
            on nnpp.park_code = p.park_code
        order by percent_non_native desc;
        """),
    "13":("Category With Most Non-Native",
        """
        select category, sum(nativeness = "Not Native") as non_native_count,
        count(*) as total_in_cat,
        round(100.0 * sum(nativeness = "Not Native") / count(*), 2) as non_native_pct
        from species
        group by category
        having total_in_cat >= 50
        order by non_native_pct desc, non_native_count desc;
        """),
    "14":("Most Common Taxonomy Order",
        """
        select tax_order, count(*) as amount
        from species
        group by tax_order
        order by amount desc;
        """),
    "15":("Most Common Families",
        """
        select family, count(*) as amount
        from species
        group by family
        order by amount desc;
        """),
    "16":("Orders With Highest Percentage of At-Risk Species",
        """
        -- need all tax orders & at risk species then do math

        with most_common_tax as(
            select s.tax_order, count(*) as total
            from species s
            where s.tax_order is not null
                and trim(s.tax_order) <> ''
            group by s.tax_order
        ),
        at_risk_count as (
            select s.tax_order, count(*) as at_risk
            from species s
            where s.tax_order is not null
                and TRIM(s.tax_order) <> ''
                and s.conservation_status is not null
                and s.conservation_status <> ''
                and s.conservation_status <> 'none'
            group by s.tax_order
        )
        select 
            mct.tax_order,
            mct.total,
            coalesce(arc.at_risk, 0) as at_risk,
            round(coalesce(arc.at_risk, 0) * 100 / nullif(mct.total, 0), 3) as perc_at_risk
            from most_common_tax mct
            left join at_risk_count arc
                on arc.tax_order = mct.tax_order
            order by perc_at_risk desc;
        """),
    "17":("Parks Dominated By a Single Order",
        """
        with per_order as (
            select park_code, tax_order, count(*) as n
            from species 
            group by park_code, tax_order
        ),
        totals as (
            select park_code, count(*) as total_n
            from species 
            group by park_code
        ),
        ranked as (
            select
                o.park_code,
                o.tax_order,
                o.n,
                t.total_n,
                (o.n / t.total_n) as share,
                row_number() over (partition by o.park_code order by o.n desc) as rn
            from per_order o
            join totals t on t.park_code = o.park_code
        )
        select 
            p.park_code, p.park_name,
            r.tax_order as dominant_order,
            r.n as dominant_count,
            r.total_n,
            round(100 * r.share, 2) as dominant_pct
        from ranked r
        join parks p on p.park_code = r.park_code
        where r.rn = 1
        order by dominant_pct desc, dominant_count desc;
        """),

}