import jinja2 as j2

# Criando o modelo
model = "Olá {{nome}}, seja bem vindo(a). Seu email é: {{email}} e seu estado: {{estado}}"

emails = [
    ["cassiana.barreto@dadosfera.io", "Cassiana Barreto", "São Paulo"],
    ["lima.cglima@gmail.com", "Cassiana Lima", "Minas Gerais"],
    ["cassiana.limabarreto@gmail.com", "Cassiana Lima Barreto", "Rio de Janeiro"],
]

# Criando o template com o modelo
template = j2.Template(model)

# Renderizando o template
for email in emails:
    template_render = template.render(nome=email[1], email=email[0],  estado=email[2])
    print(template_render)
