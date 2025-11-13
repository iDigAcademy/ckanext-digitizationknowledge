import ckan.plugins.toolkit as toolkit
from typing import Any

# Define Template helper functions
def get_custom_featured_groups(count: int = 1):
    '''
    Returns a list of featured groups using an extra field as filter
    '''
    try:
        # Get all groups with basic fields to filter
        groups = toolkit.get_action('group_list')(
            {},
            {'all_fields': True, 'include_extras': True}
        )
        # Filter for featured groups
        featured_group_ids = [
            group.get('name') or group.get('id') for group in groups 
            if group.get('is_featured')
        ]
        
        # Get full details for each featured group
        groups_data = []
        for group_id in featured_group_ids:
            if len(groups_data) >= count:
                break
            try:
                context = {
                    'ignore_auth': True,
                    'limits': {'packages': 2},
                    'for_view': True
                }
                data_dict = {
                    'id': group_id,
                    'include_datasets': True
                }
                group = toolkit.get_action('group_show')(context, data_dict)
                groups_data.append(group)
            except toolkit.ObjectNotFound:
                continue
        
        return groups_data
    except toolkit.NotAuthorized:
        return []

def get_custom_featured_organizations(count: int = 1):
    '''
    Returns a custom list of featured organizations using field in extras
    '''
    try:
        # Get all organizations with basic fields to filter
        orgs = toolkit.get_action('organization_list')(
            {},
            {'all_fields': True, 'include_extras': True}
        )
        # Filter for featured organizations
        featured_org_ids = [
            org.get('name') or org.get('id') for org in orgs 
            if org.get('is_featured')
        ]
        
        # Get full details for each featured organization
        orgs_data = []
        for org_id in featured_org_ids:
            if len(orgs_data) >= count:
                break
            try:
                context = {
                    'ignore_auth': True,
                    'limits': {'packages': 2},
                    'for_view': True
                }
                data_dict = {
                    'id': org_id,
                    'include_datasets': True
                }
                org = toolkit.get_action('organization_show')(context, data_dict)
                orgs_data.append(org)
            except toolkit.ObjectNotFound:
                continue
        
        return orgs_data
    except toolkit.NotAuthorized:
        return []

def get_helpers():
    return {
        "get_custom_featured_groups": get_custom_featured_groups,
        "get_custom_featured_organizations": get_custom_featured_organizations,
    }
    
    # nameCallableFromTemplate:nameOfFunction
