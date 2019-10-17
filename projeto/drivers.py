import visa

rm = visa.ResourceManager()

class DMM(object):
  pass

class Cal(object):
  pass


class Keysight34465A(DMM):
  def __init__(self, addr):
    self.dmm = rm.open_resource(addr, timeout = 5000)

  def idn(self):
    return self.dmm.query('*IDN?')

  def set_range(self, unidade, val):
    self.dmm.query('CONF:{}:DC {},MAX;*OPC?'.format(unidade, val))

  def read(self):
    return self.dmm.query('READ?')
    
class Fluke5500(Cal):
  def __init__(self, addr):
    self.cal = rm.open_resource(addr)

  def idn(self):
    return self.cal.query('*IDN?')

  def standby(self):
    self.cal.query('STBY;*OPC?;')

  def operate(self):
    self.cal.query('OPER;*OPC?')

  def output(self, val, unidade):
    self.cal.query('OUT {}V, 0HZ;*OPC?;'.format(val, unidade))
