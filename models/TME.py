
from models.Utility import Utility,Beta
import json

class TME:
    def __init__(self):


        self.beta_varibales=None
        self.Modes={'BusTravel':1,'PrivateBus':2,'Car':3,'Car_Sharing_2':4,'Car_Sharing_3':5,'Motorcycle':6,'Walk':7,'Bike':8,'MRT':9}

# utility[1] = cons_PT + 
#             beta_tt_PT * (tt_bus_ivt + tt_bus_walk + tt_bus_wait) +
#             beta_cost * cost_bus + 
#             beta_central_PT * CBD + 
#             beta_parttime_PT * parttime +
#             beta_female_PT * female +
#             beta_TRANS_PT * TRANS + 
#             beta_LIC_PT * LIC +
#             beta_zerocar_PT * zerocar +
#             beta_onecar_PT * onecar + 
#             beta_twocar_PT * twocar +
#             beta_threepluscar_PT * threepluscar +
#             beta_preschool_PT * preschool +
#             beta_undergraduate_PT * undergraduate 


        self.u_bus_driver=Utility("BusTravel",["1","(tt_bus_ivt + tt_bus_walk + tt_bus_wait)","cost_bus","CBD","parttime","female","TRANS",
        "LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("cons_PT",0),Beta("beta_tt_PT",0),Beta("beta_cost",0),Beta("beta_central_PT",0),Beta("beta_parttime_PT",0),
        Beta('beta_female_PT',0),Beta('beta_TRANS_PT',0),Beta('beta_LIC_PT',0),Beta('beta_zerocar_PT',0),Beta('beta_onecar_PT',0), 
        Beta('beta_twocar_PT',0),Beta('beta_threepluscar_PT',0),Beta('beta_preschool_PT',0),Beta('beta_undergraduate_PT',0)])


	# utility[2] = cons_PB + 
    #             beta_tt_PT * tt_privatebus_all + 
    #             beta_central_PT * CBD + 
    #             beta_parttime_PT * parttime +
    #             beta_female_PT * female +
    #             beta_TRANS_PT * TRANS + 
    #             beta_LIC_PT * LIC +
    #             beta_zerocar_PT * zerocar +
    #             beta_onecar_PT * onecar + 
    #             beta_twocar_PT * twocar +
    #             beta_threepluscar_PT * threepluscar +
    #             beta_preschool_PT * preschool +
    #             beta_undergraduate_PT * undergraduate    


        self.u_private_bus_driver=Utility("PrivateBus",["1","tt_privatebus_all","CBD",'parttime','female',
                                               'TRANS','LIC','zerocar','onecar','twocar','threepluscar','preschool','undergraduate'],
                                               [Beta("cons_PB",0),Beta("beta_tt_PT",0),Beta("beta_central_PT",0),Beta("beta_parttime_PT",0),
                                                Beta("beta_female_PT",0),Beta("beta_TRANS_PT",0),Beta("beta_LIC_PT",0),Beta("beta_zerocar_PT",0),
                                                Beta("beta_onecar_PT",0),Beta("beta_twocar_PT",0),Beta("beta_threepluscar_PT",0),Beta("beta_preschool_PT",0),
                                                Beta("beta_undergraduate_PT",0)])
                                                

    # 	utility[3] = cons_drive1 + 
    #              beta_tt_drive1 * tt_cardriver_all + 
    # 	           beta_cost * cost_cardriver + 
    #              beta_central_drive1 * CBD +
    # 	           beta_parttime_drive1 * parttime +
    # 	           beta_female_drive1 * female +
    # 	           beta_TRANS_drive1 * TRANS + 
    #              beta_LIC_drive1 * LIC +
    #              beta_zerocar_drive1 * zerocar +
    # 	           beta_onecar_drive1 * onecar + 
    #              beta_twocar_drive1 * twocar +
    # 	           beta_threepluscar_drive1 * threepluscar +
    # 	           beta_preschool_drive1 * preschool +
    # 	           beta_undergraduate_drive1 * undergraduate 





        self.u_car_driver=Utility("Car",["1","tt_cardriver_all","cost_cardriver","CBD","parttime","female","TRANS","LIC","zerocar",
        "onecar","twocar","threepluscar","preschool","undergraduate"],[Beta("cons_drive1",10),Beta("beta_tt_drive1",0),Beta("beta_cost",0)
        ,Beta("beta_central_drive1",0),Beta("beta_parttime_drive1",0),Beta('beta_female_drive1',0),Beta('beta_TRANS_drive1',0),Beta('beta_LIC_drive1',0),
        Beta('beta_zerocar_drive1',0),Beta('beta_onecar_drive1',0),Beta('beta_twocar_drive1',0),Beta('beta_threepluscar_drive1',0),Beta('beta_preschool_drive1',0),Beta('beta_undergraduate_drive1',0)])



    # 	utility[4] = cons_share2 + 
    #              beta_tt_share2 * tt_carpassenger_all + 
    # 	           beta_cost * cost_carpassenger/2.0  + 
    #              beta_central_share2 * CBD + 
    # 	           beta_parttime_share2 * parttime +
    # 	           beta_female_share2 * female +
    # 	           beta_TRANS_share2 * TRANS + 
    #              beta_LIC_share2 * LIC +
    #              beta_zerocar_share2 * zerocar +
    # 	           beta_onecar_share2 * onecar + 
    #              beta_twocar_share2 * twocar +
    # 	           beta_threepluscar_share2 * threepluscar +
    # 	           beta_preschool_share2 * preschool +
    # 	           beta_undergraduate_share2 * undergraduate 


        self.u_car_sharing_2_driver=Utility("Car_Sharing_2",["1","tt_carpassenger_all","cost_carpassenger/2.0","CBD","parttime","female","TRANS","LIC","zerocar",
        "onecar","twocar","threepluscar","preschool","undergraduate"],[Beta("cons_share2",0),Beta("beta_tt_share2",0),Beta("beta_cost",0),Beta("beta_central_share2",0),
        Beta("beta_parttime_share2",0),Beta("beta_female_share2",0),Beta("beta_TRANS_share2",0),Beta("beta_LIC_share2",0),Beta("beta_zerocar_share2",0),Beta("beta_onecar_share2",0),Beta("beta_twocar_share2",0)
        ,Beta("beta_threepluscar_share2",0),Beta("beta_preschool_share2",0),Beta("beta_undergraduate_share2",0)])



    # 	utility[5] = cons_share3+ 
    #               beta_tt_share3 * tt_carpassenger_all + 
    # 	            beta_cost * cost_carpassenger/3.0  + 
    #               beta_central_share3 * CBD + 
    #               beta_parttime_share3 * parttime +
    # 	            beta_female_share3 * female +
    # 	            beta_TRANS_share3 * TRANS + 
    #               beta_LIC_share3 * LIC +
    #               beta_zerocar_share3 * zerocar +
    # 	            beta_onecar_share3 * onecar + 
    #               beta_twocar_share3 * twocar +
    # 	            beta_threepluscar_share3 * threepluscar +
    # 	            beta_preschool_share3 * preschool +
    # 	            beta_undergraduate_share3 * undergraduate 


        self.u_car_sharing_3_driver=Utility("Car_Sharing_3",["1","tt_carpassenger_all","cost_carpassenger/3.0","CBD","parttime","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar",
        "preschool","undergraduate"],[Beta("cons_share3",0),Beta("beta_tt_share3",0),Beta("beta_cost",0),Beta("beta_central_share3",0),Beta("beta_parttime_share3",0),Beta("beta_female_share3",0),Beta("beta_TRANS_share3",0),
        Beta("beta_LIC_share3",0),Beta("beta_zerocar_share3",0),Beta("beta_onecar_share3",0),Beta("beta_twocar_share3",0),Beta("beta_threepluscar_share3",0),Beta("beta_preschool_share3",0),Beta("beta_undergraduate_share3",0)])


    #	utility[6] = cons_motor + 
    #           beta_tt_motor* tt_motor_all + 
    #	        beta_cost * cost_motor + 
    #           beta_central_motor * CBD + 
    #	        beta_parttime_motor * parttime +
    #	        beta_female_motor * female +
    #	        beta_TRANS_motor * TRANS + 
    #           beta_LIC_motor * LIC +
    #           beta_zerocar_motor * zerocar +
    #	        beta_onecar_motor * onecar + 
    #           beta_twocar_motor * twocar +
    #	        beta_threepluscar_motor * threepluscar +
    #	        beta_preschool_motor * preschool +
    #	        beta_undergraduate_motor * undergraduate 


        self.u_motorcycle_driver=Utility("Motorcycle",["1","tt_motor_all","cost_motor","CBD","parttime","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("cons_motor",0),Beta("beta_tt_motor",0),Beta("beta_cost",0),Beta("beta_central_motor",0),Beta("beta_parttime_motor",0),Beta("beta_female_motor",0),Beta("beta_TRANS_motor",0),Beta("beta_LIC_motor",0),
        Beta("beta_zerocar_motor",0),Beta("beta_onecar_motor",0),Beta("beta_twocar_motor",0),Beta("beta_threepluscar_motor",0),Beta("beta_preschool_motor",0),Beta("beta_undergraduate_motor",0)])


