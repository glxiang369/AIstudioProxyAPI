from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import subprocess
import uvicorn

app = FastAPI()

# 启动代理服务（模拟原项目的 start.py）
def start_proxy():
    subprocess.Popen(["python", "launch_camoufox.py", "--headless", "--server-port", "8000"])

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <body>
            <h1>AI Studio Proxy API</h1>
            <p>服务已运行！客户端可连接至：<code>http://localhost:8000/v1</code></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    start_proxy()
    uvicorn.run(app, host="0.0.0.0", port=7860)
