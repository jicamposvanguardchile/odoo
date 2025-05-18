from odoo import api

def _pre_init_prtg_module(cr):
    cr.execute("""
            CREATE TABLE prtg_historic_data
            (
                id             serial primary key,
                dt             timestamp,
                dt_date        date NOT NULL,
                dt_raw         VARCHAR(50),
                prtg_server_id integer NOT NULL,
                prtg_sensor_id integer NOT NULL,
                coverage       VARCHAR(50),
                coverage_raw   real,
                content        xml,
                min_5          bigint,
                min_10         bigint,
                min_15         bigint,
                min_30         bigint,
                hr_1           bigint,
                hr_12          bigint,
                day_1          bigint,
                mon_1          bigint,
                year_1         bigint
            );
        """)
            ##CREATE INDEX prtg_sensor_id_idx ON prtg_historic_data (prtg_sensor_id);
            ##CREATE UNIQUE INDEX title_idx ON films (title);

def _post_uninstall_prtg_module(cr, registry):
    cr.execute("""
            DROP TABLE prtg_historic_data;
        """)
