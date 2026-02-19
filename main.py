import webview
import os
import sys

def get_html_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'index.html')
    return os.path.join(os.path.dirname(__file__), 'index.html')

def start_app():
    html_file = get_html_path()
    
    window = webview.create_window(
        'Media Player', 
        html_file,
        width=1100,
        height=700,
        resizable=True,
        background_color='#0e0e12'
    )
    
    webview.start()

if __name__ == '__main__':
    start_app()