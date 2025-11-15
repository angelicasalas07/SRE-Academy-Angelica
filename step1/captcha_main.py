from flask import Flask, render_template

captcha_test_app = Flask(__name__)

@captcha_test_app.route('/')
def Home():
    #return ('button.html')
    return render_template('captcha_widget.html')
    
# @captcha_test_app.get('/widget') # 'http://127.0.0.1:5000/widget'
# def get_widget():
#     return render_template('captcha_widget.html')

if __name__ == '__main__':
    captcha_test_app.run(debug=True)