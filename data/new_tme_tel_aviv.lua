local beta_cost = -0.0432


local cons_walk = 1.75
local cons_bike = -2.2
local cons_drive1 = 1.25
local cons_share2 = 1.75
local cons_share3 = 1.3
local cons_PT = -2.71
local cons_PB = -0.75
local cons_motor = 3.2
local cons_MRT = 0






local beta_tt_walk = -4.884
local beta_tt_bike = -4.188
local beta_tt_drive1 = -2.844
local beta_tt_share2 = -3.594
local beta_tt_share3 = -3.702
local beta_tt_PT = -0.2616
local beta_tt_motor = -4.188
local beta_tt_MRT = -0.2616


local beta_central_walk = 2.49
local beta_central_bike = 1.5
local beta_central_drive1 = 0
local beta_central_share2 = 0
local beta_central_share3 = 0
local beta_central_PT = 2.12
local beta_central_motor = 0
local beta_central_MRT = 2.12


local beta_parttime_walk = 0
local beta_parttime_bike = 0
local beta_parttime_drive1 = 0
local beta_parttime_share2 = 0.522
local beta_parttime_share3 = -0.336
local beta_parttime_PT = -0.729
local beta_parttime_motor = 0
local beta_parttime_MRT = -0.729


local beta_preschool_walk = 0.617
local beta_preschool_bike = 0
local beta_preschool_drive1 = 0
local beta_preschool_share2 = 1.28
local beta_preschool_share3 = 1.4
local beta_preschool_PT = -0.736
local beta_preschool_motor = 0
local beta_preschool_MRT = -0.736


local beta_undergraduate_walk = 0
local beta_undergraduate_bike = 1.49
local beta_undergraduate_drive1 = 0
local beta_undergraduate_share2 = -0.457
local beta_undergraduate_share3 = -1.96
local beta_undergraduate_PT = 0
local beta_undergraduate_motor = 0
local beta_undergraduate_MRT = 0


local beta_female_walk = 0
local beta_female_bike = -1.27
local beta_female_drive1 = 0
local beta_female_share2 = 0
local beta_female_share3 = 0
local beta_female_PT = -0.314
local beta_female_motor = 0
local beta_female_MRT = -0.314


local beta_LIC_walk = 1.32
local beta_LIC_bike = 0
local beta_LIC_drive1 = 0
local beta_LIC_share2 = 1.46
local beta_LIC_share3 = 0
local beta_LIC_PT = 0
local beta_LIC_motor = 0
local beta_LIC_MRT = 0


local beta_TRANS_walk = 1.26
local beta_TRANS_bike = 0
local beta_TRANS_drive1 = 0
local beta_TRANS_share2 = 0
local beta_TRANS_share3 = 0
local beta_TRANS_PT = 1.2
local beta_TRANS_motor = 0
local beta_TRANS_MRT = 1.2


local beta_zerocar_walk = 0
local beta_zerocar_bike = 1.05
local beta_zerocar_drive1 = 0
local beta_zerocar_share2 = -1.2
local beta_zerocar_share3 = 0
local beta_zerocar_PT = 0.761
local beta_zerocar_motor = 0
local beta_zerocar_MRT = 0.761


local beta_onecar_walk = 1.13
local beta_onecar_bike = 1.4
local beta_onecar_drive1 = 0
local beta_onecar_share2 = 0.272
local beta_onecar_share3 = 0.843
local beta_onecar_PT = 0.6
local beta_onecar_motor = 0
local beta_onecar_MRT = 0.6


local beta_twocar_walk = 0.36
local beta_twocar_bike = 0.767
local beta_twocar_drive1 = 0
local beta_twocar_share2 = 0.459
local beta_twocar_share3 = 1.08
local beta_twocar_PT = 0.376
local beta_twocar_motor = 0
local beta_twocar_MRT = 0.376


local beta_threepluscar_walk = 0
local beta_threepluscar_bike = 0
local beta_threepluscar_drive1 = 0
local beta_threepluscar_share2 = 0
local beta_threepluscar_share3 = 0
local beta_threepluscar_PT = 0
local beta_threepluscar_motor = 0
local beta_threepluscar_MRT = 0








utility[1] = cons_PT * 1 +
beta_tt_PT * (tt_bus_ivt + tt_bus_walk + tt_bus_wait) +
beta_cost * cost_bus +
beta_central_PT * CBD +
beta_parttime_PT * parttime +
beta_female_PT * female +
beta_TRANS_PT * TRANS +
beta_LIC_PT * LIC +
beta_zerocar_PT * zerocar +
beta_onecar_PT * onecar +
beta_twocar_PT * twocar +
beta_threepluscar_PT * threepluscar +
beta_preschool_PT * preschool +
beta_undergraduate_PT * undergraduate






