# Projetos do curso

Cada projeto deve ficar em uma subpasta própria, identificada pelo número da
aula e por um nome descritivo em `snake_case`.

Estrutura recomendada:

```text
Projetos/
└── <numero>.<nome_do_projeto>/
    ├── README.md        # objetivo, requisitos e critérios de avaliação
    ├── main.py          # ponto inicial do programa
    ├── modulo.py        # scripts adicionais, somente quando necessários
    └── data/            # fontes de dados, somente quando necessárias
        ├── raw/         # arquivos originais, que nunca devem ser alterados
        └── processed/   # resultados de limpeza ou transformação
```

Projetos pequenos podem conter apenas `README.md` e `main.py`. A organização
deve crescer junto com a necessidade real do projeto.
