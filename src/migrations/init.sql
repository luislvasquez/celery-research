-- Setup 
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Network table
---- Creation
CREATE TABLE networks (
    _id SERIAL,
    id UUID NOT NULL DEFAULT uuid_generate_v4(),
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    customer  VARCHAR,
    PRIMARY KEY(_id)
);

---- Population
-- INSERT INTO networks ()