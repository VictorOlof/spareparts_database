from Data.base_document import Document
from Data.models import employee, order
from Data.pymongo_repository import repo_functions as rf
from Data.pymongo_models import Order
import Data.pymongo_models as mm

print(mm.Order.find_document(employee_id=1))

print(mm.Customer.find_document(first_name="Pelle"))

# mm.Order, employee_id = 1
