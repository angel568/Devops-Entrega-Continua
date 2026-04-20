from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo - DevOps</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Serif+Display&display=swap');

            * { margin: 0; padding: 0; box-sizing: border-box; }

            body {
                min-height: 100vh;
                background: #0a0a0f;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Space Mono', monospace;
                overflow: hidden;
            }

            .grid-bg {
                position: fixed; inset: 0;
                background-image: 
                    linear-gradient(rgba(0,255,136,0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0,255,136,0.05) 1px, transparent 1px);
                background-size: 40px 40px;
                animation: gridMove 20s linear infinite;
            }

            @keyframes gridMove {
                0% { transform: translateY(0); }
                100% { transform: translateY(40px); }
            }

            .container {
                position: relative;
                text-align: center;
                padding: 60px 80px;
                border: 1px solid rgba(0,255,136,0.3);
                background: rgba(10,10,15,0.9);
                backdrop-filter: blur(10px);
                box-shadow: 0 0 60px rgba(0,255,136,0.1), inset 0 0 60px rgba(0,255,136,0.02);
            }

            .container::before {
                content: '';
                position: absolute;
                top: -1px; left: 20px; right: 20px; height: 3px;
                background: linear-gradient(90deg, transparent, #00ff88, transparent);
            }

            .tag {
                font-size: 11px;
                color: #00ff88;
                letter-spacing: 4px;
                text-transform: uppercase;
                margin-bottom: 24px;
                opacity: 0.7;
            }

            h1 {
                font-family: 'DM Serif Display', serif;
                font-size: clamp(48px, 8vw, 96px);
                color: #ffffff;
                line-height: 1;
                margin-bottom: 16px;
            }

            h1 span { color: #00ff88; }

            .subtitle {
                font-size: 13px;
                color: rgba(255,255,255,0.4);
                letter-spacing: 2px;
                margin-bottom: 48px;
            }

            .stack {
                display: flex;
                gap: 12px;
                justify-content: center;
                flex-wrap: wrap;
            }

            .badge {
                padding: 6px 16px;
                border: 1px solid rgba(0,255,136,0.3);
                font-size: 11px;
                letter-spacing: 2px;
                color: #00ff88;
                background: rgba(0,255,136,0.05);
            }

            .cursor {
                display: inline-block;
                width: 3px;
                height: 1em;
                background: #00ff88;
                vertical-align: middle;
                margin-left: 4px;
                animation: blink 1s step-end infinite;
            }

            @keyframes blink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0; }
            }

            .corner {
                position: absolute;
                width: 12px; height: 12px;
                border-color: #00ff88;
                border-style: solid;
            }
            .corner.tl { top: -1px; left: -1px; border-width: 2px 0 0 2px; }
            .corner.tr { top: -1px; right: -1px; border-width: 2px 2px 0 0; }
            .corner.bl { bottom: -1px; left: -1px; border-width: 0 0 2px 2px; }
            .corner.br { bottom: -1px; right: -1px; border-width: 0 2px 2px 0; }
        </style>
    </head>
    <body>
        <div class="grid-bg"></div>
        <div class="container">
            <div class="corner tl"></div>
            <div class="corner tr"></div>
            <div class="corner bl"></div>
            <div class="corner br"></div>
            <p class="tag">// ciclo devops completo</p>
            <h1>Hola <span>Mundo</span><span class="cursor"></span></h1>
            <p class="subtitle">PYTHON · FLASK · DOCKER · DOCKER HUB</p>
            <div class="stack">
                <span class="badge">PYTHON 3.11</span>
                <span class="badge">FLASK 3.0</span>
                <span class="badge">DOCKER</span>
                <span class="badge">CI/CD READY</span>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok", "app": "hola-mundo"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
