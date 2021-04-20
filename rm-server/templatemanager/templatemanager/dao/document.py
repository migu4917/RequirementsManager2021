from dataclasses import dataclass
from typing import Dict, List

from pymongo.collection import Collection


@dataclass
class Document:
    id: str
    document_name: str
    introduction: str
    last_time: str
    content: str  # todo

    def jsonify(self) -> Dict:
        return {
            'id': self.id,
            'document_name': self.document_name,
            "introduction": self.introduction,
            "last_time": self.last_time,
            'content': self.content,
        }


class DocumentDao:
    def create_document(self, document: Document):
        pass

    def delete_document(self, _id: str):
        pass

    def edit_document(self, _id: str, attributes: Dict):
        pass

    def get_document(self, _id: str) -> Document:
        pass

    def get_all_document(self) -> List[Document]:
        pass


class DocumentMongoDBDao(DocumentDao):
    def __init__(self, collection: Collection):
        self.collection = collection

    def create_document(self, document: Document):
        self.collection.insert_one(document.jsonify())

    def delete_document(self, document_id: str):
        self.collection.delete_one({"id": document_id})

    def edit_document(self, document_id: str, attributes: Dict):
        new_values = {"$set": attributes}
        self.collection.update_one(
            {"id": document_id},
            new_values
        )

    def get_document(self, document_id: str) -> Document:
        document_dict = self.collection.find_one(
            {"id": document_id}
        )
        document = None
        if document_dict:
            document = Document(**document_dict)
        return document
