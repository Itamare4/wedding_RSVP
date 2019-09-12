# wedding_RSVP

<p align="center">
<img src="https://github.com/Itamare4/wedding_RSVP/blob/master/SMS/Wedding_RSVP.png?raw=true" height="400" width=auto>
</p>

### Brief ###
System that sends, recieves, and proccess SMS from guests to confirm the estimated guests that will arrive to the wedding(RSVP), it uses AirMore(Android Side) & pyairmore(PC side) to send the SMS through mobile network.


### SMS RSVP ###
### Prerequisites ###
* Fill attached excel file with the guests details (currently tested only in Israel, try to change the COUNTRY_AREA_CODE)
* Install pyairmore (pip install pyairmore)
* Configure IP address (line 21)
* Change invitation, transportation etc. to your custom message.


### WEBSITE RSVP ###
<p align="center">
<img src="https://github.com/Itamare4/wedding_RSVP/blob/master/Website/website_screenshot.jpg?raw=true" height="400" width=auto>
</p>

Idea was to create a website that holds the wedding invitation, link to Waze navigation, and guests can register to the wedding bus.  
Database is based on simple PHP, SQL form, that saves the name, phone number, and number of seats to reserve on the bus.
Many parts of this code can be cleaned, i didn't use most of the features from registration and login.  
Code was based on registration and login from html-form-guide.com.

### About ###
Itamar Eliakim<br>
M.Sc Robotics Engineer, Tel Aviv, Israel<br>
Email - Itamare@gmail.com