utility[2] = cons_PB * 1 +
beta_tt_PT * tt_privatebus_all +
beta_central_PT * CBD +
beta_parttime_PT * parttime +
beta_female_PT * female +
beta_TRANS_PT * TRANS +
beta_LIC_PT * LIC +
beta_zerocar_PT * zerocar +
beta_onecar_PT * onecar +
beta_twocar_PT * twocar +
beta_threepluscar_PT * threepluscar +
beta_preschool_PT * preschool +
beta_undergraduate_PT * undergraduate






utility[3] = cons_drive1 * 1 +
beta_tt_drive1 * tt_cardriver_all +
beta_cost * cost_cardriver +
beta_central_drive1 * CBD +
beta_parttime_drive1 * parttime +
beta_female_drive1 * female +
beta_TRANS_drive1 * TRANS +
beta_LIC_drive1 * LIC +
beta_zerocar_drive1 * zerocar +
beta_onecar_drive1 * onecar +
beta_twocar_drive1 * twocar +
beta_threepluscar_drive1 * threepluscar +
beta_preschool_drive1 * preschool +
beta_undergraduate_drive1 * undergraduate






utility[4] = cons_share2 * 1 +
beta_tt_share2 * tt_carpassenger_all +
beta_cost * cost_carpassenger/2.0 +
beta_central_share2 * CBD +
beta_parttime_share2 * parttime +
beta_female_share2 * female +
beta_TRANS_share2 * TRANS +
beta_LIC_share2 * LIC +
beta_zerocar_share2 * zerocar +
beta_onecar_share2 * onecar +
beta_twocar_share2 * twocar +
beta_threepluscar_share2 * threepluscar +
beta_preschool_share2 * preschool +
beta_undergraduate_share2 * undergraduate






utility[5] = cons_share3 * 1 +
beta_tt_share3 * tt_carpassenger_all +
beta_cost * cost_carpassenger/3.0 +
beta_central_share3 * CBD +
beta_parttime_share3 * parttime +
beta_female_share3 * female +
beta_TRANS_share3 * TRANS +
beta_LIC_share3 * LIC +
beta_zerocar_share3 * zerocar +
beta_onecar_share3 * onecar +
beta_twocar_share3 * twocar +
beta_threepluscar_share3 * threepluscar +
beta_preschool_share3 * preschool +
beta_undergraduate_share3 * undergraduate






utility[6] = cons_motor * 1 +
beta_tt_motor * tt_motor_all +
beta_cost * cost_motor +
beta_central_motor * CBD +
beta_parttime_motor * parttime +
beta_female_motor * female +
beta_TRANS_motor * TRANS +
beta_LIC_motor * LIC +
beta_zerocar_motor * zerocar +
beta_onecar_motor * onecar +
beta_twocar_motor * twocar +
beta_threepluscar_motor * threepluscar +
beta_preschool_motor * preschool +
beta_undergraduate_motor * undergraduate






utility[7] = cons_walk * 1 +
beta_tt_walk * tt_walk +
beta_central_walk * CBD +
beta_parttime_walk * parttime +
beta_female_walk * female +
beta_TRANS_walk * TRANS +
beta_LIC_walk * LIC +
beta_zerocar_walk * zerocar +
beta_onecar_walk * onecar +
beta_twocar_walk * twocar +
beta_threepluscar_walk * threepluscar +
beta_preschool_walk * preschool +
beta_undergraduate_walk * undergraduate






utility[8] = cons_bike * 1 +
beta_tt_bike * tt_bike +
beta_central_bike * CBD +
beta_female_bike * female +
beta_TRANS_bike * TRANS +
beta_LIC_bike * LIC +
beta_zerocar_bike * zerocar +
beta_onecar_bike * onecar +
beta_onecar_bike * twocar +
beta_twocar_bike * threepluscar +
beta_threepluscar_bike * preschool +
beta_preschool_bike * undergraduate






utility[9] = cons_MRT * 1 +
beta_tt_MRT * tt_mrt_all +
beta_cost * cost_mrt +
beta_central_MRT * CBD +
beta_parttime_MRT * parttime +
beta_female_MRT * female +
beta_TRANS_MRT * TRANS +
beta_LIC_MRT * LIC +
beta_zerocar_MRT * zerocar +
beta_onecar_MRT * onecar +
beta_twocar_MRT * twocar +
beta_threepluscar_MRT * threepluscar +
beta_preschool_MRT * preschool +
beta_undergraduate_MRT * undergraduate





