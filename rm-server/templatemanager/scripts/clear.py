from templatemanager.mongodb import template_collection, document_collection


if __name__ == '__main__':
    template_collection.drop()
    document_collection.drop()