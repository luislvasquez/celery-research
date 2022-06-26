-- Setup 
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Network table
---- Creation
DROP TABLE IF EXISTS networks;

CREATE TABLE networks (
    _id SERIAL,
    id UUID NOT NULL DEFAULT uuid_generate_v4(),
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    customer VARCHAR,
    status VARCHAR,
    operation_started TIMESTAMP WITHOUT TIME ZONE,
    operation_finished TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY(_id)
);

---- Population
INSERT INTO networks (name, location, customer, status)
VALUES
    ('mig_network_1', 'Tangamandapio', 'migration_customer', 'ONLINE'),
    ('mig_network_2', 'Narnia', 'migration_customer', 'ONLINE'),
    ('mig_network_3', 'Hogwarts', 'migration_customer', 'ONLINE')
;
