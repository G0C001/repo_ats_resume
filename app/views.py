from django.shortcuts import render
from django.http import HttpResponse
from app.body import styleresume, personal, summary, education, experience_certfy, skills, project_lang
from weasyprint import HTML

def resume(request):
    # if request.method == 'POST':
        # role = request.POST.get('Role')
        # skill = request.POST.get('skill')
        
        # html_template = f"""
        #     {styleresume.style()}
        #     <body>
        #         <div class="container">
        #             {personal.personal(role)}
        #             {summary.summary(role)}
        #             {education.education()}
        #             {experience_certfy.experience_certfy()}
        #             {skills.skill(skill)}
        #             {project_lang.project_lan()}
        #         </div>
        #     </body>
        # """
        # pdf_file = HTML(string=html_template).write_pdf()

        # response = HttpResponse(pdf_file, content_type='application/pdf')
        # response['Content-Disposition'] = f'inline; filename="GokulVasanth_{role}_Resume.pdf"'

        # return response
        
    return render(request, 'index.html')
