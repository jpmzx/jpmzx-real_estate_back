select_properties = """
            select
                p.id "id",
                p.address  "address",
                p.city "city",
                p.price "price",
                p.year "year",
                COALESCE(sh.status_id, 0) "status_id",
                COALESCE(sh.update_date, CURRENT_DATE()) "status_update_date",
                COALESCE(s.name, 'creado') "status_name",
                COALESCE(s.label, 'Inmueble creado') "status_label"
            from
                property p
            left join status_history sh ON
                sh.property_id = p.id
                and sh.id = (
                select
                    max(sht.id)
                from
                    status_history sht
                where
                    sht.property_id = p.id)
            left join status s on
                sh.status_id = s.id
        """

select_properties_public = """
            select
                p.id "id",
                p.address  "address",
                p.city "city",
                s.name "status_name",
                s.label "status_label",
                p.price "price",
                p.year "year"
            from
                property p
            left join status_history sh ON
                sh.property_id = p.id
                and sh.id = (
                select
                    max(sht.id)
                from
                    status_history sht
                where
                    sht.property_id = p.id)
            left join status s on
                sh.status_id = s.id
        """
