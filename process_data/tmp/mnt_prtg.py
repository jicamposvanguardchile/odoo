import os
import time
import datetime
import pytz
import re

#path = '/odoo/custom/prtg_reports/'
#path = '../static/tmpdata/device_40_img.29222.png'
path = '/odoo/custom/prtg_reports/static/tmpdata'
#path = '/static/tmpdata/'

ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)

print(ti_c)
print(ti_m)

c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)

print(c_ti)
print(m_ti)

#_tz   = self.env['res.config.settings'].sudo().get_values()['prtg_tz']
#today = datetime.now(pytz.timezone(_tz))
today = datetime.datetime.now(pytz.timezone('America/Santiago'))

#today = datetime.datetime.utcnow()

print('hoy: %s'%(today))
ayer = today - datetime.timedelta(days=30)
print('ayer: %s'%(ayer))

contenido = os.listdir(path)
print('Archivos: %s'%(contenido))

for file in contenido:
    r = re.search("^device_[0-9]+_img", file)
    if r:
        #return r.group(rgx.value_id), r.group(rgx.uom_id), rgx.separator
        print("%s :  %s  %s"%(r,file,os.path.abspath(file)))
        #os.remove()

