# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



    
    
#  tourist package per head
class ActionPackageIndividual(Action):
    def name(self) -> Text:
        return "action_package_individual"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities= tracker.latest_message['entities']
        print(entities)
        message='place'
        name='action_package_individual'
        print(entities)
        for e in entities:
            if e['entity'] =='place':
                name = e['value']    
        if name == "alappuzha":
            message ="Rs.2999/head  for 3 days"
        if name == "munnar":
            message ="Rs.4999/head  for 4 days"
        if name == "kochi":
            message ="Rs.4999/head  for 4 days"
        if name == "wayanad":
            message ="Rs.5999/head  for 5 days"
        if name == "vagamon":
            message ="Rs.4999/head  for 3 days"
        if name == "kovalam":
            message ="Rs.4999/head  for 4 days"
        if name == "kozhikode":
            message ="Rs.1999/head  for 2 days"
        if name == "thekkady":
            message ="Rs.1999/head  for 2 days"
        if name == "varkala":
            message ="Rs.1999/head  for 1 days"
        if name == "idukki":
            message ="Rs.4999/head  for 5 days"
        print(name)
        dispatcher.utter_message(text=message)
        return []



