import drivers
import inspect

def inicia_instrumento(drivers_lista):
  for i, inst_class in enumerate(drivers_lista):
    print(str(i)+': ', inst_class)
  escolha = input('\nInforme o número:')
  addr = input('Informe o endereço GPIB:')

  instrumento = drivers_lista[int(escolha)]('GPIB0::'+addr+'::INSTR')
  print(instrumento.idn())
  return instrumento


def pega_drivers_para_classe(classe):
  drivers_list = []

  for nome_do_driver in dir(drivers):
    
    driver = drivers.__getattribute__(nome_do_driver)

    if not inspect.isclass(driver) or driver == classe:
      continue
    
    if issubclass(driver, classe):
      drivers_list.append(driver)

  return drivers_list

def main():
  drivers_dmm = pega_drivers_para_classe(drivers.DMM)
  drivers_cal = pega_drivers_para_classe(drivers.Cal)

  print('Multímetors disponíveis:')
  dmm = inicia_instrumento(drivers_dmm)
  
  print('Calibradores disponíveis:')
  cal = inicia_instrumento(drivers_cal)

  pontos_calibrados_str = input('Informe os pontos a serem calibrados separados por vírgula:')

  pontos_calibrados_float = []
  for ponto_str in pontos_calibrados_str.split(','):
    ponto_float = float(ponto_str)
    pontos_calibrados_float.append(ponto_float)

  resultados = []
  
  for ponto in pontos_calibrados_float:
    resultado = {'VI': [], 'VC': []}
    dmm.set_range('VOLT', ponto)
    cal.output(ponto, 'V')
    cal.operate()
    for n in range(4):
      leitura = dmm.read()
      
      resultado['VI'].append(float(leitura))
      resultado['VC'].append(float(ponto))

    resultados.append(resultado)
  cal.standby()

  # escreve resultados
  with open('resultados.csv', 'w') as f:
    f.write('VI 1;VI 2;VI 3;VI 4;VC 1;VC 2;VC 3;VC 4;\n')
    for ponto in resultados:
      for leitura in ponto['VI']:
        f.write(str(leitura).replace('.',',')+';')
      for leitura in ponto['VC']:
        f.write(str(leitura).replace('.',',')+';')
      f.write('\n')


if __name__ == '__main__':
  main()