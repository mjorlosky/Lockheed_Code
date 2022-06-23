from parse_utils import parse_date


# Files
fname_personal = '/Users/michaelorlosky/Documents/Lockheed_Code/python-deepdive-master/Part 2/Section 09 - Project 4/project_4_goal_1/data/personal_info.csv'
fname_employment = 'data/employment.csv'
fname_vehicles = 'data/vehicles.csv'
fname_update_status = 'data/update_status.csv'
fnames = fname_personal, fname_employment, fname_vehicles, fname_update_status

# Parsers
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, int, str)
vehicle_parser = (str, str, str, str)
update_status_parser = (str, parse_date, parse_date)
parsers = personal_parser, employment_parser, vehicle_parser, update_status_parser

# Named Tuple Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name
