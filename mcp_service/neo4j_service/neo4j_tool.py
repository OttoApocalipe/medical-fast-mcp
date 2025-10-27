from pydantic import BaseModel, Field
from dotenv import load_dotenv
from utils.neo4j_pool import pool
import os

load_dotenv()


# 参数类
class Neo4jArgs(BaseModel):
    cypher: str = Field(..., description="Cypher查询语句")


# MCP工具
def neo4j_tool(cypher: str) -> str:
    """
    执行Cypher查询，返回结果
    :param cypher: Cypher查询语句
    """
    try:
        driver = pool.create_driver()
        with driver.session(database=os.getenv("NEO4J_DATABASE")) as session:
            records = session.run(cypher)
            result = [record.data() for record in records]
            return str(result)
    except Exception as e:
        return f"执行Cypher查询失败: {str(e)}"
    finally:
        pool.close_driver()
