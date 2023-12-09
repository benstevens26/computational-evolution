import analysis

file_path = r"C:\Users\alyss\OneDrive\Documents\Year 3 Physics\Project Data\data\no_pred"

dataframes = analysis.import_data(file_path)
print('data imported')

# df_data1 = dataframes['agent_data_evo_1']
# df_pop1 = dataframes['pop_data_evo_1']
# df_pred1 = dataframes['predator_data_evo_1']
# df_data1.to_pickle('d1.pkl')
# df_pop1.to_pickle('p1.pkl')
# df_pred1.to_pickle('pr1.pkl')
#
# df_data2 = dataframes['agent_data_evo_2']
# df_pop2 = dataframes['pop_data_evo_2']
# df_pred2 = dataframes['predator_data_evo_2']
# df_data2.to_pickle('d2.pkl')
# df_pop2.to_pickle('p2.pkl')
# df_pred2.to_pickle('pr2.pkl')
#
# df_data3 = dataframes['agent_data_evo_3']
# df_pop3 = dataframes['pop_data_evo_3']
# df_pred3 = dataframes['predator_data_evo_3']
# df_data3.to_pickle('d3.pkl')
# df_pop3.to_pickle('p3.pkl')
# df_pred3.to_pickle('pr3.pkl')

df_data_prey_1 = dataframes['agent_data_no_pred_1']
df_pop_prey_1 = dataframes['pop_data_no_pred_1']
df_data_prey_1.to_pickle('d_nop1.pkl')
df_pop_prey_1.to_pickle('p_nop1.pkl')

df_data_prey_2 = dataframes['agent_data_no_pred_2']
df_pop_prey_2 = dataframes['pop_data_no_pred_2']
df_data_prey_2.to_pickle('d_nop2.pkl')
df_pop_prey_2.to_pickle('p_nop2.pkl')

df_data_prey_3 = dataframes['agent_data_no_pred_3']
df_pop_prey_3 = dataframes['pop_data_no_pred_3']
df_data_prey_3.to_pickle('d_nop3.pkl')
df_pop_prey_3.to_pickle('p_nop3.pkl')

# df_data4 = dataframes['agent_data_evo_4']
# df_pop4 = dataframes['pop_data_evo_4']
# df_pred4 = dataframes['predator_data_evo_4']
# df_data4.to_pickle('d4.pkl')
# df_pop4.to_pickle('p4.pkl')
# df_pred4.to_pickle('pr4.pkl')
#
# df_data5 = dataframes['agent_data_evo_0']
# df_pop5 = dataframes['pop_data_evo_0']
# df_pred5 = dataframes['predator_data_evo_0']
# df_data5.to_pickle('d5.pkl')
# df_pop5.to_pickle('p5.pkl')
# df_pred5.to_pickle('pr5.pkl')

# df_data6 = dataframes['agent_data_evo_5']
# df_pop6 = dataframes['pop_data_evo_5']
# df_pred6 = dataframes['predator_data_evo_5']
# df_data6.to_pickle('d6.pkl')
# df_pop6.to_pickle('p6.pkl')
# df_pred6.to_pickle('pr6.pkl')

# df_data7 = dataframes['agent_data_evo_6']
# df_pop7 = dataframes['pop_data_evo_6']
# df_pred7 = dataframes['predator_data_evo_6']
# df_data7.to_pickle('d7.pkl')
# df_pop7.to_pickle('p7.pkl')
# df_pred7.to_pickle('pr7.pkl')
#
# df_data8 = dataframes['agent_data_evo_7']
# df_pop8 = dataframes['pop_data_evo_7']
# df_pred8 = dataframes['predator_data_evo_7']
# df_data8.to_pickle('d8.pkl')
# df_pop8.to_pickle('p8.pkl')
# df_pred8.to_pickle('pr8.pkl')
#
# df_data9 = dataframes['agent_data_evo_9']
# df_pop9 = dataframes['pop_data_evo_9']
# df_pred9 = dataframes['predator_data_evo_9']
# df_data9.to_pickle('d9.pkl')
# df_pop9.to_pickle('p9.pkl')
# df_pred9.to_pickle('pr9.pkl')
#
# df_data10 = dataframes['agent_data_evo_9']
# df_pop10 = dataframes['pop_data_evo_9']
# df_pred10 = dataframes['predator_data_evo_9']
# df_data10.to_pickle('d10.pkl')
# df_pop10.to_pickle('p10.pkl')
# df_pred10.to_pickle('pr10.pkl')
