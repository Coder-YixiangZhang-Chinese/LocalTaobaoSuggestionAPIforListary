from flask import Flask, request, jsonify
import requests
import socket
import sys

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0

if is_port_in_use(60000):
    print("服务已经在运行。")
    sys.exit(0)  # 如果端口已经被占用，则退出

app = Flask(__name__)

def fetch_taobao_suggestions(query):
    url = f"https://suggest.taobao.com/sug?code=utf-8&q={query}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            return [item[0] for item in data.get("result", [])]
    except Exception as e:
        print(f"Error fetching suggestions: {e}")
    return []

@app.route("/suggest")
def suggest():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    suggestions = [query]
    results = fetch_taobao_suggestions(query)
    suggestions += [s for s in results if s != query]

    subtypes = [[512] for _ in suggestions]

    output = [
        query,
        suggestions,
        [],
        {"google:suggestsubtypes": subtypes}
    ]

    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=60000, threaded=False, processes=1)