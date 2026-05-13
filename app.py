# -*- coding: utf-8 -*-
"""
PDF → Excel Pro v2.0
Mali Müşavirlik Sürümü
Levent Emirhan Özhan tarafından geliştirilmiştir.
"""

import webview
import os
import sys

def resource_path(filename):
    """PyInstaller ile paketlenince doğru yolu bul."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', filename)

def main():
    html_path = resource_path('index.html')

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    window = webview.create_window(
        title='PDF → Excel Pro | Mali Müşavirlik — Levent Emirhan Özhan',
        html=html_content,
        width=1300,
        height=840,
        min_size=(960, 640),
        background_color='#0f1117',
        text_select=False,
    )

    webview.start(debug=False)

if __name__ == '__main__':
    main()
