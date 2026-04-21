from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils.predictor import extract_sugar_levels_from_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []

    if request.method == 'POST':
        fasting = request.form.get('fasting')
        postmeal = request.form.get('postmeal')
        uploaded_file = request.files.get('report')

        # ✅ Manual Input Logic
        try:
            if fasting:
                f = int(fasting)
                if f < 70:
                    result.append(f"Fasting: {f} mg/dL - Critical (Too Low)")
                elif f > 110:
                    result.append(f"Fasting: {f} mg/dL - Critical (Too High)")
                else:
                    result.append(f"Fasting: {f} mg/dL - Normal")

            if postmeal:
                p = int(postmeal)
                if p < 110:
                    result.append(f"Post-Meal: {p} mg/dL - Critical (Too Low)")
                elif p > 160:
                    result.append(f"Post-Meal: {p} mg/dL - Critical (Too High)")
                else:
                    result.append(f"Post-Meal: {p} mg/dL - Normal")
        except ValueError:
            result.append("Please enter valid numbers.")

        # ✅ Uploaded Report Logic
        if uploaded_file and uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)

            try:
                values, _ = extract_sugar_levels_from_image(filepath)
                if not values:
                    result.append("No valid sugar values found in uploaded report.")
                else:
                    if 'fasting' in values:
                        f = values['fasting']
                        if f < 70:
                            result.append(f"Fasting (from image): {f} mg/dL - Critical (Too Low)")
                        elif f > 110:
                            result.append(f"Fasting (from image): {f} mg/dL - Critical (Too High)")
                        else:
                            result.append(f"Fasting (from image): {f} mg/dL - Normal")

                    if 'postmeal' in values:
                        p = values['postmeal']
                        if p < 110:
                            result.append(f"Post-Meal (from image): {p} mg/dL - Critical (Too Low)")
                        elif p > 160:
                            result.append(f"Post-Meal (from image): {p} mg/dL - Critical (Too High)")
                        else:
                            result.append(f"Post-Meal (from image): {p} mg/dL - Normal")
            except Exception as e:
                result.append(f"Error processing uploaded image: {str(e)}")

    return render_template('index.html', result=result)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
