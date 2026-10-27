from flask import Flask, request, jsonify, render_template_string
from operacoes_basicas import somar, subtrair, multiplicar, dividir

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Flask</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 50px auto; padding: 20px; }
        .input-group { display: flex; gap: 10px; margin-bottom: 15px; align-items: center; }
        input, select, button { padding: 10px; font-size: 16px; }
        input[type="number"] { flex: 1; }
        select { width: 100px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; width: 100%; }
        button:hover { background: #0056b3; }
        #res { margin-top: 20px; font-size: 18px; font-weight: bold; text-align: center; }
    </style>
</head>
<body>
    <h1>Calculadora</h1>
    <div class="input-group">
        <input type="number" id="a" placeholder="Número 1" step="any">
        <select id="op">
            <option value="somar">+</option>
            <option value="subtrair">-</option>
            <option value="multiplicar">*</option>
            <option value="dividir">/</option>
        </select>
        <input type="number" id="b" placeholder="Número 2" step="any">
    </div>
    <button onclick="calcular()">Calcular</button>
    <p id="res"></p>

    <script>
        async function calcular() {
            const a = parseFloat(document.getElementById('a').value);
            const b = parseFloat(document.getElementById('b').value);
            const op = document.getElementById('op').value;
            const r = await fetch('/calcular', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({a, b, op})
            });
            const d = await r.json();
            document.getElementById('res').innerText = d.resultado !== undefined ? d.resultado : d.erro;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    a, b, op = data['a'], data['b'], data['op']
    if op == 'somar':
        return jsonify({'resultado': somar(a, b)})
    if op == 'subtrair':
        return jsonify({'resultado': subtrair(a, b)})
    if op == 'multiplicar':
        return jsonify({'resultado': multiplicar(a, b)})
    if op == 'dividir':
        return jsonify({'resultado': dividir(a, b)})
    return jsonify({'erro': 'Operação inválida'})

if __name__ == '__main__':
    app.run(debug=True)