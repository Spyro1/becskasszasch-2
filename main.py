from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Secret key for session management

# # Főoldal endpoint
# @app.route('/')
# def home():
#     return render_template('home.html')

# # Login endpoint
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # Példa logika admin ellenőrzéshez
#         if username == 'admin' and password == 'admin':
#             session['user'] = 'admin'
#         else:
#             session['user'] = 'user'
#         return redirect(url_for('home'))
#     return render_template('login.html')

# # Register endpoint
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # Itt kezelheted a regisztrációs logikát
#         return redirect(url_for('home'))
#     return render_template('register.html')

# # Kilépés endpoint
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)