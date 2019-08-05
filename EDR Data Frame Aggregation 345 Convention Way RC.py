#EDR Data Frame Aggregation 1165 65th St, Oakland
import pandas as pd

edr = pd.read_csv(r'C:\Users\zsham\Desktop\Pywork\Data\345_Convention_Report_CSV.csv')
pd.set_option('display.max_columns', None)

#Fixing column names by removing whitespace
edr.columns = [col.strip('    ') for col in edr.columns]

#creating a df of subject site listings
tp_df = edr[edr['DIST'] == 0]
print(tp_df)

#Adjacent Listings (30 foot radius)
adj_df = edr[(edr.DIST > 0) & (edr.DIST < 100)]
print(adj_df)

#Petroleum Hydocarbon/MBTEX LUST Case DF (528 Foot Radius)
lust_df = edr[(edr['DB NAME'] == 'LUST') & (edr.DIST <= 528)]
lust_grouped = lust_df.groupby(['FACILITY','STREET', 'DB NAME']).DIST.mean().reset_index()
lust = lust_grouped.sort_values('DIST', ascending=True).reset_index()
print(lust)

#Chlorinated Solvents SLIC Case DF (1760 Foot Radius)
slic_df = edr[(edr['DB NAME'] == 'CPS-SLIC') & (edr.DIST <= 1760)]
slic_grouped = slic_df.groupby(['FACILITY','STREET', 'DB NAME']).DIST.mean().reset_index()
slic = slic_grouped.sort_values('DIST', ascending=True).reset_index()
print(slic)

#Export Data Frames to Excel Sheets
with pd.ExcelWriter('Site Info 345 Convention.xlsx') as writer:
     tp_df.to_excel(writer, sheet_name='Subject Site')
     adj_df.to_excel(writer, sheet_name='Adjacent Sites')
     lust.to_excel(writer, sheet_name='LUST Sites')
     slic.to_excel(writer, sheet_name='SLIC Sites')