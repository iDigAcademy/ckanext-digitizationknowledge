import ckan.plugins.toolkit as toolkit
from typing import Any

# Define Template helper functions
def get_custom_featured_groups(count: int = 1):
    '''
    Returns a list of featured groups using the is_featured field.
    Uses group_show to reliably get the is_featured field for each group.
    '''
    try:
        # Get all groups (just names)
        all_groups = toolkit.get_action('group_list')({}, {})
        
        groups_data = []
        for group_name in all_groups:
            if len(groups_data) >= count:
                break
            
            try:
                context = {
                    'ignore_auth': True,
                    'limits': {'packages': 2},
                    'for_view': True
                }
                data_dict = {
                    'id': group_name,
                    'include_datasets': True
                }
                # group_show DOES return is_featured reliably
                group = toolkit.get_action('group_show')(context, data_dict)
                
                # Check if featured (field is in the show response)
                if group.get('is_featured'):
                    groups_data.append(group)
            except toolkit.ObjectNotFound:
                continue
        
        return groups_data
    except Exception:
        return []

def get_custom_featured_organizations(count: int = 1):
    '''
    Returns a list of featured organizations using the is_featured field.
    Uses organization_show to reliably get the is_featured field for each org.
    '''
    try:
        # Get all organizations (just names)
        all_orgs = toolkit.get_action('organization_list')({}, {})
        
        orgs_data = []
        for org_name in all_orgs:
            if len(orgs_data) >= count:
                break
            
            try:
                context = {
                    'ignore_auth': True,
                    'limits': {'packages': 2},
                    'for_view': True
                }
                data_dict = {
                    'id': org_name,
                    'include_datasets': True
                }
                # organization_show DOES return is_featured reliably
                org = toolkit.get_action('organization_show')(context, data_dict)
                
                # Check if featured (field is in the show response)
                if org.get('is_featured'):
                    orgs_data.append(org)
            except toolkit.ObjectNotFound:
                continue
        
        return orgs_data
    except Exception:
        return []

def get_helpers():
    return {
        "get_custom_featured_groups": get_custom_featured_groups,
        "get_custom_featured_organizations": get_custom_featured_organizations,
    }
    
    # nameCallableFromTemplate:nameOfFunction
