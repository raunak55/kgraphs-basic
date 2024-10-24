from dotenv import load_dotenv
import os
from langchain_community.graphs import Neo4jGraph

load_dotenv()

AURA_INSTANCENAME = os.environ["AURA_INSTANCENAME"]
NEO4J_URI = os.environ["NEO4J_URI"]
NEO4J_USERNAME = os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD = os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE = os.environ["NEO4J_DATABASE"]
AUTH = (NEO4J_USERNAME, NEO4J_PASSWORD)

kg = Neo4jGraph(url=NEO4J_URI,username=NEO4J_USERNAME,password=NEO4J_PASSWORD,database=NEO4J_DATABASE)

cypher = "MATCH(n) return count(n) as no_of_nodes"
result = kg.query(cypher)
print(f"There are {result[0]['no_of_nodes']} nodes")

cypher = "MATCH(n:HealthcareProvider) return count(n) as no_of_providers"
result = kg.query(cypher)
print(f"There are {result[0]['no_of_providers']} health care providers")


cypher = "MATCH(n:HealthcareProvider) return n.name as name"
result = kg.query(cypher)
for r in result:
    print(r['name'])

print('*'*20)
cypher = "MATCH(n:Patient) return n.name as name limit 10"
result = kg.query(cypher)
for r in result:
    print(r['name'])

print('*'*20)
cypher = "MATCH(n:Specialization) return n.name as name"
result = kg.query(cypher)
for r in result:
    print(r['name'])
