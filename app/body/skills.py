def skill(skills_new):
    skills_dict = skills_new

    add = ''
    for key in skills_dict:
            add += f"<li><strong>{key}:</strong> {', '.join(skills_dict[key])}</li>"
    skills_html = f"""
    <section class="section">
        <h2>Skills</h2>
        <ul class="skills">
            {add}
        </ul>
    </section>"""

    return skills_html

# skills_new = {
#         "Frontend": ["HTML", "CSS", "Bootstrap", "JavaScript", "AJAX"],
#         "Backend": ["Python", "Django", "MySQL", "REST APIs"],
#         "Tools": ["GitHub", "Visual Studio Code", "Jupyter Notebook"],
#         "OS": ["Linux", "Windows"],
#         "Other Skills": []
#     }
# print(skill(skills_new))
