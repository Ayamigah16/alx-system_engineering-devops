-- Create the replica_user with appropriate permissions
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'dev-ab';

-- Grant replication privileges to replica_user
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant SELECT privileges on mysql.user to holberton_user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
