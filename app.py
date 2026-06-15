# -*- coding: utf-8 -*-
import webview
import os
import sys
import base64
import webbrowser


def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'src', filename)


class Api:
    """JS <-> Python bridge.

    Exposes file-save and external-link helpers to the web UI so that
    "İndir" (Excel/CSV export) actually writes a file to disk via a
    native save dialog, and footer links open in the system browser.
    """

    def __init__(self):
        self.window = None

    def save_file(self, filename, base64_data):
        try:
            downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
            if not os.path.isdir(downloads_dir):
                downloads_dir = os.path.expanduser('~')

            result = self.window.create_file_dialog(
                webview.SAVE_DIALOG,
                directory=downloads_dir,
                save_filename=filename,
            )

            if not result:
                return {'success': False, 'cancelled': True}

            path = result if isinstance(result, str) else result[0]

            data = base64.b64decode(base64_data)
            with open(path, 'wb') as f:
                f.write(data)

            return {'success': True, 'path': path}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    def open_link(self, url):
        try:
            webbrowser.open(url)
            return True
        except Exception:
            return False


def main():
    html_path = resource_path('index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    api = Api()
    window = webview.create_window(
        title='PDF → Excel Pro | Talvixa',
        html=html_content,
        width=1300,
        height=840,
        min_size=(960, 640),
        background_color='#0f1117',
        text_select=False,
        js_api=api,
    )
    api.window = window
    webview.start(debug=False)


if __name__ == '__main__':
    main()
