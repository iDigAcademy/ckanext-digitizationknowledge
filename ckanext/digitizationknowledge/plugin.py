import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from collections import OrderedDict


# import ckanext.digitizationknowledge.cli as cli
# import ckanext.digitizationknowledge.helpers as helpers
# import ckanext.digitizationknowledge.views as views
from ckanext.digitizationknowledge.logic import (
    validators
    # action, auth, validators
)


class DigitizationknowledgePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "digitizationknowledge")

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    def get_validators(self):
        return validators.get_validators()
    
    # IFacets

    def dataset_facets(self, facets_dict, package_type):
        """Modify the facets_dict and return it
        """
        new_facets = OrderedDict()
        new_facets['type'] = toolkit._('Digitization Resource Type')
        new_facets['category'] = toolkit._('Categories')
        #new_facets['task'] = toolkit._('Tasks')

        # Add the rest of the facets
        for key, value in facets_dict.items():
            new_facets[key] = value

        return new_facets
    
    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict
    
    def organization_facets(self, facets_dict, organization_type, package_type):
        return facets_dict

    def before_dataset_index(self, pkg_dict):
        # Get the task_cluster value

        # for field_name in self.JSON_LIST_FIELDS:
        #     if field_name in pkg_dict:
        #         pkg_dict[field_name] = self._process_json_list_field(
        #             pkg_dict.get(field_name, ''),
        #             field_name
        #         )
        return pkg_dict
   
    # Required methods with default implementations
    
    def before_dataset_search(self, search_params):
        return search_params

    def after_dataset_search(self, search_results, search_params):
        return search_results

    def before_dataset_view(self, pkg_dict):
        return pkg_dict

    def after_dataset_create(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_update(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_delete(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_show(self, context, pkg_dict):
        return pkg_dict

    def create(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass

    def read(self, entity):
        pass

