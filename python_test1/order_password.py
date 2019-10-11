
password = [0, 1, 4]
user_entry = []
print("Password: ")
while True:
    entry = int(input())
    user_entry.append(entry)

    for i in range(len(user_entry)):
        if user_entry[i] != password[i]:
            user_entry = []
            print("Reseting: ")
            break

    if len(user_entry) == len(password):
        print("OK")
        break
