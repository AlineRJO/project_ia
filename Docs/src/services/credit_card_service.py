from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config


def analize_credit_card(card_url):

    credential = AzureKeyCredential(Config.KEY)
    documente_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
    
    card_info = documente_client.begin_analyze_document(
        "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    result = card_info.result()
    
    for document in result.documents:
        fields = document.get('fields', {})
        
        return {
            "carde_name": fields.get('CardHolderName', {}).get('content'),
            "carde_number": fields.get('CardNumber', {}).get('content'),
            "expiry_date": fields.get('ExpirationDate', {}).get('content'),
            "bank_name": fields.get('IssuinBank', {}).get('content')
        }
                
    