# Buscador de Termos em PDF

Este é um script Python que busca termos específicos em arquivos PDF dentro de uma pasta e suas subpastas. Ele suporta buscas por termos individuais e combinações de termos (usando `&`). O script exibe os resultados no terminal e gera um PDF com as páginas relevantes e os termos destacados.

---
# Abra a Wiki do projeto para mais informações

## Funcionalidades

- Busca recursiva em todos os PDFs de uma pasta e subpastas.
- Suporte a múltiplos termos de pesquisa.
- Busca por termos individuais ou combinações de termos (usando `&`).
- Exibe no terminal:
  - Nome do arquivo.
  - Número da página.
  - Trecho do texto com contexto (70 caracteres antes e depois do termo).
- Gera um PDF com:
  - Páginas que contêm os termos.
  - Termos destacados com marca-texto.

---

## Como Usar

### Pré-requisitos

- Python 3.x instalado.
- Biblioteca PyMuPDF (`fitz`) instalada.

### Instalação

1. Clone este repositório ou baixe o script `buscador.py`.

2. Instale a biblioteca PyMuPDF:
   ```bash
   pip install pymupdf
   ```

3. Crie um arquivo `termos.txt` na mesma pasta do script. Adicione os termos de busca, um por linha. Para combinações de termos, use `&`:
   ```
   Gustavo
   Carneiro
   Gustavo & Carneiro
   Telecomunicações
   ```

### Execução

1. Coloque os arquivos PDF na pasta onde o script será executado (ou em subpastas).

2. Execute o script:
   ```bash
   python3 buscador.py
   ```

3. O script exibirá os resultados no terminal e gerará dois arquivos:
   - `Resultados_<DATA_HORA>.pdf`: PDF com as páginas relevantes e termos destacados.
   - `Resultados.txt`: Relatório textual com todas as ocorrências.

---

## Exemplo de Uso

### Arquivo `termos.txt`
```
Gustavo
Carneiro
Gustavo & Carneiro
Telecomunicações
```

### Saída no Terminal
```
Processando: ./exemplo.pdf

Arquivo: ./exemplo.pdf
Página: 5
Termo: Gustavo
Contexto: [...] trecho com a palavra Gustavo [...]
================================================================================

Arquivo: ./exemplo.pdf
Página: 10
Termos combinados: Gustavo & Carneiro
================================================================================
```

### Arquivos Gerados
- `Resultados_20231025_1430.pdf`: PDF com as páginas que contêm os termos.

---

## Personalização

- **Termos de busca**: Edite o arquivo `termos.txt` para adicionar ou remover termos.
- **Contexto no terminal**: O script exibe 70 caracteres antes e depois do termo. Para alterar, modifique o valor no código:
  ```python
  trecho = texto[max(0, inicio-70):min(len(texto), fim+70)]
  ```

---

## Contribuição

Contribuições são bem-vindas! Siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Se tiver dúvidas ou sugestões, entre em contato:

- **Nome**: Gustavo Carneiro
- **Telegram**: [Lieva](http://t.me/lievasomal)
- **GitHub**: [gustavocarneiro](https://github.com/quietbytesilence)

---

## Agradecimentos

- À comunidade Python por fornecer ferramentas incríveis.
- Aos mantenedores do PyMuPDF por uma biblioteca poderosa para manipulação de PDFs.

