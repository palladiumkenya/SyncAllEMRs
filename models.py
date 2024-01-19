from app import db
#from sqlalchemy_utils import ScalarListType
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql.base import UUID
db.UUID = UUID




class All_EMRSites(db.Model):
    __tablename__ = 'All_EMRSites'

    MFL_Code = db.Column(db.String(100), nullable=False, primary_key=True)
    Facility_Name = db.Column('Facility_Name', db.String(100), nullable=False)
    County = db.Column(db.String(100), nullable=False)
    SubCounty = db.Column(db.String(100), nullable=False)
    Owner = db.Column(db.String(100), nullable=False)
    Latitude = db.Column(db.String(100), nullable=False)
    Longitude = db.Column(db.String(100), nullable=False)
    SDP = db.Column(db.String(100), nullable=False)
    SDP_Agency = db.Column('SDP_Agency',db.String(100), nullable=False)
    Implementation = db.Column(db.String(100), nullable=False)
    EMR = db.Column(db.String(100), nullable=False)
    EMR_Status = db.Column('EMR_Status',db.String(100), nullable=False)
    HTS_Use = db.Column('HTS_Use', db.String(100), nullable=False)
    HTS_Deployment = db.Column('HTS_Deployment', db.String(100), nullable=False)
    HTS_Status = db.Column('HTS_Status', db.String(100), nullable=False)
    # IL_Status = db.Column('IL Status',db.String(100), nullable=False)
    # Registration_IE = db.Column('Registration IE',db.String(100), nullable=False)
    # Phamarmacy_IE = db.Column('Phamarmacy IE',db.String(100), nullable=False)
    mlab = db.Column(db.String(100), nullable=False)
    Ushauri = db.Column(db.String(100), nullable=False)
    Nishauri = db.Column(db.String(100), nullable=False)
    # Appointment_Management_IE = db.Column('Appointment Management IE', db.String(100), nullable=False)
    OVC = db.Column(db.String(100), nullable=False)
    OTZ = db.Column(db.String(100), nullable=False)
    PrEP = db.Column(db.String(100), nullable=False)
    # three_PM = db.Column('3PM',db.String(100), nullable=False)
    AIR = db.Column(db.String(100), nullable=False)
    KP = db.Column(db.String(100), nullable=False)
    MCH = db.Column(db.String(100), nullable=False)
    # TB = db.Column(db.String(100), nullable=False)
    Lab_Manifest = db.Column('Lab_Manifest',db.String(100), nullable=False)
    Comments = db.Column(db.String(100), nullable=False)
    Project = db.Column(db.String(100), nullable=False)
    EMRType = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Facility_Name {self.Facility_Name}>'