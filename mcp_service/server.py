from fastmcp import FastMCP

from sql_service.sql_tool import sql_tool
from neo4j_service.neo4j_tool import neo4j_tool
from email_service.email_tool import email_tool
# 创建 MCP 应用程序
app = FastMCP(
    name="MCP",
    version="1.0.0"
)


# neo4j数据库查询工具
@app.tool(name="neo4j_tool", description="执行Cypher查询")
def neo4j_tool_mcp(cypher: str) -> str:
    """
    执行Cypher查询，返回结果
    :param cypher: Cypher查询语句
    """
    return neo4j_tool(cypher)


# sql数据库查询工具
@app.tool(name="sql_tool", description="执行SQL查询")
def sql_tool_mcp(sql: str) -> str:
    """
    执行SQL查询，返回结果
    :param sql: SQL查询语句
    """
    return sql_tool(sql)


# 邮件发送工具
@app.tool(name="email_tool", description="发送邮件")
def email_tool_mcp(dest_email: list[str], subject: str, content: str) -> str:
    """
    向一个或多个收件人发送邮件
    :param dest_email: 收件人邮箱列表
    :param subject: 邮箱主题
    :param content: 邮箱内容
    :return: 发送成功与否
    """
    return email_tool(dest_email, subject, content)


if __name__ == "__main__":
    # 启动 MCP 服务
    app.run(
        host="0.0.0.0",     # 监听所有地址
        port=8001,
        transport="sse",    # 使用 SSE 传输
    )
