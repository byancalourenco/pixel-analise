# pega a função que analisa, que esta no arquivo analyzer.py
from modules.continuity.analyzer import analyze_continuity

# guarda o arquivo enviado
imagem = "document_editado.png"

#  passando a imagem para a função
result = analyze_continuity(
    imagem
)

# exibir o resultado
print(result)