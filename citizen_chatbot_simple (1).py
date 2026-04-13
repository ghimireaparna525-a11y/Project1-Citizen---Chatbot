# ============================================================
# Citizen Support Chatbot – Simple Keyword Matcher
# Project 1
# Author: Aparna Ghimire
# Date: jan 2026
# Description: A simple Python chatbot that matches keywords
#              in a user's question and returns a helpful
#              answer about local council services.
# ============================================================

# --- Step 1: Define our knowledge base ---
# This is a list. Each item has:
#   "keywords" : words we look for in the user's question
#   "answer"   : what we reply if we find those words

knowledge_base = [
    {
        "keywords": ["bin", "rubbish", "collection", "missed", "waste"],
        "answer": "To report a missed bin collection, visit your local council website and fill in the missed collection form. Most councils aim to collect within 2 working days."
    },
    {
        "keywords": ["parking", "permit", "park"],
        "answer": "You can apply for a resident parking permit through your local council website. You will need proof of address and your vehicle registration number."
    },
    {
        "keywords": ["parking fine", "penalty", "pcn", "fine"],
        "answer": "Parking fines can be paid online through the link on your penalty charge notice. You usually get a 50% discount if you pay within 14 days."
    },
    {
        "keywords": ["vote", "register", "election", "voting"],
        "answer": "You can register to vote at gov.uk/register-to-vote. You will need your National Insurance number and your current address."
    },
    {
        "keywords": ["council tax", "tax"],
        "answer": "Council tax can be paid online through your local council website by direct debit, card or bank transfer. If you are on a low income you may qualify for a reduction."
    },
    {
        "keywords": ["pothole", "road", "highway", "pavement"],
        "answer": "You can report a pothole or road damage using the form on your local council website. Include the road name and a photo if possible."
    },
    {
        "keywords": ["housing", "house", "council house", "rent"],
        "answer": "Contact your local council housing department to join the housing register. You will be assessed on your circumstances and given a priority banding."
    },
    {
        "keywords": ["gp", "doctor", "nhs", "health", "prescription"],
        "answer": "You can find your nearest GP surgery at nhs.uk using the GP finder tool. Contact the surgery directly to register as a new patient."
    },
    {
        "keywords": ["school", "education", "admissions", "place"],
        "answer": "School place applications are made through your local council admissions team. Deadlines vary by school year group — check your council website."
    },
    {
        "keywords": ["passport", "renew", "document"],
        "answer": "UK passports are renewed through His Majesty's Passport Office at gov.uk/renew-adult-passport. Standard renewal currently takes up to 10 weeks."
    },
    {
        "keywords": ["benefit", "universal credit", "support", "money"],
        "answer": "Universal credit applications are made online at gov.uk/universal-credit. You will need your bank details and information about your housing costs."
    },
    {
        "keywords": ["recycle", "recycling", "centre", "tip"],
        "answer": "Your local council website has a list of recycling centres and their opening hours. You can search by postcode to find the nearest one."
    },
    {
        "keywords": ["street light", "light", "lamp", "lamppost"],
        "answer": "Report a broken street light to your local council using the online fault reporting form. Include the lamp post number if it is visible."
    },
    {
        "keywords": ["fly tip", "flytipping", "dumping", "litter"],
        "answer": "Report fly tipping to your local council using the online reporting form or by calling the council waste team."
    },
    {
        "keywords": ["planning", "permission", "extension", "build"],
        "answer": "For home alterations, apply through your local council planning portal at planningportal.co.uk. Minor changes may not need permission."
    },
]

# --- Step 2: Define the function that finds an answer ---
# A function is a reusable block of code.
# This one takes the user's question and searches for keywords.

def get_answer(user_question):
    # Convert the question to lowercase so "BIN" and "bin" both match
    question_lower = user_question.lower()

    # Loop through each item in our knowledge base
    for item in knowledge_base:
        # Loop through each keyword for this item
        for keyword in item["keywords"]:
            # Check if the keyword appears anywhere in the question
            if keyword in question_lower:
                # If yes, return the answer straight away
                return item["answer"]

    # If no keyword matched, return a default message
    return "I'm sorry, I don't have information on that. Please visit your local council website or call them directly for help."


# --- Step 3: Run the chatbot ---
# This is the main part that the user interacts with.

def run_chatbot():
    print("=" * 55)
    print("  Welcome to the Citizen Support Chatbot")
    print("  Type your question below, or type 'quit' to exit.")
    print("=" * 55)
    print()

    # Keep looping until the user types 'quit'
    while True:
        # Ask the user to type a question
        user_input = input("You: ")

        # If they type quit, stop the program
        if user_input.lower() == "quit":
            print("Chatbot: Thank you for using the Citizen Support Chatbot. Goodbye!")
            break

        # If they typed nothing, ask again
        if user_input.strip() == "":
            print("Chatbot: Please type a question and press Enter.")
            print()
            continue

        # Get the answer using our function
        answer = get_answer(user_input)

        # Print the chatbot's reply
        print(f"Chatbot: {answer}")
        print()


# --- Step 4: Start the program ---
# This line means: only run the chatbot if we run THIS file directly.
# It is a standard Python convention.

if __name__ == "__main__":
    run_chatbot()
