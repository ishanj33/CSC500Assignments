def courseMapping():
    room_dict = {"CSC101":3004, "CSC102":4501, "CSC103":6755, "NET110":1244, "COM241":1411}
    instructors_dict = {"CSC101":"Haynes", "CSC102":"Alvarado", "CSC103":"Rich", "NET110":"Burke", "COM241":"Lee"}
    meeting_time_dict = {"CSC101":"8:00 a.m", "CSC102":"9:00 a.m.", "CSC103":"10:00 a.m.", "NET110":"11:00 a.m.", "COM241":"1:00 p.m."}
    course_num = str(input("Please enter course: "))
    while course_num not in room_dict.keys() or course_num not in instructors_dict.keys() or course_num not in meeting_time_dict.keys():
        course_num = str(input("Please enter a valid course: "))
    print("Room Number:", room_dict[course_num])
    print("Instructor:", instructors_dict[course_num])
    print("Meeting Time:", meeting_time_dict[course_num])

def main():
    courseMapping()
    
if __name__== "__main__":
    main()
