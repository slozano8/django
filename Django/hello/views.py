from django.http import HttpResponse
HTML_STRING = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payroll Information</title>
</head>
<body>
    <h1>Payroll Information Form</h1>
    <form action="/process_data" method="post">
        <!-- Input field for name -->
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required><br>

        <!-- Input field for rate of pay -->
        <label for="rate">Rate of Pay (per hour):</label>
        <input type="number" id="rate" name="rate" min="0" step="0.01" placeholder="Enter rate" required><br>

        <!-- Input field for hours worked -->
        <label for="hours">Hours Worked:</label>
        <input type="number" id="hours" name="hours" min="0" step="0.01" placeholder="Enter hours" required><br>

        <!-- Submit button -->
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""
def home(request):
    return HttpResponse(HTML_STRING)
# Create your views here.

    