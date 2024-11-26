from flask import Flask, request,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
from os import environ
from urllib.parse import quote_plus

from models import *

from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

for variable, value in os.environ.items():
    app.config[variable] = value

app.secret_key = os.getenv("SECRET_KEY")

basedir = os.path.abspath(os.path.dirname(__file__))

user =os.getenv('DB_USERNAME')
dbpass = os.getenv('DB_PASSWORD')
server =os.getenv('DB_SERVER')
dbname = os.getenv('DB_NAME')
print("===>",user,dbname,dbpass,server)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://{user}:%s@{server}/{dbname}?driver=ODBC+Driver+17+for+SQL+Server' % quote_plus(dbpass)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/' ,methods = ['GET'])
def default():  # put application's code here
    return '{ status:200, version:1.00, success: Sync App running }'


@app.route('/sync/allsites' ,methods = ['GET'])
def allsites():
    res = db.session.query(All_EMRSites).all()
    allsites=[]
    # for i in res:
    #     resObj = {}
    #     res["MFL_Code"] = i[0]
    #     allsites.append(resObj)
    print(res)
    return ""


@app.route('/sync/facility' ,methods = ['POST'])
def sync_facility():  # put application's code here
    content = request.json
    # print(content)
    db.session.query(All_EMRSites).filter_by(MFL_Code=str(content["mfl_code"])).delete()
    db.session.commit()

    user = All_EMRSites(MFL_Code= str(content["mfl_code"]), Facility_Name= content["Facility_Name"], County= content["County"],
                        SubCounty= content["SubCounty"], Owner= str(content["Owner"]), Latitude= str(content["Latitude"]),
                        Longitude= str(content["Longitude"]), SDP= content["SDP"], SDP_Agency= content["Agency"],
                        Implementation= content["implementation"], EMR= content["EMR"], EMR_Status= content["EMR_Status"],
                        HTS_Use= content["HTS_Use"], HTS_Deployment= content["HTS_Deployment"], HTS_Status= content["HTS_Status"],
                        IL_Status= content["IL_Status"],
                        mlab= content["Mlab"], Ushauri= content["Ushauri"],Nishauri= content["Nishauri"],
                        OVC= content["OVC"], OTZ= content["OTZ"],
                        PrEP= content["PrEP"], AIR= content["AIR"], KP= content["KP"], MCH= content["MCH"],
                        Lab_Manifest= content["Lab_Manifest"], Comments= "", Project= "KenyaHMIS III", EMRType=content["EMRType"])
    db.session.add(user)
    db.session.commit()

    emrsdata = db.session.query(All_EMRSites).all()
    print(f'============ Facility Synced {str(content["mfl_code"])} {content["FacilityName"]} ============ ')
    return f'============ success ============ '


@app.route('/sync/full/list/facilities/emrs' ,methods = ['POST'])
def sync_facilities_emrs():  # put application's code here
    try:
        contents = request.json
        #clear table first
        db.session.query(All_EMRSites).delete()
        db.session.commit()

        for content in contents:
            data = All_EMRSites(MFL_Code= str(content["mfl_code"]), Facility_Name= content["Facility_Name"], County= content["County"],
                            SubCounty= content["SubCounty"], Owner= str(content["Owner"]), Latitude= str(content["Latitude"]),
                            Longitude= str(content["Longitude"]), SDP= content["SDP"], SDP_Agency= content["Agency"],
                            Implementation= content["implementation"], EMR= content["EMR"], EMR_Status= content["EMR_Status"],
                            HTS_Use= content["HTS_Use"], HTS_Deployment= content["HTS_Deployment"], HTS_Status= content["HTS_Status"],
                            mlab= content["Mlab"], Ushauri= content["Ushauri"],Nishauri= content["Nishauri"],
                            OVC= content["OVC"], OTZ= content["OTZ"],InfrastructureType= content["InfrastructureType"], KEPH_Level= content["KEPH_Level"],
                            PrEP= content["PrEP"], AIR= content["AIR"], KP= content["KP"], MCH= content["MCH"],
                            Lab_Manifest= content["Lab_Manifest"], Comments= "", Project= "KenyaHMIS III", EMRType=content["EMRType"])

            db.session.add(data)
            db.session.commit()

        emrsdata = db.session.query(All_EMRSites).count()
        print(f'============ ++++ Facilities Synced {emrsdata} count ++++ ============ ')
        return jsonify({'status_code': 200,'status':'++++++++ SUCCESSFULLY SYNCED ++++++++!'})
    except Exception as e:
        message = e
        print("========== FAILED : SyncAllEMRs error => ", e)
        return jsonify({'status_code': 500,'status':"=== STATUS 500 === Failed to Sync! ==> Message: {}".format(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
