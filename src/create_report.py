
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

# ==========================================
# 1. EDIT YOUR PERSONAL DETAILS HERE
# ==========================================

STUDENT_NAME = "BHUMIKA SRIVASTAVA"
COURSE = "Bachelor of Computer Applications (BCA)"
COLLEGE = "NETAJI SUBHAS UNIVERSITY"
INTERNSHIP = "InternSpark"
TASK = "Task 2 - Loan Approval Prediction"

GITHUB_LINK = "Paste Your GitHub Repository Link Here"
NOTEBOOK_LINK = "Paste Your Jupyter Notebook Link Here"

# Enter your actual results from your notebook.
# Do not leave these as placeholders in your final report.

MODEL_RESULTS = [
    ["Model", "Precision", "Recall", "F1-score", "ROC-AUC"],
    ["Logistic Regression", "Enter", "Enter", "Enter", "Enter"],
    ["Decision Tree", "Enter", "Enter", "Enter", "Enter"],
    ["Random Forest", "Enter", "Enter", "Enter", "Enter"],
]

BEST_MODEL = "Enter the best-performing model"
BEST_THRESHOLD = "Enter the selected threshold"

# ==========================================
# 2. FILE LOCATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

PDF_PATH = OUTPUT_DIR / "Task-2-Loan-Approval-Report.pdf"

# ==========================================
# 3. DOCUMENT DESIGN
# ==========================================

doc = SimpleDocTemplate(
    str(PDF_PATH),
    pagesize=A4,
    rightMargin=50,
    leftMargin=50,
    topMargin=50,
    bottomMargin=50
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "ReportTitle",
    parent=styles["Title"],
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#17365D"),
    spaceAfter=18
)

subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontSize=12,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#555555"),
    spaceAfter=10
)

heading_style = ParagraphStyle(
    "SectionHeading",
    parent=styles["Heading2"],
    fontSize=14,
    leading=18,
    textColor=colors.HexColor("#17365D"),
    spaceBefore=13,
    spaceAfter=8
)

body_style = ParagraphStyle(
    "ReportBody",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=9
)

story = []

# ==========================================
# 4. COVER PAGE
# ==========================================

story.append(Spacer(1, 65))

story.append(Paragraph(
    "LOAN APPROVAL<br/>PREDICTION",
    title_style
))

story.append(Paragraph(
    "Machine Learning Internship Project Report",
    subtitle_style
))

story.append(Spacer(1, 35))

cover_data = [
    ["SUBMISSION DETAILS", ""],
    ["Student Name", STUDENT_NAME],
    ["Course", COURSE],
    ["College", COLLEGE],
    ["Internship Organization", INTERNSHIP],
    ["Task Number", "Task 2"],
    ["Project Title", "Loan Approval Prediction"],
]

cover_table = Table(
    cover_data,
    colWidths=[2.1 * inch, 3.8 * inch]
)

cover_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0),
     colors.HexColor("#17365D")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("SPAN", (0, 0), (-1, 0)),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
    ("BACKGROUND", (0, 1), (0, -1),
     colors.HexColor("#EAF1F8")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 11),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
]))

story.append(cover_table)
story.append(Spacer(1, 45))

story.append(Paragraph(
    "Submitted as part of the internship task requirements.",
    subtitle_style
))

story.append(PageBreak())

# ==========================================
# 5. EXECUTIVE SUMMARY
# ==========================================

story.append(Paragraph(
    "EXECUTIVE SUMMARY",
    title_style
))

story.append(Paragraph(
    "This project focuses on developing a machine learning model "
    "to predict loan approval decisions based on applicant "
    "information. The purpose is to understand how data-driven "
    "techniques can support financial institutions in evaluating "
    "loan applications.",
    body_style
))

story.append(Paragraph(
    "The project includes data cleaning, missing-value treatment, "
    "categorical encoding, feature scaling and class imbalance "
    "handling. Multiple classification algorithms are compared "
    "using standard evaluation metrics.",
    body_style
))

story.append(Paragraph(
    "The results help identify a suitable model and demonstrate "
    "how prediction thresholds can influence financial "
    "decision-making.",
    body_style
))

# ==========================================
# 6. INTRODUCTION
# ==========================================

story.append(Paragraph("1. Introduction", heading_style))

story.append(Paragraph(
    "Loan approval is an important activity for banks and financial "
    "institutions. Before approving a loan, lenders evaluate "
    "information such as an applicant's income, employment status, "
    "credit history and other financial details.",
    body_style
))

