from pydantic import BaseModel, Field   # 用于输入参数校验
from email.mime.text import MIMEText
from dotenv import load_dotenv  # 用于加载环境变量
import os   # 用于读取环境变量
import smtplib

load_dotenv()


# 参数验证
class EmailArgs(BaseModel):
    # 收件人邮箱：必填
    dest_email: list[str] = Field(..., description="收件人邮箱列表(至少包含一个收件人，必填)", example=["<EMAIL>", "<EMAIL>"])
    # 邮件主题：必填
    subject: str = Field(..., description="邮件主题，必填")
    # 邮件内容：必填
    content: str = Field(..., description="邮件内容，必填")


# MCP工具
def email_tool(dest_email: list[str], subject: str, content: str) -> str:
    """
    向一个或多个收件人发送邮件
    :param dest_email: 收件人邮箱列表(必填)
    :param subject: 邮箱主题(必填)
    :param content: 邮箱内容(必填)
    """
    try:
        # 创建邮件对象
        msg = MIMEText(content)
        msg["From"] = os.getenv("EMAIL_HOST_USER")
        msg["To"] = ", ".join(dest_email)
        msg["Subject"] = subject

        # 创建SMTP对象
        smtp = smtplib.SMTP_SSL(os.getenv("EMAIL_HOST"), 465, timeout=30)

        # 登录邮箱
        smtp.login(os.getenv("EMAIL_HOST_USER"), os.getenv("EMAIL_HOST_PASSWORD"))

        # 发送邮件
        smtp.sendmail(os.getenv("EMAIL_HOST_USER"), dest_email, msg.as_string())
        smtp.quit()
        return "发送成功"
    except smtplib.SMTPConnectError as e:
        print("SMTP连接错误:", e)
        return f"连接邮件服务器失败: {str(e)}"
    except smtplib.SMTPAuthenticationError as e:
        print("认证错误:", e)
        return f"邮箱认证失败: {str(e)}"
    except Exception as e:
        print("发生异常：", e)
        return f"发送失败: {str(e)}"
