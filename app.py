from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
    <html>
        <head>
            <title>Welcome</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    font-family: 'Arial', sans-serif;
                    background-color: rgba(255, 192, 203, 0.7); 
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    color: #333;
                }
                .container {
                    text-align: center;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #5D3FD3;
                }
                a {
                    text-decoration: none;
                    color: white;
                    background-color: #5D3FD3;
                    padding: 10px 15px;
                    border-radius: 5px;
                    transition: background-color 0.3s ease;
                }
                a:hover {
                    background-color: #7A5FD3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the E-commerce Catalog!</h1>
                <a href="/catalog">View Catalog</a>
            </div>
        </body>
    </html>
    '''

@app.route('/catalog')
def catalog():
    # In a real app, you would probably pull these from a database
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template_string('''
    <html>
        <head>
            <title>Catalog</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: rgba(255, 150, 203, 0.7);
                    margin: 0;
                    padding: 0;
                }
                .catalog-container {
                    width: 80%;
                    margin: 0 auto;
                    padding: 20px;
                }
                .item {
                    background-color: #ffffff;
                    border: 1px solid #dddddd;
                    padding: 10px;
                    margin-bottom: 10px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                .item:hover {
                    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                }
            </style>
        </head>
        <body>
            <div class="catalog-container">
                <h1>Catalog Items</h1>
                {% for item in items %}
                <div class="item">{{ item }}</div>
                {% endfor %}
            </div>
        </body>
    </html>
    ''', items=items)

if __name__ == '__main__':
    app.run(debug=True)