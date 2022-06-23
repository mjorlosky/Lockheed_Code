from parser import parse_date

personal_filename = '/Users/michaelorlosky/Documents/Lockheed_Code/python-deepdive-master/Part 2/Section 09 - Project 4/project_4_goal_1/data/personal_info.csv'
employment_filename = 'data/employment.csv'
status_filename = 'data/update_csv'
vehicle_filename = 'data/vehicles.csv'
files = personal_filename, employment_filename, status_filename, vehicle_filename

personal_parser = (str, str, str, str, str)
employment_parser = (str, str, int, str)
status_parser = (str, parse_date, parse_date)
vehicle_parser = (str, str, str, str)
full_parser = personal_parser, employment_parser, status_parser, vehicle_parser

personal_class = 'Personal'
employment_class = 'Employment'
status_class = 'Status'
vehicle_class = 'Vehicle'
classes = personal_class, employment_class, status_class, vehicle_class