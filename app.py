from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Gmail Cleaner",
        "desc": "AI-powered mobile app to organize and delete unwanted Gmail emails based on existing and AI generated categories such as promotions/social/ecommerce etc and sender information",
        "tech": ["Python", "FastAPI", "OAuth2", "ML"],
        "img": "gmail.png",
        "link": "#"
    },
    {
        "title": "WhatsApp Media Cleaner",
        "desc": "Mobile App to remove duplicate WhatsApp sent media already present in gallery and unwanted whatsapp media from phone storage",
        "tech": ["Flutter", "Image Hashing", "Dart"],
        "img": "whatsapp.png",
        "link": "#"
    },
    {
        "title": "LibrarySpaceMax",
        "desc": "Mobile app for students to reserve seats in library to save time and effort of manually checking for space. Qr code based seat booking and real time space availability in Library with seat layout UI (In Progress)",
        "tech": ["Flask", "Flutter", "QR Code", "Dart", "OAuth2"],
        "img": "libApp.png",
        "link": "#"
    },
    {
        "title": "DataViz",
        "desc": "Web app to create custom visualizations, preprocess and analyze data, build ML models (In Progress)",
        "tech": ["Flask", "CSV/Excel","Dash", "Data Visualization", "ML Models", "Data Analysis" ],
        "img": "dataviz.png",
        "link": "#"
    },
    # {
    #     "title": "DataValidationTool"
    #     "desc": "Validates data in raw files against predefined rules",
    #     "tech": ["Flask", "XML", "MongoDB"],
    #     "img": "dataValidation.png",
    #     "link": "#"
    # },
    # {
    #     "title": "DocumentWriter",
    #     "desc": "Creates documents with relevant extracted information from raw files ",
    #     "tech": ["Flask", "XML", "MongoDB", "AWS SQS", "AWS S3"],
    #     "img": "documentWriter.png",
    #     "link": "#"
    # }
]

skills = ["Python", "Flask", "FastAPI", "OAuth2", "Machine Learning"]

@app.route("/")
def home():
    return render_template("index.html", name="Rashmi", role="Tool Developer",
                            tagline="Cleaning email, chat & grading automation", skills=skills, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
