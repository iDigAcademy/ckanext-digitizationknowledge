import ckan.plugins.toolkit as toolkit
import ckan.model as model
from typing import Any

# Define Template helper functions
def get_custom_featured_groups(count: int = 1):
    '''
    Returns a list of featured groups using the is_featured field.
    Efficiently queries database first to find featured groups, then gets full details.
    '''
    try:
        # Query database directly for featured group names (fast!)
        query = model.Session.query(model.Group.name).join(
            model.GroupExtra,
            model.Group.id == model.GroupExtra.group_id
        ).filter(
            model.Group.is_organization == False,
            model.Group.state == 'active',
            model.GroupExtra.key == 'is_featured',
            model.GroupExtra.value.in_(['True', 'true', '1', 'yes'])
        ).distinct().limit(count)
        
        featured_names = [name for name, in query.all()]
        
        # Now get full details only for featured groups
        groups_data = []
        for group_name in featured_names:
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
                group = toolkit.get_action('group_show')(context, data_dict)
                groups_data.append(group)
            except toolkit.ObjectNotFound:
                continue
        
        return groups_data
    except Exception:
        return []

def get_custom_featured_organizations(count: int = 1):
    '''
    Returns a list of featured organizations using the is_featured field.
    Efficiently queries database first to find featured orgs, then gets full details.
    '''
    try:
        # Query database directly for featured org names (fast!)
        query = model.Session.query(model.Group.name).join(
            model.GroupExtra,
            model.Group.id == model.GroupExtra.group_id
        ).filter(
            model.Group.is_organization == True,
            model.Group.state == 'active',
            model.GroupExtra.key == 'is_featured',
            model.GroupExtra.value.in_(['True', 'true', '1', 'yes'])
        ).distinct().limit(count)
        
        featured_names = [name for name, in query.all()]
        
        # Now get full details only for featured orgs
        orgs_data = []
        for org_name in featured_names:
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
                org = toolkit.get_action('organization_show')(context, data_dict)
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
