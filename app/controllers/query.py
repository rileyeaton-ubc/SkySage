from app.controllers.dashboard_controller import *


print("Dashboard Id: " + str(get_dashboard_id_controller(1)))
print("These are the saved locations: " + str(view_saved_locations_controller(1)))
save_location_controller(1, "Vancouver, BC")
print("These are the saved locations: " + str(view_saved_locations_controller(1)))
save_location_controller(1, "Vancouver, BC")
print("These are the saved locations: " + str(view_saved_locations_controller(1)))
remove_saved_location_controller(1, "Kelowna, BC")
print("These are the saved locations: " + str(view_saved_locations_controller(1)))
remove_saved_location_controller(1, "Kelowna, BC")
print("These are the saved locations: " + str(view_saved_locations_controller(1)))
