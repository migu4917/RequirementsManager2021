from dataclasses import dataclass
from typing import Dict, List

from pymongo.collection import Collection


@dataclass
class Document:
    _id: str
    document_name: str
    introduction: str
    last_time: str
    content: str  # todo

    def jsonify(self) -> Dict:
        return {
            '_id': self._id,
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
        pass

    def delete_document(self, _id: str):
        pass

    def edit_document(self, _id: str, attributes: Dict):
        pass

    def get_document(self, _id: str) -> Document:
        pass

    def get_all_document(self) -> List[Document]:
        pass
