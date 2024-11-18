import streamlit.components.v1 as components

MERMAID_HTML = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.4.0/mermaid.min.js"></script>
    <style>
        #container {
            position: relative;
            width: 100%;
            height: 700px;
        }
        #graph { 
            width: 100%;
            height: 100%;
            padding-top: 40px;
        }
        .controls { 
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 1000;
            background: rgba(38, 39, 48, 0.9);
            padding: 5px;
            border-radius: 4px;
        }
        .controls button {
            margin: 0 5px;
            padding: 5px 10px;
            background: #FF4B4B;
            color: black;
            border: none;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div id="container">
        <div class="controls">
            <button onclick="adjustZoom(0.1)">➕</button>
            <button onclick="resetZoom()">⟲</button>
            <button onclick="adjustZoom(-0.1)">➖</button>
        </div>
        <pre class="mermaid" id="graph"></pre>
    </div>
    
    <script>
        console.log('Mermaid viewer initialized');
        let zoom = 1;
        
        mermaid.initialize({
            startOnLoad: true,
            theme: 'dark',
            securityLevel: 'loose'
        });
        
        function updateDiagram(code) {
            console.log('Updating diagram with code:', code);
            const element = document.getElementById('graph');
            element.innerHTML = code;
            mermaid.run().catch(console.error);
        }
        
        function adjustZoom(delta) { 
            zoom = Math.max(0.1, Math.min(5, zoom + delta)); 
            updateZoom(); 
        }
        function resetZoom() { zoom = 1; updateZoom(); }
        
        function updateZoom() {
            const svg = document.querySelector('svg');
            if (svg) svg.style.transform = `scale(${zoom})`;
        }

        window.addEventListener('message', function(event) {
            console.log('Message received:', event.data);
            if (event.data.code) updateDiagram(event.data.code);
        });
    </script>
</body>
</html>
"""


def render_mermaid(mermaid_code: str, height: int = 800):
    """Render Mermaid diagram with zoom controls"""
    components.html(
        MERMAID_HTML
        + f"""
        <script>
        console.log('Injecting mermaid code');
        window.postMessage({{ code: {repr(mermaid_code)} }}, '*');
        </script>
        """,
        height=height,
        scrolling=True,
    )
