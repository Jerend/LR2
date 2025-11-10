import os
import ast
from datetime import datetime

def generate_docs():
    """Генерирует HTML документацию из docstrings файла steam_service.py"""
    
    try:
        # Читаем и парсим файл с помощью ast
        with open('app/services/steam_service.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        docs = []
        
        # Ищем все функции и методы
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_name = node.name
                docstring = ast.get_docstring(node)
                
                docs.append({
                    'name': func_name,
                    'doc': docstring or 'Нет документации'
                })
        
        # Генерируем HTML
        html_content = generate_html_content(docs)
        
        # Создаем папку docs если нет
        os.makedirs('docs', exist_ok=True)
        
        # Сохраняем HTML
        with open('docs/index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Создаем файл .nojekyll
        with open('docs/.nojekyll', 'w') as f:
            f.write('')
        
        print(f"Documentation generated successfully! Found {len(docs)} functions.")
        
    except Exception as e:
        print(f"Error generating documentation: {e}")
        # Создаем базовую документацию в случае ошибки
        create_fallback_docs()

def generate_html_content(docs):
    """Генерирует HTML контент"""
    functions_html = "".join([
        f'''
        <div class="function">
            <div class="function-name">📖 {doc['name']}</div>
            <div class="doc">{doc['doc']}</div>
        </div>
        ''' for doc in docs
    ])
    
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Steam Service Documentation</title>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .function {{ background: #f5f5f5; padding: 20px; margin: 15px 0; border-radius: 8px; }}
        .function-name {{ font-weight: bold; color: #2c3e50; font-size: 1.2em; margin-bottom: 10px; }}
        .doc {{ white-space: pre-wrap; background: white; padding: 15px; border-radius: 5px; }}
        .timestamp {{ color: #7f8c8d; font-style: italic; margin-top: 30px; }}
        h1 {{ color: #2c3e50; }}
    </style>
</head>
<body>
    <h1>📚 Steam Service Documentation</h1>
    <p>Автоматически сгенерированная документация из docstrings</p>
    
    {functions_html if functions_html else '<p>Функции не найдены</p>'}
    
    <div class="timestamp">Сгенерировано: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
</body>
</html>"""

def create_fallback_docs():
    """Создает резервную документацию в случае ошибки"""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Steam Service Documentation</title>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .error {{ color: red; }}
    </style>
</head>
<body>
    <h1>📚 Steam Service Documentation</h1>
    <p class="error">Ошибка при генерации документации. Проверьте структуру файла steam_service.py</p>
    <div class="timestamp">Сгенерировано: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
</body>
</html>"""
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    with open('docs/.nojekyll', 'w') as f:
        f.write('')

if __name__ == "__main__":
    generate_docs()