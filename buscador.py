import os
import fitz  # PyMuPDF
import re
from datetime import datetime

def main():
    with open('termos.txt', 'r', encoding='utf-8') as f:
        termos = [line.strip() for line in f if line.strip()]
    if not termos:
        print("Nenhuma palavra-chave encontrada em termos.txt.")
        return
    keywords_individuais = [termo for termo in termos if '&' not in termo]
    keywords_combinados = [termo.split('&') for termo in termos if '&' in termo]
    referencias = []
    for raiz, _, arquivos in os.walk('.'):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.pdf'):
                caminho_pdf = os.path.join(raiz, arquivo)
                try:
                    doc = fitz.open(caminho_pdf)
                except Exception as e:
                    print(f"Erro ao abrir arquivo {caminho_pdf}: {e}")
                    continue
                print(f"\nProcessando: {caminho_pdf}")
                for num_pag in range(len(doc)):
                    try:
                        pagina = doc.load_page(num_pag)
                        texto = pagina.get_text()
                        for palavra in keywords_individuais:
                            padrao = re.compile(re.escape(palavra), re.IGNORECASE)
                            for match in padrao.finditer(texto):
                                inicio, fim = match.start(), match.end()
                                trecho = texto[max(0, inicio-70):min(len(texto), fim+70)]
                                trecho = trecho.replace('\n', ' ').strip()
                                print(
                                    f"Arquivo: {caminho_pdf}\n"
                                    f"Página: {num_pag + 1}\n"
                                    f"Termo: {palavra}\n"
                                    f"Contexto: [...] {trecho} [...]\n"
                                    + "="*80 + "\n"
                                )
                                referencias.append({
                                    'arquivo': caminho_pdf,
                                    'pagina': num_pag,
                                    'palavra': palavra,
                                    'inicio': inicio,
                                    'fim': fim
                                })
                        for combinacao in keywords_combinados:
                            termos_combinados = [termo.strip() for termo in combinacao]
                            if all(re.search(re.escape(termo), texto, re.IGNORECASE) for termo in termos_combinados):
                                print(
                                    f"Arquivo: {caminho_pdf}\n"
                                    f"Página: {num_pag + 1}\n"
                                    f"Termos combinados: {' & '.join(termos_combinados)}\n"
                                    + "="*80 + "\n"
                                )
                                referencias.append({
                                    'arquivo': caminho_pdf,
                                    'pagina': num_pag,
                                    'palavra': ' & '.join(termos_combinados),
                                    'inicio': 0,  # Não aplicável para termos combinados
                                    'fim': 0       # Não aplicável para termos combinados
                                })
                    except Exception as e:
                        print(f"Erro ao processar página {num_pag + 1} do arquivo {caminho_pdf}: {e}") 
                doc.close()
    if referencias:
        output_doc = fitz.open()
        print("Montando Arquivo.\nPor favor aguarde.")
        
        for ref in referencias:
            try:
                doc = fitz.open(ref['arquivo'])
                pagina = doc.load_page(ref['pagina'])
                output_doc.insert_pdf(doc, from_page=ref['pagina'], to_page=ref['pagina'])
                pagina_saida = output_doc[-1]
                if '&' not in ref['palavra']:
                    quads = pagina_saida.search_for(ref['palavra'], quads=True)
                    for quad in quads:
                        pagina_saida.add_highlight_annot(quad).update()
                else:
                    termos_combinados = ref['palavra'].split(' & ')
                    for termo in termos_combinados:
                        quads = pagina_saida.search_for(termo, quads=True)
                        for quad in quads:
                            pagina_saida.add_highlight_annot(quad).update()
                doc.close()
            except Exception as e:
                print(f"Erro ao processar referência {ref}: {e}")
        nome_pdf = f"Resultados_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        output_doc.save(nome_pdf)
        print(f"\nPDF com destaques salvo como: {nome_pdf}")
        output_doc.close()
    else:
        print("\nNenhuma ocorrência encontrada.")

if __name__ == "__main__":
    main()
