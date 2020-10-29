import numpy as np
def grav_accel(phi=0, h=0):
  """Ускорение свободного падения
  phi= широта местности наблюдения
  h= высота над поверхностью Земли 
  """
  g=9.78*(1+0.005302*(np.sin(phi)))**2-0.000006*(np.sin(2*phi)**2)-0.000003086*h
  return g
def losing_wight_function(mass=50, phi_0=54, phi_end=0, h_0=0, h_end=3000):
  """функция определяющая вес
  """
  p_0=grav_accel(phi_0, h_0)*mass
  p_end=grav_accel(phi_end,h_end)*mass
  delta_p=(p_0-p_end)*100
  if delta_p > 0:
    print('Вы похудеете на:', delta_p, 'г')
  elif delta_p < 0:
    print('Вы поправитесь на:', delta_p*(-1), 'г')
  else:
    print('Ты- жиробас,сиди дома!')
  
losing_wight_function(49,2,3,8,8)