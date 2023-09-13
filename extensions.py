# Get input from user using File name:
file_name = input("File name: ")

new_file_name = file_name.strip().lower()
# Get output for desired file
if '.gif' in new_file_name:
    print("image/gif")

elif '.jpg' in new_file_name or '.jpeg' in file_name:
    print("image/jpeg")

elif 'png' in new_file_name:
    print("image/png")

elif '.pdf' in new_file_name:
    print("application/pdf")

elif '.txt' in new_file_name:
    print("text/plain")

elif '.zip' in new_file_name:
    print("application/zip")

else:
    print("application/octet-stream")
