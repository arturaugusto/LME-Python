import random

class Resource(object):
  def __init__(self, addr, timeout):
    super(Resource, self).__init__()
    self.addr = addr


  def query(self, cmd):
    if '::22::' in self.addr:
      if cmd == '*IDN?':
        return 'Keysight Technologies,34465A,MY57500288,A.02.14-02.40-02.14-00.49-03-01\n'
      if cmd == 'READ?':
        return '{:e}'.format(random.random())
    if '::7::' in self.addr:
      if cmd == '*IDN?':
        return 'CALIBRADOR,55XX,XXXXXXX'
    return '1'

  def write(self, cmd):
    return None

  def read(self, cmd):
    return '{:e}'.format(random.random())


class ResourceManager(object):
  def __init__(self):
    super(ResourceManager, self).__init__()
  
  def list_resources(self):
    return ('ASRL1::INSTR',
 'ASRL2::INSTR',
 'ASRL6::INSTR',
 'ASRL8::INSTR',
 'ASRL9::INSTR',
 'GPIB0::22::INSTR')

  def open_resource(self, addr, timeout=1000):
    return Resource(addr, timeout=1000)

    
class VisaMock(object):
  def __init__(self):
    super(VisaMock, self).__init__()
    self.ResourceManager = ResourceManager



visa = VisaMock()
