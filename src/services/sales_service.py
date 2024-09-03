from src.services.email_service import EmailService

class SaleService:
    def __init__(self, to: list[str], title: str, message: str, cc: list[str] = [], attachment: str | None = None) -> None:
        pass
        self.to = to
        self.title = title
        self.message = message
        self.cc = cc
        self.attachment = attachment
        self.email = EmailService() 
    
    def get_sales_tambo (self):
        try:
            pass
            success = self.email.send(
                self.to,
                self.title,
                self.message,
                self.cc,
                self.attachment
            )
            print("Sales Tambo processed:", success)
        except Exception as e:
            raise e
            
    def get_sales_aruma (self):
        print("Hola aruma")