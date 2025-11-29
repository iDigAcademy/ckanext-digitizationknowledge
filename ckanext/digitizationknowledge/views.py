from flask import Blueprint, render_template, jsonify

import ckan.plugins.toolkit as toolkit
import ckan.model as model


digitizationknowledge = Blueprint(
    "digitizationknowledge", __name__)


#def page():
#    return "Hello, digitizationknowledge!"


#digitizationknowledge.add_url_rule(
#    "/digitizationknowledge/page", view_func=page)


# =============================================================================
# Terms of Use and Privacy Policy
# =============================================================================

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

# =============================================================================
# Group Add Feature - HTMX Routes
# =============================================================================

def group_add_list_groups():
    """
    GET /group-add/groups
    
    Returns a JSON list of groups the current user can add datasets to.
    Used to populate the group dropdown in the search page.
    """
    # Check if user is logged in
    if not toolkit.current_user.is_authenticated:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    context = {
        'user': toolkit.current_user.name,
    }
    
    try:
        # Get groups the user can manage (add datasets to)
        groups = toolkit.get_action('group_list_authz')(context, {})
        
        # Simplify the response - only send what the frontend needs
        groups_simple = [
            {
                'id': g['id'],
                'name': g['name'],
                'display_name': g.get('display_name') or g.get('title') or g['name']
            }
            for g in groups
        ]
        
        return jsonify({'success': True, 'groups': groups_simple})
        
    except toolkit.NotAuthorized:
        return jsonify({'success': False, 'error': 'Not authorized'}), 403


def group_add_dataset():
    """
    POST /group-add/add
    
    Adds a dataset to a group. Expects form data:
    - dataset_id: The ID or name of the dataset
    - group_id: The ID or name of the group
    
    Returns an HTML snippet for HTMX to swap in.
    """
    # Check if user is logged in
    if not toolkit.current_user.is_authenticated:
        return '<span class="badge bg-danger">Not authenticated</span>', 401
    
    # Get form data
    dataset_id = toolkit.request.form.get('dataset_id')
    group_id = toolkit.request.form.get('group_id')
    
    if not dataset_id or not group_id:
        return '<span class="badge bg-warning">Missing data</span>', 400
    
    context = {
        'user': toolkit.current_user.name,
    }
    
    data_dict = {
        'id': group_id,            # The group to add to
        'object': dataset_id,      # The dataset to add
        'object_type': 'package',
        'capacity': 'public'
    }
    
    try:
        toolkit.get_action('member_create')(context, data_dict)
        
        # Return success HTML snippet for HTMX
        return (
            '<span class="badge bg-success">'
            '<i class="fa fa-check"></i> Added'
            '</span>'
        )
        
    except toolkit.ObjectNotFound:
        return '<span class="badge bg-danger">Not found</span>', 404
        
    except toolkit.NotAuthorized:
        return '<span class="badge bg-danger">Not authorized</span>', 403
        
    except toolkit.ValidationError:
        return '<span class="badge bg-danger">Error</span>', 400


def group_add_status(group_id, dataset_id):
    """
    GET /group-add/status/<group_id>/<dataset_id>
    
    Checks if a dataset is already a member of a group.
    Returns an HTML snippet showing the current status.
    """
    # Check if user is logged in
    if not toolkit.current_user.is_authenticated:
        return '<span class="badge bg-secondary">-</span>', 401
    
    try:
        # Query the Member table directly to check membership
        member = model.Session.query(model.Member).filter(
            model.Member.group_id == group_id,
            model.Member.table_id == dataset_id,
            model.Member.table_name == 'package',
            model.Member.state == 'active'
        ).first()
        
        if member:
            # Already in group
            return (
                '<span class="badge bg-success">'
                '<i class="fa fa-check"></i> In group'
                '</span>'
            )
        else:
            # Not in group - show add button
            return (
                f'<button type="button" '
                f'class="btn btn-sm btn-outline-primary" '
                f'hx-post="/group-add/add" '
                f'hx-vals=\'{{"dataset_id": "{dataset_id}", "group_id": "{group_id}"}}\' '
                f'hx-swap="outerHTML">'
                f'<i class="fa fa-plus"></i> Add'
                f'</button>'
            )
            
    except Exception:
        return '<span class="badge bg-warning">Error</span>', 500


# Register the routes
digitizationknowledge.add_url_rule(
    "/group-add/groups",
    view_func=group_add_list_groups,
    methods=['GET']
)

digitizationknowledge.add_url_rule(
    "/group-add/add",
    view_func=group_add_dataset,
    methods=['POST']
)

digitizationknowledge.add_url_rule(
    "/group-add/status/<group_id>/<dataset_id>",
    view_func=group_add_status,
    methods=['GET']
)



# =============================================================================
# Blueprint registration
# =============================================================================

def get_blueprints():
    return [digitizationknowledge]

