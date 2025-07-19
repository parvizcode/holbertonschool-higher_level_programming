#!/usr/bin/env python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    for att in attendees:
        if not isinstance(att, dict):
            print("Error: Each attendee must be a dictionary")
            return
        
    if template.strip() == "":
        print("Template is empty, no output.")
        return
    if not attendees:
        print("No data, no output.")
        return
    for idx, attendee in enumerate(attendees, start=1):
        filled_template = template

        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value_str = "N/A"
            else:
                value_str = str(value)
            
            filled_template = filled_template.replace(f"{{{key}}}", value_str)

        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
