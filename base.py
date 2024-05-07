import json
import datetime

class Property:
    def __init__(self, id, location, price, size, property_type):
        self.id = id
        self.location = location
        self.price = price
        self.size = size
        self.property_type = property_type

    def display_info(self):
        print(f"Location: {self.location}")
        print(f"Price: {self.price}")
        print(f"Size: {self.size} sqft")
        print(f"Property Type: {self.property_type}")

class Residential(Property):
    def __init__(self, id, location, price, size, property_type, bedrooms, bathrooms, has_garage):
        super().__init__(id, location, price, size, property_type)
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.has_garage = has_garage

    def display_info(self):
        super().display_info()
        print(f"Bedrooms: {self.bedrooms}")
        print(f"Bathrooms: {self.bathrooms}")
        print(f"Has Garage: {self.has_garage}")

class Commercial(Property):
    def __init__(self, id, location, price, size, property_type, business_type, loading_docks, office_space):
        super().__init__(id, location, price, size, property_type)
        self.business_type = business_type
        self.loading_docks = loading_docks
        self.office_space = office_space

    def display_info(self):
        super().display_info()
        print(f"Business Type: {self.business_type}")
        print(f"Loading Docks: {self.loading_docks}")
        print(f"Office Space: {self.office_space} sqft")

class Agent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def list_properties(self):
        for property in self.properties:
            property.display_info()

class Transaction:
    def __init__(self, id, property_id, agent_id, sale_price, sale_date):
        self.id = id
        self.property_id = property_id
        self.agent_id = agent_id
        self.sale_price = sale_price
        self.sale_date = sale_date

    def record_transaction(self):
        print(f"Transaction recorded: Property {self.property_id} sold for {self.sale_price} on {self.sale_date}")

    def display_transaction_details(self):
        print(f"Transaction Details:")
        print(f"Property ID: {self.property_id}")
        print(f"Agent ID: {self.agent_id}")
        print(f"Sale Price: {self.sale_price}")
        print(f"Sale Date: {self.sale_date}")

class DataHandler:
    def __init__(self, file_path, data_format):
        self.file_path = file_path
        self.data_format = data_format

    def load_data(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data

    def save_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def process_data(self, data):
        properties = []
        for property_data in data:
            if property_data["property_type"] == "Residential":
                property = Residential(property_data["id"], property_data["location"], property_data["price"], property_data["size"], property_data["property_type"], property_data["bedrooms"], property_data["bathrooms"], property_data["has_garage"])
            elif property_data["property_type"] == "Commercial":
                property = Commercial(property_data["id"], property_data["location"], property_data["price"], property_data["size"], property_data["property_type"], property_data["business_type"], property_data["loading_docks"], property_data["office_space"])
            properties.append(property)
        return properties

    def store_properties(self, properties):
        for property in properties:
            property.display_info()

    def display_properties(self, properties):
        for property in properties:
            property.display_info()

# Example usage:
agent = Agent(1, "John Doe")
property = Residential(1, "123 Main St", 500000, 2000, "Residential", 3, 2, True)
agent.add_property(property)
agent.list_properties()

transaction = Transaction(1, 1, 1, 400000, datetime.date(2022, 1, 1))
transaction.record_transaction()
transaction.display_transaction_details()

data_handler = DataHandler("test.json", "json")
data = data_handler.load_data()
properties = data_handler.process_data(data)
data_handler.store_properties(properties)
data_handler.display_properties(properties)

# Assuming the JSON file contains a list of properties
with open("test.json", 'w') as f:
    json.dump(data, f)