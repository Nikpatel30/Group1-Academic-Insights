# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionTimetableSearch(Action):

    def name(self) -> Text:
        return "action_timetable_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sure, I'm on it!")

        return []

class TimetableForm(FormAction):

    def name(self) -> Text:
        return "facility_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["facility_type", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"Course": self.from_entity(entity="Course",
                                        intent=["inform",
                                        "search_provider"]),
                    "Timetable": self.from_entity(entity= "Timetable",
                            intent=["infrom", "search_provider"])
                            }
        
#    def submit(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: Dict[Text, Any]
#                 ) -> List[Dict]:

#         Timetable = tracker.get_slot('Timetable')
#         Course = tracker.get_slot('Course')

#         result = _find_timetable(Timetable, Course)
#         button_name = _resolve_name(TIMETABLE, Timetable)
#         if len(results) == 0:
#             dispatcher.utter_message(
#                 "Sorry, we could not find a {} in {}.".format(button_name, Timetable.title()))

#             return []

#         button = []

#         for r in results[:3]:
