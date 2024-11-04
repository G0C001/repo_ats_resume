def style():
    style = """
        <!DOCTYPE html>
        <html lang="en">

        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <title>Resume - D. Gokul Vasanth</title>
            <style>
              @page {
                size: A4;
                margin: 0mm;
              }

              body {
                font-family: Arial, sans-serif;
                font-size: 14px;
                line-height: 1.4;
                color: #333;
                margin: 0;
                padding: 0;
              }

              .container {
                width: 100%;
                max-width: 190mm; /* A4 width minus margins */
                padding: 20px;
                margin: 0 auto;
                background-color: #fff;
                box-sizing: border-box;
              }

              h1, h2, h3 {
                margin-bottom: 10px;
                color: #2E86C1;
              }

              h1 {
                font-size: 24px;
              }

              h2 {
                font-size: 18px;
                margin-top: 20px;
                border-bottom: 2px solid #2E86C1;
              }

              h3 {
                font-size: 14px;
              }

              p, ul {
                margin: 0 0 10px 0;
              }

              ul {
                list-style: disc;
                padding-left: 20px;
              }

              .section {
                margin-bottom: 20px;
              }

              /* Styling for personal details */
              .personal-details {
                display: flex;
                justify-content: space-between;
                flex-wrap: wrap;
              }

              .personal-details div {
                flex: 1;
                min-width: 50%;
              }

              /* Contact information */
              .contact-info {
                margin-top: 5px;
                font-size: 11px;
              }

              /* Skills and other list-based sections */
              .skills, .languages {
                display: flex;
                flex-wrap: wrap;
              }

              .skills li, .languages li {
                width: 48%;
                margin-bottom: 10px;
              }

              .education, .experience, .projects {
                margin-bottom: 15px;
              }

              /* Ensuring no content overflow */
              .container, .section {
                overflow: hidden;
              }

              /* Styling for A4 size */
              @media print {
                body {
                  width: 210mm;
                  height: 297mm;
                }
              }
            </style>
          </head>"""
    return style