story.append(Paragraph(
    "Machine learning can analyse historical application data "
    "and identify patterns associated with loan approval. "
    "This project applies supervised machine learning to predict "
    "loan approval outcomes.",
    body_style
))

# ==========================================
# 7. PROJECT OBJECTIVES
# ==========================================

story.append(Paragraph("2. Project Objectives", heading_style))

objectives = [
    "Understand and analyse the loan approval dataset.",
    "Identify and handle missing values and duplicate records.",
    "Convert categorical information into numerical features.",
    "Scale numerical features where required.",
    "Address class imbalance using SMOTE.",
    "Train and compare different classification algorithms.",
    "Evaluate model performance using appropriate metrics.",
    "Interpret results from a business perspective."
]

for item in objectives:
    story.append(Paragraph("&#8226; " + item, body_style))

# ==========================================
# 8. DATASET DESCRIPTION
# ==========================================

story.append(Paragraph("3. Dataset Description", heading_style))

story.append(Paragraph(
    "The dataset used in this project is the Loan Approval "
    "Prediction dataset available on Kaggle. It contains "
    "information about loan applicants and their application "
    "outcomes.",
    body_style
))

story.append(Paragraph(
    "Important features include applicant income, co-applicant "
    "income, education, employment status, loan amount, credit "
    "history and property area. The target variable represents "
    "whether the loan was approved or rejected.",
    body_style
))

story.append(Paragraph(
    "Dataset source: "
    "<link href='https://www.kaggle.com/datasets/"
    "bhanupratapbiswas/loan-approval-prediction-case-study' "
    "color='blue'>"
    "Kaggle - Loan Approval Prediction</link>",
    body_style
))

# ==========================================
# 9. DATA PREPROCESSING
# ==========================================

story.append(Paragraph("4. Data Preprocessing", heading_style))

story.append(Paragraph(
    "Data preprocessing prepares the raw dataset for machine "
    "learning. Missing numerical values were handled using "
    "median imputation, while missing categorical values were "
    "replaced using the most frequent category.",
    body_style
))

story.append(Paragraph(
    "Categorical features were transformed using One-Hot Encoding. "
    "Numerical features were scaled using StandardScaler. "
    "Duplicate records and unnecessary identifier columns "
    "were also handled.",
    body_style
))

# ==========================================
# 10. CLASS IMBALANCE
# ==========================================

story.append(Paragraph(
    "5. Handling Class Imbalance",
    heading_style
))

story.append(Paragraph(
    "Class imbalance occurs when one target category has "
    "significantly more records than another. This can affect "
    "a model's ability to recognise the minority category.",
    body_style
))

story.append(Paragraph(
    "SMOTE (Synthetic Minority Over-sampling Technique) was "
    "used to generate synthetic examples of the minority class "
    "in the training data. This helps the model learn from "
    "both categories. SMOTE was applied within the training "
    "pipeline to prevent data leakage.",
    body_style
))

# ==========================================
# 11. MODELS
# ==========================================

story.append(Paragraph(
    "6. Machine Learning Models",
    heading_style
))

story.append(Paragraph(
    "<b>Logistic Regression:</b> A classification algorithm "
    "that estimates the probability of a loan approval outcome. "
    "It provides a simple and interpretable baseline.",
    body_style
))

story.append(Paragraph(
    "<b>Decision Tree:</b> A model that makes predictions "
    "through a series of feature-based decisions. It can "
    "capture non-linear relationships.",
    body_style
))

story.append(Paragraph(
    "<b>Random Forest:</b> An ensemble learning algorithm "
    "that combines multiple decision trees to produce "
    "predictions. It can provide more stable results than "
    "a single decision tree.",
    body_style
))

# ==========================================
# 12. MODEL EVALUATION
# ==========================================

story.append(Paragraph(
    "7. Model Evaluation and Comparison",
    heading_style
))

story.append(Paragraph(
    "The models were evaluated using Precision, Recall, "
    "F1-score and ROC-AUC. These metrics provide different "
    "ways to understand the quality of classification "
    "predictions.",
    body_style
))

story.append(Paragraph(
    "<b>Precision:</b> Measures the proportion of predicted "
    "positive cases that are actually positive.",
    body_style
))

story.append(Paragraph(
    "<b>Recall:</b> Measures the proportion of actual positive "
    "cases correctly identified by the model.",
    body_style
))

