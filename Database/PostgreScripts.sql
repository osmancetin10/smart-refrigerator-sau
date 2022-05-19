-- Table: public.tbl_sr_door_status_info

-- DROP TABLE IF EXISTS public.tbl_sr_door_status_info;

CREATE TABLE IF NOT EXISTS public.tbl_sr_door_status_info
(
    id integer NOT NULL DEFAULT nextval('tbl_sr_door_status_id_seq'::regclass),
    is_door_opened boolean NOT NULL,
    status_date timestamp with time zone NOT NULL,
    CONSTRAINT tbl_sr_door_status_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_sr_door_status_info
    OWNER to gppafqfrzgxajy;
	
-- Table: public.tbl_sr_temperature_info

-- DROP TABLE IF EXISTS public.tbl_sr_temperature_info;

CREATE TABLE IF NOT EXISTS public.tbl_sr_temperature_info
(
    id integer NOT NULL DEFAULT nextval('tbl_sr_temperature_info_id_seq'::regclass),
    temperature_date timestamp with time zone NOT NULL,
    temperature numeric NOT NULL,
    CONSTRAINT tbl_sr_temperature_info_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_sr_temperature_info
    OWNER to gppafqfrzgxajy;