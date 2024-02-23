def get_evaluation_data():
    """
    Retrieve evaluation questions and answers for contract evaluation.

    Returns:
    tuple: A tuple containing two lists:
           - eval_questions: A list of evaluation questions.
           - eval_answers: A list of corresponding evaluation answers.
    """
    eval_questions = [
        "Who are the parties to the Agreement and what are their defined names?",
        "What is the termination notice?",
        "What are the payments to the Advisor under the Agreement?",
        "Can the Agreement or any of its obligations be assigned?",
        "Who owns the IP?",
        "Is there a non-compete obligation to the Advisor?",
        "Can the Advisor charge for meal time?",
        "In which street does the Advisor live?",
        "Is the Advisor entitled to social benefits?",
        "What happens if the Advisor claims compensation based on employment relationship with the Company?"
        "Under what circumstances and to what extent the Sellers are responsible for a breach of representations and warranties?",
        "Would the Sellers be responsible if after the closing it is determined that there were inaccuracies in the representation provided by them where such inaccuracies are the result of the Sellers’ gross negligence?",
        "How much is the escrow amount?",
        "Is escrow amount greater than the Retention Amount?",
        "What is the purpose of the escrow?",
        "May the Escrow Amount serve as a recourse for the Buyer in case of breach of representations by the Company?",
        "Are there any conditions to the closing?",
        "Are Change of Control Payments considered a Seller Transaction Expense?",
        "Would the aggregate amount payable by the Buyer to the Sellers be affected if it is determined that the actual Closing Debt Amount is greater than the estimated Closing Debut Amount?",
        "Does the Buyer need to pay the Employees Closing Bonus Amount directly to the Company’s employees?",
        "Does any of the Sellers provide a representation with respect to any Tax matters related to the Company?",
        "Is any of the Sellers bound by a non-competition covenant after the Closing?",
        "Whose consent is required for the assignment of the Agreement by the Buyer?",
        "Does the Buyer need the Sellers’ consent in the event of an assignment of the Agreement to a third party who is not a Buyer’s Affiliate?"
    ]
    eval_answers = [
        "Cloud Investments Ltd. (“Company”) and Jack Robinson (“Advisor”)",
        "According to section 4:14 days for convenience by both parties. The Company may terminate without notice if the Advisor refuses or cannot perform the Services or is in breach of any provision of this Agreement.",
        "According to section 6: 1. Fees of $9 per hour up to a monthly limit of $1,500, 2. Workspace expense of $100 per month, 3. Other reasonable and actual expenses if approved by the company in writing and in advance.",
        "1. Under section 1.1 the Advisor can’t assign any of his obligations without the prior written consent of the Company, 2. Under section 9 the Advisor may not assign the Agreement and the Company may assign it, 3 Under section 9 of the Undertaking the Company may assign the Undertaking.",
        "According to section 4 of the Undertaking (Appendix A), Any Work Product, upon creation, shall be fully and exclusively owned by the Company.",
        "Yes. During the term of engagement with the Company and for a period of 12 months thereafter.",
        "No. See Section 6.1, Billable Hour doesn’t include meals or travel time.",
        "1 Rabin st, Tel Aviv, Israel",
        "No. According to section 8 of the Agreement, the Advisor is an independent consultant and shall not be entitled to any overtime pay, insurance, paid vacation, severance payments or similar fringe or employment benefits from the Company.",
        "If the Advisor is determined to be an employee of the Company by a governmental authority, payments to the Advisor will be retroactively reduced so that 60% constitutes salary payments and 40% constitutes payment for statutory rights and benefits. The Company may offset any amounts due to the Advisor from any amounts payable under the Agreement. The Advisor must indemnify the Company for any losses or expenses incurred if an employer/employee relationship is determined to exist."
        "Except in the case of fraud, the Sellers have no liability for breach of representations and warranties (See section 10.01)",
        "No.",
        "The escrow amount is equal to $1,000,000.",
        "No.",
        "To serve as a recourse of the Buyer in case of post-closing adjustments of the purchase price. (See section 2.07(e)).",
        "No.",
        "No, as the signing and closing are simultaneous.",
        "Yes. (See defining of Sellers Transaction Expenses).",
        "Yes (See Section 2.07).",
        "No. (See Section 2.10).",
        "No. Only the Company provides such a representation.",
        "No.",
        "If the assignment is to an Affiliate or purchaser of all of the Buyer’s assets, no consent is required. Otherwise, the consent of the Company and the Seller Representative is required.",
        "No. If the assignment is not part of a sale of all or substantially all of the Buyer’s assets, the assignment requires the consent of the Company and the Seller’s Representative."
    ]
    
    return eval_questions, eval_answers