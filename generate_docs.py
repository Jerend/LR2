import os
from datetime import datetime

def generate_docs():
    """Генерирует HTML документацию из docstrings файла steam_service.py"""
    
    # Читает исходный код steam_service.py
    with open('app/services/steam_service.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Извлекает функции и их docstrings
    docs = []
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        if 'def ' in line and '):' in line:
            func_name = line.split('def ')[1].split('(')[0]
            
            # Ищет docstring
            docstring = ''
            j = i + 1
            while j < len(lines):
                if '"""' in lines[j]:
                    # Нашли начало docstring
                    doc_lines = []
                    start_line = j
                    
                    # Собираем docstring
                    k = start_line
                    while k < len(lines):
                        doc_lines.append(lines[k])
                        if '"""' in lines[k] and k != start_line:  # Закрывающая кавычка
                            break
                        k += 1
                    
                    docstring = '\n'.join(doc_lines)
                    break
                j += 1
            
            docs.append({'name': func_name, 'doc': docstring})
        i += 1

    # Генерирует HTML
    html_content = f"""
    <!DOCTYPE html>
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
        
        {"".join([f'''
        <div class="function">
            <div class="function-name">📖 {doc['name']}</div>
            <div class="doc">{doc['doc'] or 'Нет документации'}</div>
        </div>
        ''' for doc in docs])}
        
        <div class="timestamp">Сгенерировано: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
    </body>
    </html>
    """
        
    # Создает папку docs если нет
    os.makedirs('docs', exist_ok=True)
    
    # Сохраняет HTML
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Documentation generated successfully!")

if __name__ == "__main__":
    generate_docs()