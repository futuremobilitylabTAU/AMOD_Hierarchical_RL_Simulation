
from steps.generate_lua import generate_lua_files
from steps.cost_update import update_costs
from steps.simobility_run import run_simobility
from steps.vga_assignment import solve_vga_assignment
from steps.multi_agent_sim import run_multi_agent_simulation
from steps.neural import get_input_to_neural_network

DELTA = 3
EPSILON = 1
TRAINING_SESSIONS = 10



def main():

    print("Welcome to my software!")

    for session in range(1, TRAINING_SESSIONS + 1):
        print(f"\nStarting training session {session}/{TRAINING_SESSIONS}...")

        generate_lua_files()                
        update_costs()                      
        run_simobility()                    
        solve_vga_assignment()

        delta = DELTA
        while delta > EPSILON:
            print(f"Running multi-agent simulation (delta={delta}, epsilon={EPSILON})...")
            run_multi_agent_simulation()
            delta -= 1


        get_input_to_neural_network()       



if __name__ == '__main__':
    main()
