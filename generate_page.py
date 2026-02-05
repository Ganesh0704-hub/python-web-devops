from datetime import datetime 

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Python DevOps Web Output</title>
</head>
<body>
    <h1>🚀 Python DevOps Automation</h1>
    <h3> hello Ganesh <h3>
    <h3> hello Keerthana <h3>
    <h3> hello sanjeet <h3>
    
    <p>This page was generated automatically.</p>
    <p><b>Last updated:</b> {datetime.now()}</p>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_content)

print("Web page generated successfully")
