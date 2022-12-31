""" The application is developed by Kittipich "Luke" Aiumbhornsin
Created on December 3, 2022
Run file of the application """

from christmas_app import systemInfo, create_app
from decouple import config as en_var # import the environment var
# import pytz

print("SystemInfo -> ", systemInfo)
# print("Environment Variable: "+ en_var('christmas_app2022'))

# print(pytz.all_timezones) # List out all the timezone available
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=9999)