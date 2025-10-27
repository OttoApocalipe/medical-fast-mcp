from pydantic import BaseModel, Field   # 用于输入参数校验
from dotenv import load_dotenv  # 用于加载环境变量
import os   # 用于读取环境变量
import mysql.connector  # 用于连接Mysql数据库

# 加载环境变量
load_dotenv()

# 创建Mysql连接池
pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mysql_pool",
    pool_size=int(os.getenv("MYSQL_POOL_SIZE")),
    host=os.getenv("MYSQL_HOST"),
    port=os.getenv("MYSQL_PORT"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
)


class SqlArgs(BaseModel):
    sql: str = Field(..., description="SQL查询语句 (或者Mysql的辅助语句如: SHOW, DESCRIBE)")


# 定义智能体工具
def sql_tool(sql: str) -> str:
    """
    执行SQL查询语句，返回结果
    :param sql: SQL查询语句 (或者Mysql的辅助语句如: SHOW, DESCRIBE)
    """
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return str(result)
    except Exception as e:
        return f"执行SQL语句失败: {str(e)}"
