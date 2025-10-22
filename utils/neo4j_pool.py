from neo4j import GraphDatabase
import os
from dotenv import load_dotenv


# 定义Neo4j连接池类
class Neo4jPool:
    _driver = None

    def __init__(self, url, user, password, database, pool_size=20):
        self.url = url
        self.user = user
        self.password = password
        self.database = database
        self.pool_size = pool_size

    # Neo4j驱动创建
    def create_driver(self):
        if self._driver is None:
            self._driver = GraphDatabase.driver(
                self.url,
                auth=(self.user, self.password),
                database=self.database,
                max_connection_pool_size=self.pool_size
            )
        return self._driver

    def close_driver(self):
        if self._driver is not None:
            self._driver.close()


# Neo4j 连接池
pool = Neo4jPool(
    url=os.getenv("NEO4J_URL"),
    user=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
    database=os.getenv("NEO4J_DATABASE"),
)
