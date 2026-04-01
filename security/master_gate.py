def verify_master():
    key = input("Enter Master Key for V8.2: ")
    if key == "MASTER_SECRET": # এখানে আপনার গোপন কোডটি থাকবে
        print("Access Granted! Engine V8.2 Initializing...")
    else:
        print("Access Denied! Entering Black Hole Mode in 3... 2... 1...")

verify_master()