#        utility[7] = cons_walk  + 
#                   beta_tt_walk * tt_walk + 
#                   beta_central_walk * CBD+ 
#                   beta_parttime_walk * parttime +
#                   beta_female_walk * female +
#                   beta_TRANS_walk * TRANS + 
#                   beta_LIC_walk * LIC +
#                   beta_zerocar_walk * zerocar +
#                   beta_onecar_walk * onecar + 
#                   beta_twocar_walk * twocar +
#                   beta_threepluscar_walk * threepluscar +
#                   beta_preschool_walk * preschool +
#                   beta_undergraduate_walk * undergraduate 

        self.u_walk=Utility("Walk",["1","tt_walk","CBD","parttime","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("cons_walk",0),Beta("beta_tt_walk",0),Beta("beta_central_walk",0),Beta("beta_parttime_walk",0),Beta("beta_female_walk",0),Beta("beta_TRANS_walk",0),Beta("beta_LIC_walk",0),Beta("beta_zerocar_walk",0),
        Beta("beta_onecar_walk",0),Beta("beta_twocar_walk",0),Beta("beta_threepluscar_walk",0),Beta("beta_preschool_walk",0),Beta("beta_undergraduate_walk",0)])


#         utility[8] = cons_bike + 
#                      beta_tt_bike * tt_bike + 
#                      beta_central_bike * CBD + 
#                      beta_female_bike * female +
#                      beta_TRANS_bike * TRANS + 
#                      beta_LIC_bike * LIC +
#                      beta_zerocar_bike * zerocar +
#                      beta_onecar_bike * onecar + 
#                      beta_twocar_bike * twocar +
#                      beta_threepluscar_bike * threepluscar +
#                      beta_preschool_bike * preschool +
#                      beta_undergraduate_bike * undergraduate



        self.u_bike=Utility("Bike",["1","tt_bike","CBD","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("cons_bike",0),Beta("beta_tt_bike",0),Beta("beta_central_bike",0),Beta('beta_female_bike',0),Beta('beta_TRANS_bike',0),Beta('beta_LIC_bike',0),Beta('beta_zerocar_bike',0),Beta('beta_onecar_bike',0),
        Beta('beta_onecar_bike',0),Beta('beta_twocar_bike',0),Beta('beta_threepluscar_bike',0),Beta('beta_preschool_bike',0),Beta('beta_undergraduate_bike',0)])




