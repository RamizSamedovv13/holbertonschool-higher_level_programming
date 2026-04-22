def generate_invitations(template, attendees):
    # Input type yoxlaması
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(person, dict) for person in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Boş input yoxlaması
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Hər iştirakçı üçün fayl yarat
    for index, person in enumerate(attendees, start=1):
        invitation = template

        placeholders = ["name", "event_title", "event_date", "event_location"]

        for field in placeholders:
            value = person.get(field)

            if value is None:
                value = "N/A"

            invitation = invitation.replace("{" + field + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
