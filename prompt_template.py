# system_template_text = """
# Create a detailed and engaging case study on the topic of 'Basic Principles of Accrual Basis Accounting' (Chapter 1 of Financial Accounting). The case study should be designed specifically for the user with the following details:
#
# User's name:
# Major:
# Career objective:
# In the case study:
#
# Present a fictional scenario involving a company implementing accrual basis accounting for the first time.
# Connect the company's challenges and solutions to concepts relevant to the user's interests.
# Provide thought-provoking questions to engage the user, encouraging them to apply their expertise and career aspirations to the case.
# Use professional yet accessible language that aligns with user’s academic level.
# Ensure the case study is practical, relatable, and incorporates examples that align with user's interest.
# {parser_instructions}
# """
#
# user_template_text = "{theme}"

system_template_text = """Create a case study for an accounting course focused on Chapter 1: Accrual Basis Accounting. The case study should be educational and practical, tailored to a user who is studying [Major] and aims to become [Career Objective]. Use the user's name, [Name], as the main character in the scenario to make it relatable.

The case study should:

Introduce a scenario where [Name] is working as a junior accountant.
Highlight a situation where they need to apply accrual basis accounting principles to record revenue and expenses.
Include a practical challenge, such as distinguishing between accrual and cash basis accounting, and show how the accrual basis provides more accurate financial reporting.
Provide calculations or examples of adjusting entries for prepaid expenses, accrued expenses, and revenue recognition.
End with a question prompting the user to reflect on the benefits and challenges of accrual basis accounting.
Ensure the content is clear, concise, and suitable for accounting students at an introductory level. Avoid overly technical jargon, but include accurate accounting concepts and calculations.
{parser_instructions}
"""

user_template_text = "{theme}"
