def skill(skills_new):
    new_skills = skills_new
    skills_list = new_skills.split(',')

    default_skills = [
        "HTML", "CSS", "Bootstrap", "JavaScript", "AJAX",
        "Python", "Django", "MySQL",
        "GitHub", "Visual Studio Code", "Jupyter Notebook",
        "Linux", "Windows",
    ]
    add = ''
    for skill in skills_list:
        if skill not in default_skills:
            add += skill.strip() + ', '
    if add:
        add = add[:-2]
    skills_list_items = f'<li><strong>Other Skills:</strong> {add}</li>'
    skills = f"""
            <section class="section">
            <h2>Skills</h2>
            <ul class="skills">
            <li><strong>Frontend:</strong> HTML, CSS, Bootstrap, JavaScript, AJAX</li>
            <li><strong>Backend:</strong> Python, Django, MySQL, REST APIs</li>
            <li><strong>Tools:</strong> GitHub, Visual Studio Code, Jupyter Notebook</li>
            <li><strong>OS:</strong> Linux, Windows</li>
            {skills_list_items}
            </ul>
            </section>"""
    return skills