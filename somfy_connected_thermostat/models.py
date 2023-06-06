from enum import Enum
from time import time

class Principal:
  def __init__(self, id: int, first_name: str, last_name: str, email: str):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email

class Thermostat:
  def __init__(self, id: str, name: str):
    self.id = id
    self.name = name

class Smartphone:
  def __init__(self, name: str, vendor_id: str, push_token: str):
    self.name = name
    self.vendor_id = vendor_id
    self.push_token = push_token

class Heating_mode(Enum):
    MANUAL = 'manuel'
    FREEZE = 'freeze'
    AWAY = 'away'
    AT_HOME = 'at_home'
    SLEEP = 'sleep'

class ThermostatInfo:
  def __init__(self, temperature: float, temperature_consigne: float, battery: int, mode: str):
    self.temperature = temperature
    self.temperature_consigne = temperature_consigne
    self.battery = battery
    self.mode = mode

class ThermostatCommand:
  def __init__(self, heating_mode: Heating_mode, derogation_type: str, duration: int,finish_at: int, target_temperature: float):
    self.heating_mode = heating_mode if target_temperature > 14 else Heating_mode.FREEZE
    self.derogation_type = derogation_type
    self.duration = duration
    self.started_at = round(time())
    self.finish_at = finish_at
    self.target_temperature = target_temperature

class SetTemperatureCommand:
  def __init__(self, target_temperature: float, derogation_type: str = 'further_notice', heating_mode = Heating_mode.MANUAL):
    ThermostatCommand.__init__(
      self,
      heating_mode= heating_mode,
      derogation_type= derogation_type,
      duration= -1,
      finish_at= -1,
      target_temperature= target_temperature,
    )

class SetTemperatureWithDurationCommand:
  def __init__(self, target_temperature: float, duration: int, heating_mode = Heating_mode.MANUAL):
    ThermostatCommand.__init__(
      self,
      heating_mode= heating_mode,
      derogation_type= 'date',
      duration= duration,
      finish_at= time() + duration,
      target_temperature= target_temperature,
    )

class ResetDerogationCommand:
  def __init__(self, target_temperature: float):
    ThermostatCommand.__init__(
      self,
      heating_mode= 'at_home',
      derogation_type= 'further_notice',
      duration= -1,
      finish_at= -1,
      target_temperature= target_temperature,
    )

class SetHeatingModeCommand:
  def __init__(self, heating_mode: str, target_temperature: float):
    ThermostatCommand.__init__(
      self,
      heating_mode= heating_mode,
      derogation_type= 'further_notice',
      duration= -1,
      finish_at= -1,
      target_temperature= target_temperature,
    )

class SetFreezeModeCommand:
  def __init__(self):
    ThermostatCommand.__init__(
      self,
      heating_mode= 'freeze',
      derogation_type= 'further_notice',
      duration= -1,
      finish_at= -1,
      target_temperature= 8.0,
    )