story.append(Paragraph(
    "<b>F1-score:</b> Combines precision and recall into "
    "a single measure.",
    body_style
))

story.append(Paragraph(
    "<b>ROC-AUC:</b> Measures how well a model distinguishes "
    "between the two target classes across different thresholds.",
    body_style
))

results_table = Table(
    MODEL_RESULTS,
    colWidths=[1.65 * inch, 0.9 * inch, 0.9 * inch,
               0.9 * inch, 0.9 * inch],
    repeatRows=1
)

results_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0),
     colors.HexColor("#17365D")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [colors.white, colors.HexColor("#EAF1F8")]),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))

story.append(results_table)

story.append(Spacer(1, 10))

story.append(Paragraph(
    "Best-performing model: " + BEST_MODEL,
    body_style
))

# ==========================================
# 13. THRESHOLD SELECTION
# ==========================================

story.append(Paragraph(
    "8. Classification Threshold",
    heading_style
))

story.append(Paragraph(
    "A classification threshold determines how predicted "
    "probabilities are converted into final class predictions. "
    "A default threshold of 0.50 can be compared with a threshold "
    "selected using validation data.",
    body_style
))

story.append(Paragraph(
    "Selected threshold: " + BEST_THRESHOLD,
    body_style
))

story.append(Paragraph(
    "The final threshold should balance the risks of incorrectly "
    "approving and incorrectly rejecting applications. It should "
    "also reflect the institution's lending policy.",
    body_style
))

# ==========================================
# 14. BUSINESS INTERPRETATION
# ==========================================

story.append(Paragraph(
    "9. Business Interpretation",
    heading_style
))

story.append(Paragraph(
    "The model can support the initial screening of loan "
    "applications. However, incorrect predictions can have "
    "financial and customer-related consequences.",
    body_style
))

story.append(Paragraph(
    "A false approval may expose a lender to repayment risk, "
    "while a false rejection may prevent a creditworthy applicant "
    "from receiving a loan. Therefore, both precision and recall "
    "are important when evaluating the model.",
    body_style
))

# ==========================================
# 15. DEPLOYMENT RECOMMENDATIONS
# ==========================================

story.append(Paragraph(
    "10. Deployment Recommendations",
    heading_style
))

story.append(Paragraph(
    "The model should initially be used as a decision-support "
    "system rather than an automatic loan approval authority. "
    "Before deployment, it should be tested on recent data, "
    "checked for unfair bias, monitored for performance changes "
    "and reviewed by qualified human decision-makers.",
    body_style
))

# ==========================================
# 16. CONCLUSION
# ==========================================

story.append(Paragraph("11. Conclusion", heading_style))

story.append(Paragraph(
    "This project demonstrates the application of supervised "
    "machine learning to loan approval prediction. It covers "
    "data preprocessing, class imbalance handling, model "
    "comparison and performance evaluation.",
    body_style
))

story.append(Paragraph(
    "The project highlights how machine learning can support "
    "financial decision-making while also showing the importance "
    "of model evaluation, threshold selection, fairness and "
    "human oversight.",
    body_style
))

# ==========================================
# 17. PROJECT LINKS
# ==========================================

story.append(Paragraph(
    "12. Project Links and References",
    heading_style
))

story.append(Paragraph(
    "GitHub Repository: "
    "<link href='" + GITHUB_LINK + "' color='blue'>"
    "Open GitHub Project</link>",
    body_style
))

story.append(Paragraph(
    "Jupyter Notebook: "
    "<link href='" + NOTEBOOK_LINK + "' color='blue'>"
    "Open Project Notebook</link>",
    body_style
))

story.append(Paragraph(
    "Dataset: "
    "<link href='https://www.kaggle.com/datasets/"
    "bhanupratapbiswas/loan-approval-prediction-case-study' "
    "color='blue'>Open Kaggle Dataset</link>",
    body_style
))

# ==========================================
# 18. FOOTER
# ==========================================

def add_footer(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)

    canvas.drawString(
        50, 25,
        "InternSpark | Loan Approval Prediction"
    )

    canvas.drawRightString(
        A4[0] - 50, 25,
        "Page " + str(document.page)
    )

    canvas.restoreState()


# ==========================================
# 19. GENERATE PDF
# ==========================================

doc.build(
    story,
    onFirstPage=add_footer,
    onLaterPages=add_footer
)

print("\nPDF generated successfully!")
print("Location:", PDF_PATH)
