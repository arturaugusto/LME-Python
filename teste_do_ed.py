from visa_mock import visa
rm = visa.ResourceManager()

dmm = rm.open_resource('GPIB0::22::INSTR', timeout = 50000)
dmm.query('*CLS;*OPC?')

cal = rm.open_resource('GPIB0::7::INSTR', timeout = 10000)
cal.query('*SRE 32;*ESE 1;*CLS;*OPC?')

print("ok")
dmm.query('CONF:VOLT:DC 10,MAX;*OPC?')
cal.query('OUT 5V, 0HZ;OPER;*OPC?')

leitura = dmm.query('READ?')

cal.query('STBY;*OPC?;')

print(leitura)
