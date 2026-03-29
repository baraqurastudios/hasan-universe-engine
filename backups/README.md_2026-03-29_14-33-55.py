from safety.advanced_traps import FinalSafeguard

safeguard = FinalSafeguard()

def check_panic_command(command):
    if command == "PROTOCOL_BLACK":
        safeguard.initiate_blackout()
    
    elif command == "TRAP_PARADOX":
        safeguard.trigger_paradox()
        
    elif command == "TOTAL_WIPE":
        print("💀 MASTER COMMAND: REALITY WIPE.")
        sys.exit(1)