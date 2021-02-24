from templatemanager.mongodb import template_collection
from templatemanager.dao.template import (
    Template, TemplateMongoDBDao,
    # SYSTEM_ROLE_SYSTEM_MANAGER, SYSTEM_ROLE_COMMON_USER
)

if __name__ == '__main__':
    template_collection.drop()

    import time

    template1 = Template(
        template_name="example_template_1",
        last_time=time.asctime(time.localtime(time.time())),
        outline="example_template_1_outline",
    )
    template2 = Template(
        template_name="example_template_2",
        last_time=time.asctime(time.localtime(time.time())),
        outline="example_template_2_outline",
    )

    template_mongodb_dao = TemplateMongoDBDao(template_collection)
    template_mongodb_dao.create_template(template1)
    template_mongodb_dao.create_template(template2)
