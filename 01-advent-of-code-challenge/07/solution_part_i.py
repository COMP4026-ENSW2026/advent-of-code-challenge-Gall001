
def get_file_system_directories(file):
    current_path = ""
    directories = {"/home": 0}
    for line in file.read().splitlines():
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == "..":
                    current_path = current_path[:current_path.rindex("/")]
                elif line[2] == "/":
                    current_path = "/home"
                else:
                    current_path = current_path + "/" + line[2]
                    directories[current_path] = 0
        else:
            if line[0] != "dir":
                temp_path = current_path
                while temp_path != "":
                    directories[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex("/")]
    sum_small_directories = 0
    for _, directory in directories.items():
        if directory <= 100000:
            sum_small_directories += directory
    print(sum_small_directories)

filename =  open('01-advent-of-code-challenge/07/sample.in', 'r')
print(get_file_system_directories(filename))