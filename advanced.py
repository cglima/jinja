from jinja2 import FileSystemLoader, Environment

# carrega o arquivo do template
loader = FileSystemLoader('templates')
env = Environment(loader=loader)
template = env.get_template('homepage.html')


file = open('output/index.html', 'w')


# renderiza o template (arquivo html)
template_render = template.render(titulo= "Teste com jinja", cor_fundo="#000", cor_texto="#FFF", nome="Cassiana")
file.write(template_render)
file.close()