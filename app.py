from flask import Flask, request,Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
from os import environ

from models import *

from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://'+os.getenv('DB_USERNAME')+':'+os.getenv('DB_PASSWORD')+'@'+os.getenv('DB_Server')+'/'+os.getenv('DB_NAME')+'?driver=ODBC+Driver+17+for+SQL+Server'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/sync/facility' ,methods = ['POST', 'GET'])
def sync_facility():  # put application's code here
    content = request.json
    # print(content)
    db.session.query(All_EMRSites).filter_by(MFL_Code=str(content["mfl_code"])).delete()
    db.session.commit()

    user = All_EMRSites(MFL_Code= str(content["mfl_code"]), Facility_Name= content["FacilityName"], County= content["County"],
                        SubCounty= content["SubCounty"], Owner= str(content["Owner"]), Latitude= str(content["lat"]),
                        Longitude= str(content["lon"]), SDP= content["SDP"], SDP_Agency= content["Agency"],
                        Implementation= content["implementation"], EMR= content["EMR"], EMR_Status= content["EMR Status"],
                        HTS_Use= content["HTS Use"], HTS_Deployment= content["HTS Deployment"], HTS_Status= content["HTS Status"],
                        IL_Status= content["IL Status"], Registration_IE= content["registration ie"], Phamarmacy_IE= content["pharmacy ie"],
                        mlab= content["Mlab"], Ushauri= content["Ushauri"],Nishauri= content["Nishauri"],
                        Appointment_Management_IE= "", OVC= content["ovc"], OTZ= content["otz"],
                        PrEP= content["prep"], three_PM= content["three_PM"], AIR= content["air"], KP= content["kp"], MCH= content["mnch"],
                        TB= content["tb"], Lab_Manifest= content["lab_manifest"], Comments= "", Project= "KenyaHMIS III")
    db.session.add(user)
    db.session.commit()

    emrsdata = db.session.query(All_EMRSites).all()
    print(f'============ Facility Synced {str(content["mfl_code"])} {content["FacilityName"]} ============ ')
    return f'============ success ============ '


@app.route('/sync/full/list/facilities/emrs' ,methods = ['POST', 'GET'])
def sync_facilities_emrs():  # put application's code here
    contents = request.json
    #clear table first
    db.session.query(All_EMRSites).delete()
    db.session.commit()

    for content in contents:
        user = All_EMRSites(MFL_Code= str(content["mfl_code"]), Facility_Name= content["FacilityName"], County= content["County"],
                            SubCounty= content["SubCounty"], Owner= str(content["Owner"]), Latitude= str(content["lat"]),
                            Longitude= str(content["lon"]), SDP= content["SDP"], SDP_Agency= content["Agency"],
                            Implementation= content["implementation"], EMR= content["EMR"], EMR_Status= content["EMR Status"],
                            HTS_Use= content["HTS Use"], HTS_Deployment= content["HTS Deployment"], HTS_Status= content["HTS Status"],
                            IL_Status= content["IL Status"], Registration_IE= content["registration ie"], Phamarmacy_IE= content["pharmacy ie"],
                            mlab= content["Mlab"], Ushauri= content["Ushauri"],Nishauri= content["Nishauri"],
                            Appointment_Management_IE= "", OVC= content["ovc"], OTZ= content["otz"],
                            PrEP= content["prep"], three_PM= content["three_PM"], AIR= content["air"], KP= content["kp"], MCH= content["mnch"],
                            TB= content["tb"], Lab_Manifest= content["lab_manifest"], Comments= "", Project= "KenyaHMIS III")
        db.session.add(user)
        db.session.commit()

    emrsdata = db.session.query(All_EMRSites).count()
    print(f'============ ++++ Facilities Synced {emrsdata} count ++++ ============ ')
    return f'============ success ============ '


if __name__ == '__main__':
    app.run(debug=True)

