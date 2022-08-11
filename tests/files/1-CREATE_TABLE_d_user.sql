CREATE TABLE IF NOT EXISTS core.d_user (
  id serial,
  name varchar(50) NOT NULL,
  surname varchar(30) NOT NULL,
  username varchar(30) NOT NULL,
  country_id integer NOT NULL,
  phone_number integer,
  email integer NOT NULL,
  device_id integer[] NOT NULL,
  PRIMARY KEY (id)
);