from django.shortcuts import render, redirect
from app.body import styleresume, personal, summary, education, experience_certfy, skills, project_lang
from django.http import HttpResponse
import json
# import ctypes
# import os
# dll_directory = r"./GTK3"
# for file_name in os.listdir(dll_directory):
#     if file_name.endswith(".dll"):
#         dll_path = os.path.join(dll_directory, file_name)
#         try:
#             my_dll = ctypes.CDLL(dll_path)
#         except Exception as e:
#             print(f"Failed to load {dll_path}: {e}")
# from weasyprint import HTML

def resume(request):
    if request.method == 'POST':
        role = request.POST.get('Role')
        skill = request.POST.get('skill')
        skills_dict = json.loads(skill)
        global html_content
        html_content = f"""
                        {styleresume.style()}
                        <body>
                            <div class="container">
                                {personal.personal(role)}
                                {summary.summary(role)}
                                {education.education()}
                                {experience_certfy.experience_certfy()}
                                {skills.skill(skills_dict)}
                                {project_lang.project_lan()}
                            </div>
                                <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
                                <script>
                                    const element = document.getElementById('resume');
                                    html2pdf()
                                        .from(element)
                                        .save('Gokul_Vasanth_{role}_Resume.pdf');
                                </script>
                        </body>
                        </html>
                    """
         # Create a PDF response
        # pdf = HTML(string=html_content).write_pdf()
        
        # Set up the response
        # response = HttpResponse(pdf, content_type='application/pdf')
        # response['Content-Disposition'] = f'attachment; filename="Gokul_Vasanth_{role}_Resume.pdf"'
        
        return 'response'

    return render(request, 'index.html')

# def download(request):

#     return render(request, 'download.html', {'html_content': html_content})
