import logging
import argparse
import psycopg2
import sql_schema_registry

logging.getLogger().setLevel(logging.INFO)


def main():
    """
    Deployment schema registry process
    :return: None
    """
    parser = argparse.ArgumentParser(description='Deploy schema registry')
    parser.add_argument('-s', '--schema', dest='schema_name', type=str, required=True, help='Schema name')
    parser.add_argument('-n', '--user', dest='user_name', type=str, help='User name (for audit purposes)')
    parser.add_argument('-d', '--database_name', dest='db_name', type=str, required=True, help='Database name')
    parser.add_argument('-du', '--database_user', dest='db_user', type=str, required=True, help='Database username')
    parser.add_argument('-dps', '--database_password', dest='db_password', type=str, required=True,
                        help='Database password')
    parser.add_argument('-dh', '--database_host', dest='db_host', type=str, required=True, help='Database host')
    parser.add_argument('-dpt', '--database_port', dest='db_port', type=str, required=True, help='Database port')
    parser.add_argument('-f', '--files_path', dest='files_path', type=str, required=True, help='SQL files path')
    parser.add_argument('-tr', '--reinit', dest='reinit_sc', default=False, action='store_true',
                        help='Reinitialise sc table')

    args = parser.parse_args()

    # Connection to DB
    pg_conn = psycopg2.connect(database=args.db_name, user=args.db_user,
                               password=args.db_password, host=args.db_host, port=args.db_port)
    pg_conn.autocommit = True
    sql_schema_registry.deploy(schema_name=args.schema_name, db_name=args.db_name, user_name=args.user_name,
                               files_path=args.files_path, schema_restart=args.reinit_sc, db_conn=pg_conn)

    pg_conn.close()


if __name__ == "__main__":
    main()