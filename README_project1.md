# Project 1 – Citizen Support Chatbot (Simple Keyword Matcher)

Portfolio Part b – Simple AI Chatbot 
Author: Aparna Ghimire 
Date: Jan 2026  
University: University of Bradford  


## What this project does

This is a simple Python chatbot that helps citizens find information about local council services. The user types a question, and the chatbot looks for keywords in the question to return a relevant answer.

For example:
- User types: *"How do I report a missed bin collection?"*
- Chatbot replies: *"To report a missed bin collection, visit your local council website..."*

This project is directly linked to my group project, which is building a conversational AI agent for citizen support. This simple version helped me understand the basic logic behind how a chatbot works before working with more advanced AI tools.

---

## How to run it

You need Python installed on your computer. Then:

1. Download the file `citizen_chatbot_simple.py`
2. Open a terminal or command prompt
3. Navigate to the folder where you saved the file
4. Type: `python citizen_chatbot_simple.py`
5. Type your question and press Enter

To stop the chatbot, type `quit` and press Enter.

---

## Example conversation

```
=======================================================
  Welcome to the Citizen Support Chatbot
  Type your question below, or type 'quit' to exit.
=======================================================

You: how do I report a pothole?
Chatbot: You can report a pothole or road damage using the form on your local council website. Include the road name and a photo if possible.

You: I need help with council tax
Chatbot: Council tax can be paid online through your local council website by direct debit, card or bank transfer. If you are on a low income you may qualify for a reduction.

You: quit
Chatbot: Thank you for using the Citizen Support Chatbot. Goodbye!
```

---

## Topics the chatbot can answer

- Bin collection and waste
- Parking permits and fines
- Voting and elections
- Council tax
- Potholes and road issues
- Council housing
- GP and NHS services
- Schools and admissions
- Passports and documents
- Benefits and universal credit
- Recycling centres
- Street lights
- Fly tipping
- Planning permission

---

## What I learnt from this project

Before building this I did not know how chatbots worked at a basic level. I assumed they were very complicated. Building this from scratch taught me that a simple chatbot is essentially a matching system — it looks for words it recognises and returns a pre-written answer.

I also learnt:
- How Python lists and dictionaries work (the knowledge base)
- How to write and call a function
- How to use a while loop to keep a program running
- Why converting text to lowercase matters (so "BIN" and "bin" both match)

The limitation of this approach is that it only works if the user uses words that are already in the keyword list. If someone asks in a completely different way, the bot will not understand. This is why more advanced AI uses machine learning rather than keyword matching — which I explore in Project 2.

---

## Files in this repository

| File | Description |
|---|---|
| `citizen_chatbot_simple.py` | The main Python chatbot script |
| `README.md` | This file — explains the project |

---

## Connection to group project

This project is the starting point of a three-part progression:

1. **This project (simple):** Keyword-based chatbot — no AI library, just Python logic
2. **Project 2 (semi-complex):** Using an NLP library to analyse citizen feedback automatically
3. **Project 3 (complex):** Using a real AI API to generate answers to any citizen question

All three projects relate to our group project building a conversational AI agent for citizen support services.
