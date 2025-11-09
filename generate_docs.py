import inspect
import os
from datetime import datetime

def generate_docs():
    """Генерирует HTML документацию из docstrings"""
    
    # Читает исходный код steam_service.py
    with open('app/services/steam_service.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Извлекает docstrings
    docs = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if 'def ' in line and '):' in line:
            func_name = line.split('def ')[1].split('(')[0]
            
            # Ищет docstring
            docstring = ''
            for j in range(i+1, min(i+10, len(lines))):
                if '"""' in lines[j] or "'''" in lines[j]:
                    # Начало docstring
                    doc_lines = []
                    for k in range(j, len(lines)):
                        doc_lines.append(lines[k])
                        if '"""' in lines[k] or "'''" in lines[k]:
                            if k != j:  # Не первая строка
                                break
                    docstring = '\n'.join(doc_lines)
                    break
            
            docs.append({'name': func_name, 'doc': docstring})

    # Генерирует HTML
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Steam Service Documentation</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .function {{ background: #f5f5f5; padding: 20px; margin: 15px 0; border-radius: 8px; }}
            .function-name {{ font-weight: bold; color: #2c3e50; font-size: 1.2em; }}
            .doc {{ white-space: pre-wrap; background: white; padding: 15px; border-radius: 5px; margin-top: 10px; }}
            .timestamp {{ color: #7f8c8d; font-style: italic; }}
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
    with open('docs/steam_service_docs.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Documentation generated successfully!")

if __name__ == "__main__":
    generate_docs()