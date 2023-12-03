import GtaManager

def run_spoofer():
    gta_manager = GtaManager.GtaManager([""])
    gta_manager.load_logs()
    gta_manager.start_analyzing()
    gta_manager.start_spoofing("")

if __name__ == "__main__":
    run_spoofer()

