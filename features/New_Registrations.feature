Feature: Registration

  @Registration
  Scenario: Registration with All Mandatory fields
    Given user is on the login page
    And select the gender
    And enter firstName,lastName,password
    And And enter address fields address1,address2,city,state,postalCode and country
    Then verify account creation is success

#        When user enters valid username "username" and valid password "valid_password"
#        Then the user is logged in

  @Registration2
  Scenario: Registration with mMandatory and Optional fields
    Given user is on the login page
    And select the gender
    And enter firstName,lastName,password
    And And enter address fields address1,address2,city,state,postalCode and country
    And select optional fields
    Then verify account creation is success
    And close the browser
#        When user enters valid username "username" and valid password "valid_password"
#        Then the user is logged in
