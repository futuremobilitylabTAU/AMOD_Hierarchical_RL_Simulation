
from models.Utility import Utility,Beta

class TME:
    def __init__(self):


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


        self.u_bus_driver=Utility("BusTravel",["cons_PT","tt_bus_ivt + tt_bus_walk + tt_bus_wait","cost_bus","CBD","parttime","female","TRANS",
        "LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("beta_cons_PT",1),Beta("beta_tt_PT",0),Beta("beta_cost",0),Beta("beta_central_PT",0),Beta("beta_parttime_PT",0),
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


        self.u_private_bus_driver=Utility("PrivateBus",["cons_PB","tt_privatebus_all","CBD",'parttime','female',
                                               'TRANS','LIC','zerocar','onecar','twocar','threepluscar','preschool','undergraduate'],
                                               [Beta("beta_cons_PB",1),Beta("beta_tt_PT",0),Beta("beta_central_PT",0),Beta("beta_parttime_PT",0),
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





        self.u_car_driver=Utility("Car",["cons_drive1","tt_cardriver_all","cost_cardriver","CBD","parttime","female","TRANS","LIC","zerocar",
        "onecar","twocar","threepluscar","preschool","undergraduate"],[Beta("beta_cons_drive1",1),Beta("beta_tt_drive1",0),Beta("beta_cost",0)
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


        self.u_car_sharing_2_driver=Utility("Car_Sharing_2",["cons_share2","tt_carpassenger_all","cost_carpassenger/2.0","CBD","parttime","female","TRANS","LIC","zerocar",
        "onecar","twocar","threepluscar","preschool","undergraduate"],[Beta("beta_cons_share2",1),Beta("beta_tt_share2",0),Beta("beta_cost",0),Beta("beta_central_share2",0),
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


        self.u_car_sharing_3_driver=Utility("Car_Sharing_3",["cons_share3","tt_carpassenger_all","cost_carpassenger/3.0","CBD","parttime","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar",
        "preschool","undergraduate"],[Beta("beta_cons_share3",1),Beta("beta_tt_share3",0),Beta("beta_cost",0),Beta("beta_central_share3",0),Beta("beta_parttime_share3",0),Beta("beta_female_share3",0),Beta("beta_TRANS_share3",0),
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


        self.u_motorcycle_driver=Utility("Motorcycle",["cons_motor","tt_motor_all","cost_motor","CBD","parttime","female","TRANS","LIC","zerocar","onecar","twocar","threepluscar","preschool","undergraduate"],
        [Beta("beta_cons_motor",1),Beta("beta_tt_motor",0),Beta("beta_cost",0),Beta("beta_central_motor",0),Beta("beta_parttime_motor",0),Beta("beta_female_motor",0),Beta("beta_TRANS_motor",0),Beta("beta_LIC_motor",0),
        Beta("beta_zerocar_motor",0),Beta("beta_onecar_motor",0),Beta("beta_twocar_motor",0),Beta("beta_threepluscar_motor",0),Beta("beta_preschool_motor",0),Beta("beta_undergraduate_motor",0)])


        self.u_walk=0
        self.u_bike=0
        self.u_mrt=0
        