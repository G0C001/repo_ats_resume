from django.shortcuts import render
from django.http import HttpResponse
import pdfkit

def resume(request):
    if request.method == 'POST':
        # Example data retrieval from POST request
        role = request.POST.get('Role')
        skill = request.POST.get('skill')

        # Generate HTML content for the PDF
        html_template = f"""
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    .container {{ max-width: 800px; margin: auto; }}
                    h1 {{ color: #333; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Resume for {role}</h1>
                    <p>Skills: {skill}</p>
                    <p>Here is a summary of qualifications...</p>
                </div>
            </body>
            </html>
        """

        # Convert HTML to PDF using pdfkit
        pdf_file = pdfkit.from_string(html_template, False)

        # Create an HTTP response with the PDF file
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Resume_{role}.pdf"'

        return response

    return render(request, 'index.html')  # Render your main form page
