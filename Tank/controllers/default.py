# -*- coding: utf-8 -*-
import smbus
from gluon.tools import Crud
crud = Crud(db)
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call():
    session.forget()
    return service()
### end requires
def index():
    return dict()
    
def error():
    return dict()
    
def graphs():
    return dict()   
    
def graphdata():
    for row in db(db.wtemp.id=='1').select():
        data1= row.wtemp  
    return data1

@auth.requires_login()    
def config():
   return dict(form=crud.update(db.waterset, 1, deletable=False)
   , form1=crud.update(db.tempset1, 1, deletable=False ))
    
def tempset():
    for row in db(db.waterset.id=='1').select():
        tempset= row.Water_Temperature
    return tempset
    
def tempset1():
    for row in db(db.tempset1.id=='1').select():
        tempset1= row.Light_Temperature
    return tempset1
    
def temp():
    for row in db(db.wtemp.id=='1').select():
        temp= row.wtemp  
    return temp
    
def temp1():
    bus = smbus.SMBus(1)
    address = 0x48
    temp1 = bus.read_byte_data(address, 0)
    temp1 = round(temp1, 1)
    return temp1
    
def heat():
    for row in db(db.heat.id=='1').select():
        heat= row.heat 
    return heat
