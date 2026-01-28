from flask import Flask, request, render_template, send_file, flash
import yt_dlp
import os
import tempfile

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # सुरक्षा के लिए एक रैंडम की रखें

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        flash('कृपया एक वैध URL दर्ज करें।')
        return render_template('index.html')
    
    try:
        # yt-dlp के साथ वीडियो डाउनलोड करें
        with tempfile.TemporaryDirectory() as temp_dir:
            ydl_opts = {
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'format': 'best',  # सर्वोत्तम गुणवत्ता
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            
            # फाइल वापस भेजें
            return send_file(filename, as_attachment=True)
    except Exception as e:
        flash(f'डाउनलोड विफल: {str(e)}')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)