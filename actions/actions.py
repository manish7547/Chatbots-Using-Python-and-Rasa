# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionReturnCourses(Action):

     def name(self) -> Text:
         return "action_return_courses"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          
            entities = tracker.latest_message['entities']
            
            entity_name = entities[0]['entity']

            if entity_name == "subject":
                 entity_value = entities[0]['value']

            if entity_value == "data science":                 
                 message = """ Please find the details of Data Analytics in the link below:
                         https://www.itvedant.com/data-science-and-ai """
            elif entity_value == "data analytics":
                 message = """ Please find the details of Data Analytics in the link below:
                         https://www.itvedant.com/master-business-data-analytics """
            elif entity_value == "full stack web developement":
                 message = """ Please find the details of full stack web developement in the link below:
                         https://www.itvedant.com/full-stack-developer """
            elif entity_value == "java training":
                 message = """ Please find the details of java training in the link below:
                         https://www.itvedant.com/java-course """
            elif entity_value == "php mysql":
                 message = """ Please find the details of php mysql in the link below:
                         https://www.itvedant.com/training/php-training-course """
            elif entity_value == "mean stack":
                 message = """ Please find the details of mean stack in the link below:
                         https://www.itvedant.com/training/mean-stack-development """
            elif entity_value == "dot net":
                 message = """ Please find the details of dot net  in the link below:
                         https://www.itvedant.com/training/dot-net-training-course """
            elif entity_value == "all":
                 message = """ Please find the details of all courses in the link below:
                         https://www.itvedant.com/training/ """
            else:
                 message = "Sorry, we do not provide this course"


            dispatcher.utter_message(text= message)
            return []
          

class ActionReturnForm(Action):

      def name(self) -> Text:
         return "action_return_form"

      def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
         dispatcher.utter_message(text="https://forms.gle/umrFZYjnDjq4q35X7")
         return []

class ActionReturnSm(Action):

     def name(self) -> Text:
         return "action_return_sm"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          
            entities = tracker.latest_message['entities']
            
            entity_name = entities[0]['entity']

            if entity_name == "sm":
                 entity_value = entities[0]['value']

            if entity_value == "facebook":                 
                 message = "facebook.com/itvedant"
            elif entity_value == "instagram":
                 message = "instagram.com/itvedant/"
            elif entity_value == "linkedin":
                 message = "linkedin.com/company/itvedant/"
            else:
                 message = "Thats it"
    






