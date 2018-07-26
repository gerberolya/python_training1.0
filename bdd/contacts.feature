Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <company>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact


  Examples:

  | firstname  | lastname  | company  |
  | firstname1 | lastname1 | company1 |
  | firstname2 | lastname2 | company2 |



Scenario: Delete contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete random contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario Outline: Modify contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a new contact info with <firstname>, <lastname> and <company>
  When I modify random contact from the list
  Then the new contact list is equal to the old list with modifiyed contact

  Examples:

  | firstname  | lastname  | company  |
  | firstname3 | lastname3 | company3 |
