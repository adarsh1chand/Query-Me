import argparse
import os

def create_env_file(api_key, server_message, db_pass, database):
    with open('.env', 'w') as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")
        f.write(f'server_on_message="{server_message}"\n')
        f.write(f"DBPASS={db_pass}\n")
        f.write(f"DATABASE={database}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a .env file for the project.')

    # Set default values as specified
    parser.add_argument('--api_key', help='OpenAI API key')
    parser.add_argument('--server_message', default='Welcome to the ChatBot server developed by Sagar Dollin. Refer to readme.md file on how to access the chat app using POSTMAN', help='Server on message text')
    parser.add_argument('--db_pass', help='Database password')
    parser.add_argument('--database', help='Database name')

    args = parser.parse_args()

    create_env_file(args.api_key, args.server_message, args.db_pass, args.database)

    print("Successfully created .env file.")
