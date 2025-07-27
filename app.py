from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Gmail Cleaner",
        "desc": "AI-powered tool to organize and delete unwanted Gmail emails.",
        "tech": ["Python", "FastAPI", "OAuth2", "ML"],
        "img": "gmail.png",
        "link": "#"
    },
    {
        "title": "WhatsApp Media Cleaner",
        "desc": "App to remove duplicate WhatsApp sent images already present in gallery.",
        "tech": ["Flutter", "Image Hashing", "Dart"],
        "img": "whatsapp.png",
        "link": "#"
    },
    {
        "title": "GradeEmailer",
        "desc": "Send personalized grade emails using name and roll_no from CSV.",
        "tech": ["Flask", "CSV", "Email"],
        "img": "gradeemailer.png",
        "link": "#"
    },
    {
        "title": "DataValidationTool",
        "desc": "Validates data in raw files against predefined rules",
        "tech": ["Flask", "XML", "MongoDB"],
        "img": "dataValidation.png",
        "link": "#"
    },
    {
        "title": "DocumentWriter",
        "desc": "Creates documents with relevant extracted information from raw files ",
        "tech": ["Flask", "XML", "MongoDB", "AWS SQS", "AWS S3"],
        "img": "documentWriter.png",
        "link": "#"
    }
]

skills = ["Python", "Flask", "FastAPI", "OAuth2", "Machine Learning"]

@app.route("/")
def home():
    return render_template("index.html", name="Rashmi", role="Tool Developer",
                            tagline="Cleaning email, chat & grading automation", skills=skills, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
