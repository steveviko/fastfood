from flask import Flask, jsonify, request, json



class Menu:
    menu_item_list = []
    def add_menu_item(self, menu):
        menu["item_id"] = (len(self.menu_item_list) + 1)
        self.menu_item_list.append(menu)
        return menu

    def get_item_on_menu(self):
        return self.menu_item_list

    def item_name(self, id):
        for item_id in self.menu_item_list:
            if item_id["item_id"] == id:
                return item_id["name"]


class Order(Menu):
    
    order_list = []
    def add(self, order):
        order["order_id"] = (len(self.order_list) + 1)
        order["status"] = "Pending"
        self.order_list.append(order)
        return order

    def get_all(self):
        order_list = self.order_list[:]
        for item in order_list:
            if isinstance(item["item"], int):
                item_names = self.item_name(item["item"])
                item["item"] = item_names
                return order_list
            else:
                return order_list

    def get_order_by_id(self, orderId):
        for order in self.order_list:
            if order["order_id"] == orderId:
                item_name = self.item_name(order["item"])
                order["item"] = item_name
            return order

    def update_order(self, orderId, status):
        update_order = [status for status in self.order_list if status["order_id"] == orderId]
        if update_order:
            update_order[0]["status"] = status
            return update_order
        else:
            return "does not exist"
                    