from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = """
with open('lista_tarefas.txt', 'w+', encoding='utf-8'):

"""

html_code = highlight(code, PythonLexer(), HtmlFormatter(style="fruity"))
print(html_code)