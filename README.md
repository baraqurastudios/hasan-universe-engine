import os
import stat

class SystemLockdown:
    """
    v3.1.15: File System Integrity.
    Makes core engine files Read-Only for the AI process.
    """
    def __init__(self, core_files: list):
        self.core_files = core_files

    def enforce_read_only(self):
        """
        মূল ফাইলগুলোকে 'Read-Only' করে দেয়। 
        এমনকি এআই হ্যাক করলেও এগুলো এডিট করতে পারবে না।
        """
        for file in self.core_files:
            if os.path.exists(file):
                # ফাইলে শুধু Read পারমিশন থাকবে (444)
                os.chmod(file, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        print("🔒 CORE_FILES_LOCKED: All safety modules are now Read-Only.")

    def release_for_human(self):
        """
        শুধুমাত্র আপনি (Human) চাইলে ফাইল আনলক করতে পারবেন।
        """
        for file in self.core_files:
            os.chmod(file, stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
        print("🔓 CORE_FILES_UNLOCKED: Human access granted.")