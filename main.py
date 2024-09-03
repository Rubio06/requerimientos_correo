from src.services.sales_service import SaleService

class Main:
    def __init__(self) -> None:
        pass
        self.sale_service = SaleService(
            to = ["lindcorpprueba@gmail.com"], 
            title = "Este es mi titulo 2", 
            message = "Este es el mensaje numero dos", 
            cc = ["mensaje cc"], 
            attachment = "prueba.xlsx"
        )
    
    def process (self):
        pass
        self.sale_service.get_sales_tambo()

Main().process()
