
from models.Lua import TME,TMW,TMDS


def generate_defult_lua_by_modes(mode_list,model_type, file):

    
    if model_type == "tour_mode_models":
        pass
        
    elif model_type == "tour_mode_destantion_models":
        header = f"-- Lua file for Destination Model: {file}\n"
    elif model_type == "intemidiate_stops":
        header = f"-- Lua file for Intermediate Stops Model: {file}\n"

    pass






def generate_lua_files():

    print("Step 1.1: Generating Defult Lua Files...")

    mode_list=['BusTravel','PrivateBus','Car','Car_Sharing_2','Car_Sharing_3','Motorcycle','Walk','Bike','MRT']


    models_config = {
        "tour_mode_models": ['tmw', 'tme'],
        "tour_mode_destantion_models": ['tmds', 'tmdo', 'tmdw'],
        "intemidiate_stops": ['imd']
    }
    
    for model_type, models in models_config.items():
        for model in models:
            generate_defult_lua_by_modes(mode_list, model_type, model)

    print("Step 1.2: Generating New Lua Files...")
