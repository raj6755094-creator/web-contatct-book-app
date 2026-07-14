import os
from flask import Flask, render_template

# 1. Sabse pehle absolute path set karein taaki PythonAnywhere ko folders mil sakein
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(base_dir, 'static')
)

# [Optional] Agar aapka contacts database se nahi aa raha hai, 
# toh aap is tarah ka temporary dummy data rakh sakte hain test karne ke liye:
all_contacts = [
    {"name": "Raj", "phone": "1234567890", "email": "raj@example.com"},
    {"name": "Rahul", "phone": "9876543210", "email": "rahul@example.com"}
]

# 2. Aapka Main Home Route
@app.route('/')
def home():
    # render_template ko 'index.html' aur 'contacts' pass kar rahe hain
    return render_template('index.html', contacts=all_contacts)

# 3. App ko run karne ke liye (Local testing ke liye bhi kaam aayega)
if __name__ == '__main__':
    app.run(debug=True)
