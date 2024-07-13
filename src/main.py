import os
import json
import argparse
from src.database import database

def research_agent(args, db):

    return 0

def paras_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_path',default='./database', type=str, help='Directory of the database.')
    parser.add_argument('--topic',default='', type=str, help='Topic to generate survey for')
    parser.add_argument('--api_model',default='gpt-4o-2024-05-13', type=str, help='Model to use')
    parser.add_argument('--api_url',default='https://api.openai.com/v1/chat/completions', type=str, help='url for API request')
    parser.add_argument('--api_key',default='', type=str, help='API key for the model')
    parser.add_argument('--embedding_model',default='nomic-ai/nomic-embed-text-v1', type=str, help='Embedding model for retrieval.')
    args = parser.parse_args()
    return args

def main(args):

    db = database(db_path = args.db_path, embedding_model = args.embedding_model)

    # create a new research agent yourself:
    new_research_idea = research_agent(args, db)

    return 0

if __name__ == '__main__':

    args = paras_args()

    main(args)