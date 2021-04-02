## Time table finder
* greet
  - utter_greet

* inform_timetable{"Timetable" : "timetable", "Course" : "AIDI" , "Group" : "A" , "Date" : "Tuesday" }
  - action_timetable_search

* thanks
  -utter_goodbye


## Time table + course + group
* greet
  - utter_greet
  
* inform_timetable{"Timetable" : "timetable" , "Date" : "Monday" }
  - utter_ask_course

* inform_course{"Course" : "AIDI"}
  - utter_ask_group

* inform_group{"Group" : "A"}
  - action_timetable_search

* thanks
  -utter_goodbye


## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

