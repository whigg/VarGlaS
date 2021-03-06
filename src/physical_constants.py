"""
This module contains the classes that hold known 
physical constants relavent to the simulations and a class to create new 
constants
"""

class PhysicalConstant(float):
  """
  This class allows the creation of new floating point physical constants.
      
  :param float value: Value of the physical constant
  :param description: Description of the physical constant
  :param units: Units of the physical constant
  """
  def __new__(cls, value = 0.0, description = None, units = None):
    """
    Creates a new PhysicalConstant object
    """
    ii = float.__new__(cls,value)
    ii.description = description
    ii.units = units
    return ii

class IceParameters(object):
  """
  This class contains the default physical parameters used in modeling
  the ice sheet.
  
  :param params: Optional dictionary object of physical parameters
  """
  def __init__(self,params=None):
    if params:
      self.params = params
    else:
      self.params = self.get_default_parameters()

  def globalize_parameters(self, namespace=None):
    """
    This function converts the parameter dictinary into global PhysicalContstant
    objects
    
    :param namespace: Optional namespace in which to place the global variables
    """
    for param in self.params.iteritems():
      vars(namespace)[param[0]] = PhysicalConstant(param[1][0],
                                                   param[1][1],
                                                   param[1][2])

  def get_default_parameters(self):
    """
    Creates a dictionary of default physical constants and returns it
    
    :rtype: Python dictionary
    """
    d_params = \
    {'eps_reg': (1e-15,   'strain rate regularization parameter','t^{-1}'),
     'n'      : (3.0,     'viscosity nonlinearity parameter','dimensionless'),
     'rho'    : (910,     'ice density','kg m^{-3}'),
     'rho_w'  : (1000,    'water density', 'kg m^{-3}'),
     'g'      : (9.81,    'gravitational acceleration','m s^{-2}'),
     'a0'     : (5.45e10, 'ice hardness limit','a^{-1} Pa^{-1}'),
     'Q0'     : (13.9e4,  'ice activation energy','J mol^{-1}'),
     'R'      : (8.314,   'universal gas constant','J mol^{-1} K^{-1}'),
     'k'      : (6.62e7,  'thermal conductivity of ice','W m^{-1} K^{-1}'),
     'C'      : (2009,    'heat capacity of ice','J kg^{-1} K^{-1}'),
     'L'      : (3.35e5,  'latent heat of ice','J kg^{-1}'),
     'q_geo'  : (1324512, 'geothermal heat flux','W m^{-2}'),
     'gamma'  : (8.71e-4, 'pressure melting point depth dependence','K m^{-1}'),
     'nu'     : (3.5e3,   'moisture diffusivity','kg m^{-1} a^{-1}'),
     'C_w'    : (4217.6,  'Heat capacity of water at 273K','J Kg^{-1} K^{-1}'),
     'E'      : (1.,      'Enhancement Factor','')}

    return d_params








  
