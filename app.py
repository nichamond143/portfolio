from flask import Flask, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", main_id="full-screen")


@app.route("/about")
def about():

    educations = [
        {
            "images": [
                {
                    "path": "static/images/speech-comp.png",
                    "alt": "National Speech Competition",
                },
                {
                    "path": "static/images/royal-assessment.jpg",
                    "alt": "Royal Student Assessment",
                },
                {
                    "path": "static/images/student-council.jpg",
                    "alt": "Student Council Presentation",
                },
            ],
            "image_path": "static/images/speech-comp.png",
            "image_alt": "Mond giving a speech at a competition",
            "logo_path": "static/logos/bn.png",
            "logo_alt": "Bumnetnarong Wittayakhom School Logo",
            "name": "Bumnetnarong Wittayakhom School ",
            "year": "2017-2021",
            "program": "IEP/MEP Program",
            "gpax": "3.76",
            "accomplishments": [
                "Two-time national impromptu English speech winner Year 2018 and 2019",
                "Parcipant of the Regional Student Assessment to Recieve the Royal Student Award Year 2020",
                "President of IEP/MEP Student Council",
            ],
        },
        {
            "images": [
                {
                    "path": "static/images/dean-honor-roll.jpg",
                    "alt": "Received Dean's Honor Roll",
                },
                {
                    "path": "static/images/ECTI-DAMT.jpg",
                    "alt": "ECTI-DAMT NCON Event",
                },
                {
                    "path": "static/images/hackathon-1.jpg",
                    "alt": "Teaching at MFU Hackathon 2024",
                },
            ],
            "logo_path": "static/logos/mfu.png",
            "logo_alt": "MFU Logo",
            "name": "Mae Fah Luang University ",
            "year": "2021-Present",
            "program": "Bachelor of Engineering in Software Engineering",
            "gpax": "3.97",
            "accomplishments": [
                "On the Dean's Honor Roll in 2022 and received the Certificate of Excellence for Academic Performance in 2021",
                "Presented paper titled Elderly Motion Tracking System with AI-Enabled Edge Computing at the ECTI DAMT & NCON 2023 International Conference in Chiang Mai, Thailand",
                "Taught a front-end course using Nuxt.js 3 and Vuetify 3 at the MFU Hackathon 2024",
            ],
        },
    ]

    skills = [
        {"name": "HTML", "path": "static/logos/HTML5-logo.png"},
        {"name": "CSS", "path": "static/logos/CSS3-logo.png"},
        {"name": "JavaScript", "path": "static/logos/javascript-logo.png"},
        {"name": "Bootstrap", "path": "static/logos/bootstrap-logo.png"},
        {"name": "Vue.js", "path": "static/logos/vue-logo.png"},
        {"name": "Nuxt.js", "path": "static/logos/nuxt-logo.png"},
        {"name": "Vuetify", "path": "static/logos/vuetify-logo.png"},
        {"name": "Dart", "path": "static/logos/dart-logo.png"},
        {"name": "Flutter", "path": "static/logos/flutter-logo.png"},
        {"name": "Java", "path": "static/logos/java-logo.png"},
        {"name": "Python", "path": "static/logos/python-logo.png"},
        {"name": "Scikit-learn", "path": "static/logos/scikit-learn-logo.png"},
        {"name": "YOLO", "path": "static/logos/YOLO-logo.png"},
        {"name": "SQL", "path": "static/logos/sql-logo.png"},
        {"name": "Firebase", "path": "static/logos/firebase-logo.png"},
        {"name": "Git", "path": "static/logos/git-logo.png"},
        {"name": "Figma", "path": "static/logos/figma-logo.png"},
        {"name": "Jira", "path": "static/logos/jira-logo.png"},
        {"name": "VSCODE", "path": "static/logos/vs-code-logo.png"},
        {"name": "Eclipse", "path": "static/logos/eclipse-logo.png"},
        {"name": "Jupyter", "path": "static/logos/jupyter_logo.png"},
    ]

    return render_template(
        "about.html", skills=skills, educations=educations, main_id="scroll-screen"
    )


@app.route("/projects")
def project():
    return render_template("projects.html", main_id="scroll-screen")


@app.route("/contacts")
def contact():
    return render_template("contacts.html", main_id="full-screen")
