import re

tmpl_porcentaje = r'\s*(\d+,\d+|\d+)\s+(\%)\s*'

tmpl_rpm        = r'\s*(\d+,\d+|\d+)\s+(rpm)\s*'
tmpl_Vdc        = r'\s*(\d+,\d+|\d+)\s+(Vdc)\s*'
tmpl_Vac        = r'\s*(\d+,\d+|\d+)\s+(Vac)\s*'

tmpl_oF         = r'\s*(\d+)\s+(°F)\s*'
tmpl_oF_dot     = r'\s*(\d+.\d+)\s+(°F)\s*'
tmpl_oF_comma   = r'\s*(\d+,\d+)\s+(°F)\s*'

tmpl_oC         = r'\s*(\d+)\s+(°C)\s*'
tmpl_oC_dot     = r'\s*(\d+.\d+)\s+(°C)\s*'
tmpl_oC_comma   = r'\s*(\d+,\d+)\s+(°C)\s*'

tmpl_Amp        = r'\s*(\d+,\d+|\d+)\s+(Amp)\s*'

tmpl_Hz         = r'\s*(\d+,\d+|\d+)\s+(Hz)\s*'

tmpl_Kw         = r'\s*(\d+,\d+|\d+)\s+(Kw)\s*'

tmpl_psi        = r'\s*(\d+,\d+|\d+)\s+(psi)\s*'

tmpl_xseg       = r'\s*(\d+)\s+(#/s)\s*'
tmpl_xseg_dot   = r'\s*(\d+.\d+)\s+(#/s)\s*'
tmpl_xseg_comma = r'\s*(\d+,\d+)\s+(#/s)\s*'

tmpl_num        = r'\s*(\d+,\d+|\d+)\s+(#)$'

tmpl_GB         = r'\s*(\d+)\s+(GB)\s*'
tmpl_GB_dot     = r'\s*(\d+\.\d+|\d+)\s+(GB)\s*'
tmpl_GB_comma   = r'\s*(\d+\,\d+|\d+)\s+(GB)\s*'

tmpl_Msgxs      = r'\s*(\d+\.\d+|\d+)\s+(Msg/s)\s*'
tmpl_d          = r'\s*(\d+\.\d+|\d+)\s+(d)\s+'
tmpl_Horas      = r'\s*(\d+\.\d+|\d+)\s+(Horas)\s*'
tmpl_msec       = r'\s*(\d+\.\d+|\d+)\s+(msec)\s*'
tmpl_empty      = r'\s*(&amp;nbsp;)\s*'
tmpl_Mbitxs     = r'\s*(&lt;)\s*(\d+\.\d+|\d+)\s+(Mbit/s)\s*'
tmpl_h_m        = r'\s*(\d+\.\d+|\d+)\s+h\s+(\d+\.\d+|\d+)\s+m\s+'

 #/s

e = ' 0 %'
e = '&lt; 0.01 Mbit/s'
tmpl = '\s*(&lt;)\s*(\d+\.\d+|\d+)\s+(Mbit/s)\s*'
r = re.match(tmpl,e)
print(r)
if r:
    print(r.group(2))
    print(r.group(3))
#    print(r.group(3))

