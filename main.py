import ansible_runner
import os

def run_playbook(playbook_path):
    print("Current Directory:", os.getcwd())
    current_directory = os.getcwd()
    playbook_path = os.path.join(current_directory, playbook_name)
    
    if not os.path.isfile(playbook_path):
        print(f"Error: The playbook file {playbook_path} does not exist.")
        return
    
    result = ansible_runner.run(playbook=playbook_path)
    
    if result.status == 'successful':
        print("Playbook executed successfully.")
    else:
        print("Playbook execution failed.")
    
    print("Status:", result.status)
    print("Stats:", result.stats)
    print("RC:", result.rc)
    print("Events:", list(result.events))

if __name__ == "__main__":
    playbook_path = 'helloworld.playbook'
    run_playbook(playbook_path)
