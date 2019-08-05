# Site-Report-Code
Aggregating and Filtering Important Info from EDR

The purpose of this script is to take an Environmental Database Resources (EDR) Report and extract the useful information to an Environmental Consultant conducting a Phase I ESA or Environmental Transaction Screen.

An EDR report is a large excel spreadsheet or CSV doc, typically 600-1000 rows long, detailing which properties within a 1-mile radius of a given address are listed on standard environmental databases (Haznet, LUST, SLIC, EMI, etc.). An environmental consultant can parse this info and extract relevant information from this data dump to gather insights on the subsurface conditions on and around a given site. This script was written to expedite that process by quickly extracting the most relevant info.

The output of this script is an excel spreadsheet consisting of four dataframes that have been converted to excel sheets named Subject Site, Adjacent Sites, LUST Sites and SLIC Sites. Subject Site contains a table of all listing for the project address, Adjacent Site contains a table of all listing for the addresses adjacent to the project adress, LUST Sites contains all LUST cases within a 
