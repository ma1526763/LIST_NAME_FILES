with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()
    name_list[-1] = f"{name_list[-1]}\n"
with open("Input/Letters/starting_letter.txt") as letter:
    first_line, remaining_lines = letter.readline(), letter.read()
    for name in name_list:
        with open(f"Output/ReadyToSend/mail_for_{name[:-1]}.txt", "w") as file:
            file.write(first_line.replace("[name]", name[:-1]))
            file.write(remaining_lines)