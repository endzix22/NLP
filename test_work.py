import pandas as pd

runlog_id_runlog_by_mpn = pd.read_csv('C:/Users/tczanjan/Downloads/runlog_id_runlog_by_mpn.csv')
df_cust_control = runlog_id_runlog_by_mpn[runlog_id_runlog_by_mpn['OWNERSHIP'].isin(['CCP', 'CFP', 'CGP', 'PLUG-IN PRICE'])]
nan_cust_control = df_cust_control[df_cust_control['RECOMMENDED_PRICE_MCE_CL'].isna()]
nan_cust_control_quantity = nan_cust_control.groupby('QW_PROJECT_ID')['PART_QUANTITY'].sum().reset_index()
nan_cust_control_quantity.columns = ['QW_PROJECT_ID', 'PART_QUANTITY_with_NA']
#x_controlled_resistor', 'QW_PROJECT_ID']]