import ckan.plugins.toolkit as toolkit

# Define Template helper functions
def get_custom_featured_groups():
    '''
    Returns a list of featured groups using an extra field as filter
    '''
    try:
        # Get all groups with all fields.
        groups = toolkit.get_action('group_list')(
            {},
            {'all_fields': True, 'include_extras': True}
        )
        # Filter for featured groups.
        filtered_groups = [
            group for group in groups if group.get('is_featured')
        ]
        return filtered_groups
    except toolkit.NotAuthorized:
        return []

def get_custom_featured_organizations():
    '''
    Returns a custom list of featured organizations using field in extras
    '''
    try:
        # Get all organizations with all fields.
        orgs = toolkit.get_action('organization_list')(
            {},
            {'all_fields': True, 'include_extras': True}
        )
        # Filter for featured organizations
        featured_orgs = [
            org for org in orgs if org.get('is_featured')
        ]
        return featured_orgs
    except toolkit.NotAuthorized:
        return []

def get_helpers():
    return {
        "get_custom_featured_groups": get_custom_featured_groups,
        "get_custom_featured_organizations": get_custom_featured_organizations,
    }
    
    # nameCallableFromTemplate:nameOfFunction
