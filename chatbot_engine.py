def get_response(user_input):
    user_input = user_input.strip().lower()

    if "admission" in user_input:
        return "You can apply for admission online through our portal."

    elif "course" in user_input or "program" in user_input:
        return "We offer B.Tech, MCA, MBA, and BBA programs."

    elif "fee" in user_input or "fees" in user_input:
        return "The MCA fee is ₹90,000 per year. Other courses vary."

    elif "placement" in user_input or "job" in user_input:
        return "Our placement cell connects students with top companies like Infosys, TCS, and Wipro."

    elif "hostel" in user_input:
        return "Yes, separate hostel facilities are available for boys and girls."

    elif "scholarship" in user_input:
        return "Scholarships are available for merit and economically weaker students."

    elif "library" in user_input:
        return "Our central library offers thousands of books and digital resources."

    elif "canteen" in user_input or "food" in user_input:
        return "Our canteen provides affordable and hygienic food options."

    elif "transport" in user_input or "bus" in user_input:
        return "Yes, we offer transport facilities for day scholars."

    elif "contact" in user_input:
        return "You can reach us at +91-9999999999 or via our contact page."

    else:
        return "I'm not sure about that. Please contact the helpdesk at +91-9999999999."
