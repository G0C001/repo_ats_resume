from django.shortcuts import render
from django.http import HttpResponse
from app.body import styleresume, personal, summary, education, experience_certfy, skills, project_lang
# import asyncio
# from playwright.async_api import async_playwright

# async def generate_pdf(html_content):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()

#         # Set the HTML content
#         await page.set_content(html_content)

#         # Generate PDF
#         pdf_file = await page.pdf(format='A4')

#         await browser.close()

#         return pdf_file
    
def resume(request):
    if request.method == 'POST':
        pass
        # role = request.POST.get('Role')
        # skill = request.POST.get('skill')

        # # Generate HTML content for the PDF
        # html_template = f"""
        #                 {styleresume.style()}
        #                 <body>
        #                     <div class="container">
        #                         {personal.personal(role)}
        #                         {summary.summary(role)}
        #                         {education.education()}
        #                         {experience_certfy.experience_certfy()}
        #                         {skills.skill(skill)}
        #                         {project_lang.project_lan()}
        #                     </div>
        #                 </body>
        #             """


        # pdf_file = asyncio.run(generate_pdf(html_template))

        # response = HttpResponse(pdf_file, content_type='application/pdf')
        # response['Content-Disposition'] = f'inline; filename="GokulVasanth_{role}_Resume.pdf"'

        # return response

    return render(request, 'index.html')