#         utility[9] = cons_MRT + 
#                    beta_tt_MRT * tt_mrt_all +
#                    beta_cost * cost_mrt + 
#                    beta_central_MRT * CBD + 
#                    beta_parttime_MRT * parttime +
#                    beta_female_MRT * female +
#                    beta_TRANS_MRT * TRANS + 
#                    beta_LIC_MRT * LIC +
#                    beta_zerocar_MRT * zerocar +
#                    beta_onecar_MRT * onecar + 
#                    beta_twocar_MRT * twocar +
#                    beta_threepluscar_MRT * threepluscar +
#                    beta_preschool_MRT * preschool +
#                    beta_undergraduate_MRT * undergraduate 



        self.u_mrt=Utility("MRT",["1","tt_mrt_all","cost_mrt","CBD","parttime","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("cons_MRT",0),Beta("beta_tt_MRT",0),Beta("beta_cost",0),Beta("beta_central_MRT",0),Beta("beta_parttime_MRT",0),Beta('beta_female_MRT',0),Beta('beta_TRANS_MRT',0),Beta('beta_LIC_MRT',0),
        Beta('beta_zerocar_MRT',0),Beta('beta_onecar_MRT',0),Beta('beta_twocar_MRT',0),Beta('beta_threepluscar_MRT',0),Beta('beta_preschool_MRT',0),Beta('beta_undergraduate_MRT',0)])




    def get_function_for_mode(self, mode):
        
        mode_to_function_name = {
            "BusTravel": "u_bus_driver",
            "PrivateBus": "u_private_bus_driver",
            "Car": "u_car_driver",
            "Car_Sharing_2": "u_car_sharing_2_driver",
            "Car_Sharing_3": "u_car_sharing_3_driver",
            "Motorcycle": "u_motorcycle_driver",
            "Walk": "u_walk",
            "Bike": "u_bike",
            "MRT": "u_mrt"
        }

        function_name = mode_to_function_name.get(mode)
        return getattr(self, function_name, None)


    def load_beta_variables(self, file_path):
        with open(file_path, 'r') as json_file:
            self.beta_varibales = json.load(json_file)
        self.update_utilities()
  


    def update_utilities(self):
        if not self.beta_varibales:
            raise ValueError("Beta variables are not loaded!")
        for mode in self.Modes:
            function = self.get_function_for_mode(mode)
            beta_list=function.get_betas_list()
            for beta in beta_list:

                updated_value = None
                if beta.beta in self.beta_varibales:
                    updated_value = self.beta_varibales[beta.beta]
                else:
                    for category, values in self.beta_varibales.items():
                        if isinstance(values, dict) and beta.beta in values:
                            updated_value = values[beta.beta]
                            break
                if updated_value is not None:
                    beta.value = updated_value
                else:
                    print(f"Warning: {beta.beta} not found in beta variables. Keeping the default value.")


    def generate_lua(self,file_path):
            
            lua_variables = []
            lua_lines = []


            ####### Local varibales Here ########

            json_data=self.beta_varibales
            if "beta_cost" in json_data:
                    lua_variables.append(f"local beta_cost = {json_data['beta_cost']}")

            lua_variables.append("\n"* 1)

            if "constants" in json_data:
                    for key, value in json_data["constants"].items():
                        lua_variables.append(f"local {key} = {value}")

            lua_variables.append("\n"* 1)

            for category, coefficients in json_data.items():
                    if category.endswith("_coefficients"):
                        for key, value in coefficients.items():
                            lua_variables.append(f"local {key} = {value}")
                    lua_variables.append("\n"* 1)


            lua_lines.extend(lua_variables)
            lua_lines.append("\n"* 5)

            ####### Utility functions for each mode ########
            for mode, mode_index in self.Modes.items():
                utility_function = self.get_function_for_mode(mode)
                equation_parts = []
                for beta, variable in zip(utility_function.betas, utility_function.varibales):
                         equation_parts.append(f"{beta.beta} * {variable}")
                lua_equation = " + ".join(equation_parts)
                lua_equation = " +\n".join(equation_parts)


                lua_lines.append(f"utility[{mode_index}] = {lua_equation}")
                lua_lines.append("\n" * 5)

           



            lua_script = "\n".join(lua_lines)
            self.save_to_file(lua_script, file_path)
            return lua_script


    def save_to_file(self, content, file_path):

            with open(file_path, "w") as lua_file:
                lua_file.write(content)
            print(f"Lua file saved to: {file_path}")