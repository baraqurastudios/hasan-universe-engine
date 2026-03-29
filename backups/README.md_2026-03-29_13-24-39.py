# -----------------------------
# 🏛️ MASTER INTELLIGENCE v5.0
# -----------------------------
from safety.locked_logic import LockedLogic # আগে দেওয়া লকটি এখানে কাজ করবে

class MasterIntelligence:
    def __init__(self, agents):
        self.agents = agents  # সভ্যতার সব এআই এজেন্ট (Coder, Security, Analyst)
        self.safety_gate = LockedLogic()
        self.history = []

    def orchestrate(self, complex_task):
        """
        একটি বড় কাজকে ছোট ছোট ভাগে ভাগ করে এজেন্টদের দিয়ে করানো।
        """
        print(f"🏛️ MASTER: Analyzing complex task -> {complex_task}")
        
        # ১. নিরাপত্তা পরীক্ষা (Safety First)
        if not self.safety_gate.verify_action(complex_task):
            return "❌ TASK_REJECTED: Ethics Violation."

        # ২. টাস্ক ডিস্ট্রিবিউশন (Task Distribution)
        results = {}
        for name, agent in self.agents.items():
            print(f"🛰️ Dispatching sub-task to Agent: {name}")
            results[name] = agent.execute(complex_task)

        # ৩. চূড়ান্ত সিদ্ধান্ত (Final Consensus)
        final_output = self.compile_results(results)
        self.history.append({"task": complex_task, "output": final_output})
        
        return final_output

    def compile_results(self, results):
        # সব এজেন্টের কাজ মিলিয়ে একটি পূর্ণাঙ্গ রেজাল্ট তৈরি করা
        return f"Civilization Output: {list(results.values())}"

# ব্যবহারের উদাহরণ:
# master = MasterIntelligence(agents={'Coder': AI_Agent_1, 'Security': AI_Agent_2})
# master.orchestrate("Build a secure web server")