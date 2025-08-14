from flask import Flask, request, jsonify
import pysolr

app = Flask(__name__)

solr = pysolr.Solr('http://localhost:8983/solr/cbo', always_commit=True)

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')
    if not termo:
        return jsonify({"erro": "Informe o parâmetro 'termo'"}), 400
    
    resultados = solr.search(f"titulo:*{termo}* OR codigo:*{termo}*")
    return jsonify([{"codigo": r["codigo"], "titulo": r["titulo"]} for r in resultados])

if __name__ == '__main__':
    app.run(debug=True)
