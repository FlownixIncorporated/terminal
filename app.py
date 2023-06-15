import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def execute():
    output = ""
    if request.method == "POST":
        command = request.form['command']

        try:
            output =  subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        except subprocess.CalledProcessError as e:
            output = e.output.decode('utf-8')

    return f"""    
    <!DOCTYPE html>
    <html>
    <head>
        <title>Terminal Command Executor</title>
    </head>
    <body>
        <h1 style="font-family:sans-serif; text-align:center; margin-top:8em !important;">Terminal Command Executor</h1>
        <form method="POST" style="text-align:center;">
            <input type="text" name="command" placeholder="Enter a command" required style="border-radius:2em; text-align:center; height:2em; width:20em; outline:none;"></br>
            <button type="submit" style="width:10em; height:2.5em; text-align:center; background-color:aqua; border-radius:2em; border:none; margin-top:1em;">Execute</button>
        </form>
            <h2 style="font-family:sans-serif; text-align:center; margin-top:5em !important;">Output:</h2>
            <pre style="font-family:monospace; text-align:center;">{ output if output != "" else "" }</pre>
    </body>
    </html>
    """
