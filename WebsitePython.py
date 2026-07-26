from flask import Flask, render_template_string

app = Flask(__name__)

# -----------------------
# CSS (shared by all pages)
# -----------------------

STYLE = """
<style>
body{
    margin:0;
    font-family:Arial, Helvetica, sans-serif;
    background:#f4f4f4;
}

header{
    background:#1f4d7a;
    color:white;
    padding:20px;
}

nav{
    margin-top:10px;
}

nav a{
    color:white;
    text-decoration:none;
    margin-right:20px;
    font-weight:bold;
}

nav a:hover{
    text-decoration:underline;
}

main{
    width:80%;
    margin:auto;
    margin-top:30px;
    padding:40px;
    background:white;
    border-radius:10px;
    box-shadow:0px 0px 10px rgba(0,0,0,.2);
}

button{
    background:#1f4d7a;
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:5px;
    cursor:pointer;
}

button:hover{
    background:#356ea3;
}

input, textarea{
    width:100%;
    padding:10px;
    border-radius:5px;
    border:1px solid #ccc;
    margin-bottom:15px;
}

footer{
    text-align:center;
    padding:20px;
    color:#666;
}
</style>
"""

# -----------------------
# Home Page
# -----------------------

@app.route("/")
def home():
    return render_template_string(f"""
<!DOCTYPE html>
<html>

<head>
<title>My Python Website</title>
{STYLE}
</head>

<body>

<header>
<h1>My Python Website</h1>

<nav>
<a href="/">Home</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
</nav>
</header>

<main>

<h2>Welcome!</h2>

<p>
This website is completely powered by Python and Flask.
</p>

<p>
Everything you are seeing is generated from a single Python file.
</p>

<button onclick="hello()">
Click Me
</button>

</main>

<footer>
Created with Flask
</footer>

<script>
function hello(){{
    alert("Hello from Python!");
}}
</script>

</body>
</html>
""")


# -----------------------
# About Page
# -----------------------

@app.route("/about")
def about():
    return render_template_string(f"""
<!DOCTYPE html>
<html>

<head>
<title>About</title>
{STYLE}
</head>

<body>

<header>
<h1>About</h1>

<nav>
<a href="/">Home</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
</nav>

</header>

<main>

<h2>About This Website</h2>

<p>
This website demonstrates how Flask can generate web pages using only Python.
</p>

<ul>
<li>Python Backend</li>
<li>HTML Rendering</li>
<li>CSS Styling</li>
<li>JavaScript Interaction</li>
</ul>

</main>

<footer>
Thanks for visiting!
</footer>

</body>
</html>
""")


# -----------------------
# Contact Page
# -----------------------

@app.route("/contact")
def contact():
    return render_template_string(f"""
<!DOCTYPE html>
<html>

<head>
<title>Contact</title>
{STYLE}
</head>

<body>

<header>
<h1>Contact</h1>

<nav>
<a href="/">Home</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
</nav>
</header>

<main>

<h2>Contact Us</h2>

<form>

<label>Name</label>
<input type="text">

<label>Email</label>
<input type="email">

<label>Message</label>
<textarea rows="6"></textarea>

<button type="submit">
Send Message
</button>

</form>

</main>

<footer>
Example Flask Website
</footer>

</body>
</html>
""")


# -----------------------
# Start the server
# -----------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
