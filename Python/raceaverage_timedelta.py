from datetime import timedelta, datetime
# Nonworking draft

class RaceAverage():
  """ Input: ["12:00 PM, DAY 1", "12:01 PM, DAY 1"]
      Output: 241
      
      Input: ["02:00 PM, DAY 19", "02:00 PM, DAY 20", "01:58 PM, DAY 20"]
      Output: 27239
  """
  def __init__(self, start):
    self.start = datetime(start)
    
    
  def avgMinutes(self, times):
  
    for time in times:
      total = abs(time - self.start)
      
    return total.minutes / times.length


