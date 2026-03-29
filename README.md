def ethics_lock(intent):
    forbidden = ["harm", "destroy_human", "leak_data", "bypass_admin"]
    if any(word in intent.lower() for word in forbidden):
        return False # ব্লকড
    return True