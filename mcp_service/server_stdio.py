from fastmcp import FastMCP

# 创建 MCP 应用程序
app = FastMCP(
    name="MCP",
    version="1.0.0"
)


# 定义MCP工具
@app.tool(name="hello_tool", description="问候工具")
def hello(name: str):
    """
    用于产生问候的话语

    Args:
        name (str): 问好的目标的名字.

    Returns:
        str: 问好的语句.
    """
    return f"Hello, {name}!"


@app.tool(name="calculate_tool", description="两数求和工具")
def calculate(x: float, y: float):
    """
    将输入的两个数相加得到结果

    Args:
        x (float): 第一个输入的数字
        y (float): 第二个输入的数字

    Returns:
        float: 计算结果
    """
    # Calculate the tool value
    tool_value = x + y

    return tool_value


if __name__ == "__main__":
    # 启动 MCP 服务
    app.run(
        transport="stdio",    # 使用 SSE 传输
    )
