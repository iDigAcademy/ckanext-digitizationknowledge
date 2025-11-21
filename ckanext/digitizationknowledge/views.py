from flask import Blueprint, render_template


digitizationknowledge = Blueprint(
    "digitizationknowledge", __name__)


#def page():
#    return "Hello, digitizationknowledge!"


#digitizationknowledge.add_url_rule(
#    "/digitizationknowledge/page", view_func=page)


# Define page for Terms of Use

def terms_of_use():
    "Render the Terms of use page."
    return render_template('digitizationknowledge/terms_of_use.html')

digitizationknowledge.add_url_rule(
    "/terms-of-use", view_func=terms_of_use
) 

# Define page for privacy policy

def privacy_policy():
    "Render the privacy policy page."
    return render_template('digitizationknowledge/privacy_policy.html')

digitizationknowledge.add_url_rule(
    "/privacy-policy", view_func=privacy_policy
)

def get_blueprints():
    return [digitizationknowledge]
