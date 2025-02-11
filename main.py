import os
from gg import Tele
import requests
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/chk/<name>', methods=['GET'])
def vbv(name):
    try:
        gg = str(Tele(name))

        # تحديد مسار الملف حيث سيتم حفظ النتيجة
        file_path = "results.txt"

        # إذا لم يكن الملف موجودًا، سيتم إنشاؤه
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("Results Log\n")
                file.write("==================\n\n")

        # تنسيق الرسالة التي سيتم حفظها
        message = f"""
        CC: {name}

        RESPONSE: {gg}

        """

        # فتح الملف وإضافة الرسالة الجديدة
        with open(file_path, "a") as file:
            file.write(message + "\n\n")

        # إرجاع النتيجة إلى المستخدم
        return gg

    except Exception as e:
        app.logger.error(f"Error: {e}")
        return f"An error occurred: {e}", 500

@app.route('/do', methods=['GET'])
def download_file():
    # مسار الملف الذي سيتم تنزيله
    file_path = "results.txt"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404


if __name__ == '__main__':
    # استخدام المنفذ الذي توفره Heroku
    port = int(os.environ.get('PORT', 5000))  # إذا لم يتم تعيين المتغير، استخدم 5000 كخيار افتراضي
    app.run(host='0.0.0.0', port=port)
