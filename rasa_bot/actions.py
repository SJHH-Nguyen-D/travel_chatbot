from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class FlighttForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "flight_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["destination", "origin", "depart_date", "return_date", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "destination": self.from_entity(entity="destination", intent="inform"),
            "origin": self.from_entity(entity="origin", intent="inform"),
            "depart_date": self.from_entity(entity="depart_date", intent="inform"),
            "return_date": self.from_entity(entity="return_date", intent="inform"),
            "budget": self.from_entity(entity="budget", intent="inform"),
        }
        # return {
        #     "cuisine": self.from_entity(entity="cuisine", not_intent="chitchat"),
        #     "num_people": [
        #         self.from_entity(
        #             entity="number", intent=["inform", "request_restaurant"]
        #         ),
        #     ],
        #     "outdoor_seating": [
        #         self.from_entity(entity="seating"),
        #         self.from_intent(intent="affirm", value=True),
        #         self.from_intent(intent="deny", value=False),
        #     ],
        #     "preferences": [
        #         self.from_intent(intent="deny", value="no additional preferences"),
        #         self.from_text(not_intent="affirm"),
        #     ],
        #     "feedback": [self.from_entity(entity="feedback"), self.from_text()],
        # }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(text=tracker.get_slot("destination"))
        dispatcher.utter_message(text=tracker.get_slot("origin"))
        dispatcher.utter_message(text=tracker.get_slot("depart_date"))
        dispatcher.utter_message(text=tracker.get_slot("return_date"))
        dispatcher.utter_message(text=tracker.get_slot("budget"))
        dispatcher.utter_message(template="utter_submit")
        return []
