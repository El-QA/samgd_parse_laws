# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
import requests

url = "http://opendata.samgd.ru/api/laws/"
cols = ["Basic Law", "Bill Number", "Duma Adoption Date", "Effective Date", "Id Law", "Law Full Name", "Law Number",
        "Publication Date", "Signed By Governor Date", "Law Url", "Smi Id", "Smi Title", "Theme Block Id",
        "Theme Block Id"]
rows = []

# Get xml data from link
response = requests.get(url)

# Parsing the XML file
laws = Xet.fromstring(response.content)
for law in laws.findall("./Law"):
    basic_law = law.find("BasicLaw").text
    bill_number = law.find("BillNumber").text
    duma_adoption_date = law.find("DumaAdoptionDate").text
    effective_date = law.find("EffectiveDate").text
    id_law = law.find("Id").text
    law_full_name = law.find("LawFullName").text
    law_number = law.find("LawNumber").text
    publication_date = law.find("PublicationDate").text
    signed_by_governor_date = law.find("SignedByGovernorDate").text
    law_url = law.find("Url").text

    for smi_info in law.findall("./Smi"):
        smi_id = smi_info.find("Id").text
        smi_title = smi_info.find("Title").text

    for theme_info in law.findall("./ThemeBlock"):
        theme_id = theme_info.find("Id").text
        theme_title = theme_info.find("Title").text

    rows.append({"Basic Law": basic_law,
                 "Bill Number": bill_number,
                 "Duma Adoption Date": duma_adoption_date,
                 "Effective Date": effective_date,
                 "Id Law": id_law,
                 "Law Full Name": law_full_name,
                 "Law Number": law_number,
                 "Publication Date": publication_date,
                 "Signed By Governor Date": signed_by_governor_date,
                 "Law Url": law_url,
                 "Smi Id": smi_id,
                 "Smi Title": smi_title,
                 "Theme Block Id": theme_id,
                 "Theme Block Title": theme_title})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')
