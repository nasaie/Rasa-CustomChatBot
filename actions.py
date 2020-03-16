# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
# from rasa_platform.core.tracker_store import InMemoryTrackerStore

class ActionAccount1(Action):

    def name(self) -> Text:
        return "action_account1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="1. To ensure a complete collection system – Arahan Perbendaharaan 53")
        dispatcher.utter_message(text="2. To provide basic need to public that is notification on receipt for payment made – Arahan Perbendaharaan 61")
        dispatcher.utter_message(text="3. To ensure Pemungut be given authorisation in writing to collect money – Arahan 53 and Arahan Perbendaharaan 69")
        dispatcher.utter_message(text="4. To ensure complete set of documents – Arahan Perbendaharaan 6")

        return []

class ActionAccount2(Action):

    def name(self) -> Text:
        return "action_account2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="1. Kewangan 248 is a cash book that shows information about collection of monies, amount of monies credited to banks and also the classification of accounts to which the monies are credited to.")
        dispatcher.utter_message(text="2. Kewangan 249 is a main cash book used by Pemungut whom does not have many types of collection.")

        return []

class ActionAccount3(Action):

    def name(self) -> Text:
        return "action_account3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Debit Advice ia a document used by banks to show the transfer of money from one’s account to another account. In the case of Custom’s Pemungut, it is a document that shows transfer of Customs revenue collection for a certain period of time from Customs Station’s accounts to Customs Main collection account.")

        return []

class ActionAccount4(Action):

    def name(self) -> Text:
        return "action_account4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="In order for a Penyata Pemungut to be processed the following documents are needed :")
        dispatcher.utter_message(text="1. Penyata Pemungut that consists of Borang Slip Masuk Bank that has bank’s confirmation credit print-out, Pungutan Dimasukira Ke Dalam Akaun-Akaun Di Bawah, Senarai Cek/Kiriman Wang/Wang Pos/Bank Draf Yang Dibayar Masuk, Butir-Butir Akaun Subsidiari (if applicable) and Senarai Resit Yang Dikeluarkan.")
        dispatcher.utter_message(text="2. PC POS / RM 20 / Consol Reports.")
        dispatcher.utter_message(text="3. Debit Advice (whereby the amount of Debit Advice should tally with the amount of the said Penyata Pemungut) – only with regard to Pemungut that use their own bank’s account before being transferred to Customs Main collection account.")

        return []

class ActionInternalTax1(Action):

    def name(self) -> Text:
        return "action_internal_tax1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="A type of tax imposed on certain goods imported into or manufactured in Malaysia.")

        return []

class ActionInternalTax2(Action):

    def name(self) -> Text:
        return "action_internal_tax2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="1. Liquor.")
        dispatcher.utter_message(text="2. Cigarettes, tobacco and tobacco products.")
        dispatcher.utter_message(text="3. Motor Vehicles.")
        dispatcher.utter_message(text="4. Playing cards (Playing Cards).")
        dispatcher.utter_message(text="5. Mahjong tiles.")

        return []

class ActionInternalTax3(Action):

    def name(self) -> Text:
        return "action_internal_tax3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="• Alcohol / Liquor / Todi")
        dispatcher.utter_message(text="• Tobacco / Cigarette")
        dispatcher.utter_message(text="• Vehicle / Playing Cards / Mahjong Tiles")

        return []

class ActionInternalTax4(Action):

    def name(self) -> Text:
        return "action_internal_tax4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Submit an application letter together with 2 copies of form JKED No.1 and supporting documents to the nearest customs office.")

        return []

class ActionInternalTax5(Action):

    def name(self) -> Text:
        return "action_internal_tax5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="1. Imported Cigarettes have a tax label affixed to the box")
        dispatcher.utter_message(text="2. Locally manufactured cigarette have a security ink mark printed (diamond) on box")

        return []

class ActionInternalTax6(Action):

    def name(self) -> Text:
        return "action_internal_tax6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="1. Imported liquor / locally manufactured liquor has tax label affixed to bottles / cans / containers")
        dispatcher.utter_message(text="2. Locally manufactured beer/stout has a security ink mark printed on bottle/can/container")

        return []

class ActionInternalTax7(Action):

    def name(self) -> Text:
        return "action_internal_tax7"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Goods have to be declared in customs import declaration Form No. 1 and the duty / tax assessed paid to the customs office where goods are released from customs control.")

        return []

class ActionInternalTax8(Action):

    def name(self) -> Text:
        return "action_internal_tax8"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Form Excise no.8 is to be submitted together with necessary documents before approval is given and movement authorised.")

        return []

class ActionInternalTax9(Action):

    def name(self) -> Text:
        return "action_internal_tax9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Vehicles only – Submit Excise No. 8 and customs form no. 7 together with necessary documents for approval and authorization of movement. Bagi barangan am – Mengemukakan Borang Kastam 3 beserta dokumen sokongan untuk kelulusan.")

        return []

class ActionInternalTax10(Action):

    def name(self) -> Text:
        return "action_internal_tax10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="4 years.")

        return []

class ActionInternalTax11(Action):

    def name(self) -> Text:
        return "action_internal_tax11"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The list of eligible persons and goods can be found at http://tariff.customs.gov.my")

        return []
