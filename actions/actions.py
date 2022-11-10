# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

MVG_STATIONS = [
    {
        "from": "Hochschule Muenchen",
        "to": "Olympiazentrum",
        "time_needed": 21.0
    }
]

# NOTE(Michael): We could use this action to store the name in
#                the TrackerStore (in memory database) or a persitent DB
#                such as MySQL. But we need to store a key-value pair 
#                to identify the user by id eg. (user_id, slotvalue)
class ActionStoreUserName(Action):

     def name(self) -> Text:
         return "action_store_name"
         
     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        print("Sender ID: ", tracker.sender_id)

        return []


class ActionUserName(Action):

     def name(self) -> Text:
         return "action_get_name"

     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        if not username :
            dispatcher.utter_message(" Du hast mir Deinen Namen nicht gesagt.")
        else:
            dispatcher.utter_message(' Du bist {}'.format(username))

        return []

class ActionMVG(Action):

     def name(self) -> Text:
         return "action_get_travel_time"

     def run(self, dispatcher, tracker, domain):
        print("LOG MVG Action: Run method called.")
        from_station = tracker.get_slot("from_station")
        to_station = tracker.get_slot("to_station")
        if not from_station or not to_station :        
            dispatcher.utter_message("Diese Stationen habe ich nicht erkannt!")
        else:
            station = MVG_STATIONS[0]
            print("LOG MVG Action: ", station)
            if from_station == station["from"] and to_station == station["to"]:
                dispatcher.utter_message("Du brauchst exakt {} Minuten. Gute Reise!".format(station["time_needed"]))
            
        return []

