def get_dict(f_name):  # function to get a sorted (by time) dictionary by reading the data file
    dict = {}
    with open(f_name, 'r') as f:
        f.readline()
        for line in f:
            name, crossing, gate_no, time = (line.strip()).split(', ')
            if name not in dict:
                dict[name] = {'crossing': [], 'gate no.': [], 'time': []}
            dict[name]['crossing'].append(crossing)
            dict[name]['gate no.'].append(gate_no)
            dict[name]['time'].append(time)
    for name, data in dict.items():
        data['time'], data['crossing'], data['gate no.'] = zip(
            *sorted(zip(data['time'], data['crossing'], data['gate no.']), key=lambda x: time_to_sec(x[0])))
    return dict


def time_to_sec(time):  # function to convert hh:mm:ss into for seconds for calculation purposes
    hrs, mins, sec = time.split(':')
    return (int(hrs) * 3600) + (int(mins) * 60) + (int(sec))


# function which returns the type of crossing which has been made for an entry just before the current time or at the current time
def nearest_entry_before_cur_time(dict, name, time):
    times = dict[name]['time']
    crossings = dict[name]['crossing']
    for i in range(len(times) - 1, -1, -1):
        if time_to_sec(times[i]) <= time:
            return crossings[i]
    return None


def stud_record(dict, name):  # function which writes the contents for a given student into a file and determines whether that student is present in the campus using the nearest_entry_using_cur_time function by taking in current time as input
    cur_time = input("Enter the current time (hh:mm:ss): ")
    cur_time = time_to_sec(cur_time)
    if name not in dict:
        print(f"{name} not found in the data\n")
        return
    with open(f"Record of {name}.txt", "w") as f:
        for i in range(len(dict[name]['crossing'])):
            f.write(
                f"{(dict[name]['crossing'][i], dict[name]['gate no.'][i], dict[name]['time'][i])}\n")
    print(f"Record of {name} has been written to a file.")

    # code block which determines whether student is present in campus currently
    if nearest_entry_before_cur_time(dict, name, cur_time) == None:
        print(f"{name} is currently not present in the campus.\n")
    else:
        crossing = nearest_entry_before_cur_time(
            dict, name, cur_time)
        if crossing == "ENTER":
            print(f"{name} is currently present in the campus.\n")
        else:
            print(f"{name} is currently not present in the campus.\n")


# function which writes into a file all the student entries made between a time duration
def time_dur(dict, start_time, end_time):
    start_time = time_to_sec(start_time)
    end_time = time_to_sec(end_time)
    with open("Entries between given time duration.txt", "w") as f:
        for name, data in dict.items():
            for i in range(len(data['time'])):
                if start_time <= time_to_sec(data['time'][i]) <= end_time:
                    f.write(
                        f"{name}, {data['crossing'][i]}, {data['gate no.'][i]}, {data['time'][i]}\n")
    print("entries between the given time duration have been written in file successully.")


def gate_cnt(dict, gate_no):  # function which counts the entries and exits made by a gate
    enter_cnt = 0
    exit_cnt = 0
    for _, data in dict.items():
        for i in range(len(data['time'])):
            if data['gate no.'][i] == gate_no:
                if data['crossing'][i] == "ENTER":
                    enter_cnt += 1
                else:
                    exit_cnt += 1
    print(f"Number of students entered through gate {gate_no}: {enter_cnt}")
    print(f"Number of students exited through gate {gate_no}: {exit_cnt}")


print("Menu:")
print("1. Give a student name to get the record of him/her moving in/out of campus and whether they are currently present in campus or not.")
print("2. Give the start time and the end time to get all the students who entered the campus during this time and all students who exited the campus during this time.")
print("3. Give the gate number to get get the number of times students have entered the campus through that gate and the number of times students have exited the campus from that gate.")
print("4. Give nothing and press ENTER to exit.\n")

stud_dict = get_dict("IP Assignment-3/data.txt")

while True:
    ch = input("Enter choice: ")
    print()
    if ch == '1':
        name = input("Enter the student name: ")
        stud_record(stud_dict, name)
    elif ch == '2':
        start_time = input("Enter the start time (hh:mm:ss): ")
        end_time = input("Enter the end time (hh:mm:ss): ")
        time_dur(stud_dict, start_time, end_time)
    elif ch == '3':
        gate_no = input("Enter the gate number: ")
        gate_cnt(stud_dict, gate_no)
    elif ch == '':
        break
    else:
        print("invalid choice. Please try again.")
    print()
