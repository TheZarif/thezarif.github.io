"""Build the downloadable academic CV at files/zarifmasud_cv.pdf.

Run with reportlab available on PYTHONPATH, for example:
    PYTHONPATH=/tmp/zarif-cv-pdf-deps python3 scripts/build_cv_pdf.py
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "files" / "zarifmasud_cv.pdf"
NAVY = colors.HexColor("#21364b")
GREY = colors.HexColor("#536273")


def style(name, **kwargs):
    options = {"fontName": "Helvetica", "textColor": NAVY}
    options.update(kwargs)
    return ParagraphStyle(name, **options)


NAME = style("name", fontName="Helvetica-Bold", fontSize=19, leading=22, alignment=TA_CENTER)
SUBTITLE = style("subtitle", fontSize=9.2, leading=12, alignment=TA_CENTER)
CONTACT = style("contact", fontSize=8.2, leading=11, alignment=TA_CENTER)
SECTION = style("section", fontName="Helvetica-Bold", fontSize=10.5, leading=13, spaceBefore=11, spaceAfter=4)
BODY = style("body", fontSize=8.8, leading=11.6, alignment=TA_LEFT)
SMALL = style("small", fontSize=8.3, leading=10.9)
ITEM_TITLE = style("item-title", fontName="Helvetica-Bold", fontSize=8.8, leading=11.4)
DATE = style("date", fontSize=8.2, leading=11, alignment=2)


def paragraph(text, paragraph_style=BODY):
    return Paragraph(text, paragraph_style)


def heading(title):
    return [paragraph(title, SECTION), HRFlowable(width="100%", thickness=0.6, color=GREY), Spacer(1, 4)]


def dated_entry(title, dates, detail, note=None):
    row = Table(
        [[paragraph(title, ITEM_TITLE), paragraph(dates, DATE)]],
        colWidths=[6.00 * inch, 1.20 * inch],
        hAlign="LEFT",
    )
    row.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    blocks = [row, paragraph(detail, SMALL)]
    if note:
        blocks.append(paragraph(note, SMALL))
    blocks.append(Spacer(1, 5))
    return KeepTogether(blocks)


def publication(title, date, authors, venue, link=None):
    title_line = f'<b>{title}</b>'
    if link:
        title_line = f'<link href="{link}" color="#1c587b">{title_line}</link>'
    blocks = [
        dated_entry(title_line, date, authors, venue),
    ]
    return blocks


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#cad2d9"))
    canvas.setLineWidth(0.5)
    canvas.line(0.65 * inch, 0.52 * inch, 7.85 * inch, 0.52 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(0.65 * inch, 0.36 * inch, "Zarif Masud | Curriculum Vitae")
    canvas.drawRightString(7.85 * inch, 0.36 * inch, str(doc.page))
    canvas.restoreState()


def main():
    document = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.53 * inch,
        bottomMargin=0.68 * inch,
        title="Zarif Masud - Curriculum Vitae",
        author="Zarif Masud",
    )
    story = [
        paragraph("Zarif Masud", NAME),
        Spacer(1, 2),
        paragraph("PhD Student in Information | Faculty of Information, University of Toronto", SUBTITLE),
        Spacer(1, 5),
        paragraph(
            'Toronto, Canada | <link href="mailto:zarif.masud@mail.utoronto.ca" color="#1c587b">zarif.masud@mail.utoronto.ca</link> | (416) 668 0689 | '
            '<link href="https://www.zarifmasud.net" color="#1c587b">zarifmasud.net</link>',
            CONTACT,
        ),
        paragraph(
            '<link href="https://www.linkedin.com/in/zarifmasud" color="#1c587b">linkedin.com/in/zarifmasud</link> | '
            '<link href="https://github.com/TheZarif" color="#1c587b">github.com/TheZarif</link>',
            CONTACT,
        ),
    ]

    story += heading("Research Interests")
    story += [paragraph("Responsible AI, algorithmic bias, information retrieval, migration studies, computational social science")]

    story += heading("Education")
    story += [
        dated_entry(
            "University of Toronto, Toronto, Canada",
            "Sep 2026 - Present",
            "PhD in Information, Faculty of Information",
            "Supervisors: Dr. Ebrahim Bagheri and Dr. Syed Ishtiaque Ahmed",
        ),
        dated_entry(
            "Toronto Metropolitan University, Toronto, Canada",
            "Sep 2023 - 2026",
            "Doctoral studies in Computer Engineering",
        ),
        dated_entry(
            "University of Waterloo, Waterloo, Canada",
            "Sep 2017 - Oct 2019",
            "MMath in Computer Science",
        ),
        dated_entry(
            "University of Dhaka, Dhaka, Bangladesh",
            "Jan 2012 - Feb 2016",
            "BSc in Software Engineering",
        ),
    ]

    story += heading("Experience")
    story += [
        dated_entry(
            "Researcher, BARTA - Remote, Dhaka, Bangladesh",
            "Jul 2022 - Present",
            "Mentor interdisciplinary teams on low-resource language processing and responsible AI projects.",
        ),
        dated_entry(
            "Software Engineer, Modern Data - Remote, Ontario, Canada",
            "Apr 2023 - Oct 2024",
            "Developed data engineering and analytics pipelines using Python, SQL, and AWS for enterprise clients.",
        ),
        dated_entry(
            "Software Development and Design Engineer, YuJa - Toronto, Canada",
            "Sep 2020 - Aug 2022",
            "Led the Himalayas project to reduce cloud storage costs for YuJa's Enterprise Video Platform by 60-70%.",
        ),
        dated_entry(
            "Associate Software Engineer, Kaz Software Ltd. - Dhaka, Bangladesh",
            "Jul 2016 - Jul 2017",
            "Built a full-stack information system for NGOs.",
        ),
    ]

    story += heading("Research Projects")
    story += [
        dated_entry(
            "Observatory on Immigration Discourses (IDIO), Bridging Divides",
            "Active",
            "Team member on an AI-assisted research observatory studying immigration discourse.",
            '<link href="https://www.torontomu.ca/bridging-divides/research/research-projects/citizenship-and-participation/observatory-on-immigration-discourses/" color="#1c587b">Project page</link>',
        ),
        dated_entry(
            "MS MARCO Immigration Narrative Bias",
            "2026",
            "Released data and reproducible analysis accompanying the ECIR 2026 paper.",
            '<link href="https://github.com/TheZarif/msmarco-bias" color="#1c587b">Research archive</link>',
        ),
        PageBreak(),
    ]

    story += heading("Publications")
    story += publication(
        "Emotional and Informational Trajectories of Immigrants: A Longitudinal Study of Reddit Communities",
        "2027",
        "Zarif Masud, Abhijit Paul, Naimul Khan, Syed Ishtiaque Ahmed, and Ebrahim Bagheri.",
        "Accepted for the International AAAI Conference on Web and Social Media (ICWSM 2027).",
    )
    story += publication(
        "The Role of Artificial Intelligence in Immigration: From Automation to Accountability",
        "2026",
        "Zarif Masud, Syed Ishtiaque Ahmed, and Ebrahim Bagheri.",
        "In Ana Beduschi (Ed.), <i>Handbook on Migration and Artificial Intelligence</i>. Edward Elgar Publishing.",
        "https://www.e-elgar.com/shop/usd/handbook-on-migration-and-artificial-intelligence-9781035331611.html",
    )
    story += publication(
        "How Information Retrieval Systems Construct and Amplify Immigration Narratives",
        "2026",
        "Zarif Masud, Abhijit Paul, Syed Ishtiaque Ahmed, and Ebrahim Bagheri.",
        "<i>Advances in Information Retrieval</i> (ECIR 2026), pp. 474-488. DOI: 10.1007/978-3-032-21324-2_36.",
        "https://doi.org/10.1007/978-3-032-21324-2_36",
    )
    story += publication(
        "Partisan Perspectives on AI and Immigration: An Analysis of Canadian Parliamentary Discourse (2014-2024)",
        "2025",
        "Eleyan Sawafta, Zarif Masud, Yasmeen Abu-Laban, Syed Ishtiaque Ahmed, Ebrahim Bagheri, and Geoffrey Rockwell.",
        "<i>Canadian Ethnic Studies</i>, 57(3), 49-75. DOI: 10.1353/ces.2025.a989105.",
        "https://doi.org/10.1353/ces.2025.a989105",
    )
    story += publication(
        "Development of a COVID-19-Related Anti-Asian Tweet Dataset: A Quantitative Study",
        "2023",
        "Mahdi Mokhberi, Zarif Masud, Shebuti Rayana, and Syed Ishtiaque Ahmed.",
        "<i>JMIR Formative Research</i>, 7(1), e40403. DOI: 10.2196/40403.",
        "https://doi.org/10.2196/40403",
    )
    story += publication(
        "SAFFRON: A Semi-Automated Framework for Software Requirements Prioritization",
        "2017",
        "S. A. Asif, Zarif Masud, R. Easmin, and A. Gias.",
        "<i>International Journal of Advanced Computer Science and Applications</i>, 8(12).",
        "https://thesai.org/Publications/ViewPaper?Volume=8&amp;Issue=12&amp;Code=IJACSA&amp;SerialNo=83",
    )

    story += heading("Workshop Papers")
    story += publication(
        "Exploring Cross-Lingual Knowledge Transfer via Transliteration-Based MLM Fine-Tuning for Critically Low-resource Chakma Language",
        "2025",
        "Adity Khisa, Nusrat Jahan Lia, Tasnim Mahfuz Nafis, Zarif Masud, Tanzir Pial, Shebuti Rayana, and Ahmedul Kabir.",
        "<i>Proceedings of the Second Workshop on Bangla Language Processing (BLP-2025)</i>, pp. 280-291. DOI: 10.18653/v1/2025.banglalp-1.23.",
        "https://aclanthology.org/2025.banglalp-1.23/",
    )
    story += publication(
        "Sinophobia on Twitter: Integrating Theory, Humans, and Machines",
        "2021",
        "Ahana Biswas, Zarif Masud, Shebuti Rayana, and Syed Ishtiaque Ahmed.",
        "ACM CSCW Workshop on Addressing Challenges and Opportunities in Online Extremism Research.",
    )

    story += heading("Preprints")
    story += publication(
        "State-of-the-Art Translation of Text-to-Gloss Using mBART: A Case Study of Bangla",
        "2025",
        "Sharif Mohammad Abdullah, Abhijit Paul, Zarif Masud, Shebuti Rayana, Abu Nayeem Md Touhidul Alam, Faisal Muhammad Shah, Md Shadab Iftikhar, Md Arid Hasan, and Ahmed Imtiaz Humayun.",
        "arXiv:2504.02293.",
        "https://arxiv.org/abs/2504.02293",
    )
    story += publication(
        "Where Journalism Silenced Voices: Indigenous Communities in Bangladeshi Media",
        "2025",
        "Abhijit Paul, Arifur Rahman Khisa, Zarif Masud, Sharif Mohammad Abdullah, Arif Kabir, and Shebuti Rayana.",
        "arXiv:2506.09771.",
        "https://arxiv.org/abs/2506.09771",
    )
    story += publication(
        "Stemming: The Evolution and Current State with a Focus on Bangla",
        "2025",
        "Abhijit Paul, Md Abu Farin, Zarif Masud, Sharif Mohammad Abdullah, Arif Kabir, and Saiful Islam.",
        "arXiv:2508.15711.",
        "https://arxiv.org/abs/2508.15711",
    )

    story += heading("Thesis")
    story += publication(
        "Switching GAN-Based Image Filters to Improve Perception for Autonomous Driving",
        "2019",
        "Zarif Masud.",
        "Master's thesis, University of Waterloo.",
        "https://uwspace.uwaterloo.ca/handle/10012/15099",
    )

    document.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    main()
