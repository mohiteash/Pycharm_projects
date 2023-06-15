Feature: Demo Web Shop

  Background: Common steps
    Given launch the browser
    When open demo web shop home page
    And click on Electronics category


  Scenario: click on camera
    Then Click on camera
    And Click on sort by dropdown, click on "Name: A to Z" for camera
    And Click on sort by dropdown, click on "Name: Z to A" for camera
    And Click on sort by dropdown, click on "Price: Low to High" camera
    And Click on sort by dropdown, click on "Price: High to Low" camera
    And Click on sort by dropdown, click on "Created on" camera
    And click on display, click on 4 for camera
    And click on display, click on 8 for camera
    And click on display, click on 12 for camera
    And click on view by, click on "list" for camera
    And click on view by, click on  "Grid" for camera
    And click on filter under 500 for camera
    And click on Remove_filter for camera
    And click on filter over 500 for camera
    And click on Removefilter for camera
    And click on one of the product and see its description for camera
    And come back and click on another product description and come back for camera
    Then verify the camera page is modified as selected options for camera


  Scenario: click on cell phone
    Then Click on cell phone
    And Click on sort by dropdown, click on "Name: A to Z" for cell_phone
    And Click on sort by dropdown, click on "Name: Z to A" for cell_phone
    And Click on sort by dropdown, click on "Price: Low to High" for cell_phone
    And Click on sort by dropdown, click on "Price: High to Low" for cell_phone
    And Click on sort by dropdown, click on "Created on" for cell_phone
    And click on display, click on 4 for cell_phone
    And click on display, click on 8 for cell_phone
    And click on display, click on 12 for cell_phone
    And click on view by, click on cell_list for cell_phone
    And click on view by, click on cell_Grid for cell_phone
    And click on one of the product and see its description for cell_phone
    And come back and click on another product description and come back for cell_phone
    And click on one of the product to cart for cell_phone
    Then verify the cell phone page is modified as selected options and product is added to cart for cell_phone




