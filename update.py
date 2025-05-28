from datetime import datetime

# Write the current timestamp to a file
with open("last_updated.txt", "w") as f:
    f.write("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
