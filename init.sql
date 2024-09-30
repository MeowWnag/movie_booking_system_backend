DO $$ 
BEGIN 
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'movie_booking_system') THEN 
        CREATE DATABASE movie_booking_system; 
    END IF; 
END $$; 

DO $$ 
BEGIN 
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'app_user') THEN 
        CREATE ROLE app_user WITH LOGIN PASSWORD 'userpassword'; 
    END IF; 
END $$;

ALTER DATABASE movie_booking_system OWNER TO app_user;

-- 創建 app_user 資料表
CREATE TABLE IF NOT EXISTS app_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    role VARCHAR(50) DEFAULT 'user'
);
