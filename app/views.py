from django.shortcuts import render, redirect
from app.body import styleresume, personal, summary, education, experience_certfy, skills, project_lang
import json
def resume(request):
    if request.method == 'POST':
        role = request.POST.get('Role')
        skill = request.POST.get('skill')
        skill_dict = json.loads(skill)
        global html_content
        html_content = f"""
                        {styleresume.style()}
                        <body>
                            <div class="container">
                                {personal.personal(role)}
                                {summary.summary(role)}
                                {education.education()}
                                {experience_certfy.experience_certfy()}
                                {skills.skill(skill_dict)}
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
        return redirect('download')

    return render(request, 'index.html')

def download(request):

    return render(request, 'download.html', {'html_content': html_content})
