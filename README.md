# Jinja

- Sistema de template para Python
- Popula e renderiza um template usando:
  - Variáveis passadas para o template
  - Tags de controle
    - Condicionais
    - Looping
    - Inclusão de outros templates
    - Herança de templates
    - Macros
  - Filtros
- Integra bem com Flask

## Instalação

    ```bash
    pip install jinja2
    ```

- Tudo no jinja é feito atraves de um ambiente (environment)
  - O ambiente é responsável por armazenar as configurações do jinja

## Template basics

- Um template é um arquivo de texto com variáveis e tags de controle

### Variáveis

- São delimitadas por `{{ }}`
- Exemplo:

    {{ user.name }}

### Tags de controle

- São delimitados por `{% %}`
- Exemplo:

    {% if user %}
        {{ user.name }}
    {% endif %}

### Conditionals

- Executa um bloco de código se uma condição for verdadeira
- Exemplo:

    {% if user %}
        {{ user.name }}
    {% else %}
        {{ 'No user' }}
    {% endif %}

### Filters

- São funções que modificam o valor de uma variável
- São aplicados com o pipe `|`

- Exemplo: `{{ var|safe }}`
    safe
    capitalize
    lower
    upper
    title
    trim
    striptags

### Loops

- Itera sobre uma lista de itens
- Exemplo:

    {% for item in items %}
        {{ item }}
    {% endfor %}

### Includes

- Inclui um template dentro de outro
- Exemplo:

    {% include 'header.html' %}

### Herança

- Permite criar um template base e extender ele em outros templates
- Exemplo:

    {% extends 'base.html' %}

### Macros

- Define um bloco de código que pode ser reutilizado
- Exemplo:

    {% macro input(name, value='') %}
        <input type="text" name="{{ name }}" value="{{ value }}">
    {% endmacro %}

### Comentários

- Comentários em jinja são feitos com `{# #}`
- Exemplo:

    {# This is a comment #}

## Referências

- [Primer on Jinja Templating](https://realpython.com/primer-on-jinja-templating/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)