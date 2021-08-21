import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(nextStreamId = sp.TNat, streams = sp.TBigMap(sp.TNat, sp.TRecord(deposit = sp.TNat, ratePerSecond = sp.TNat, receiver = sp.TAddress, remainingBalance = sp.TNat, sender = sp.TAddress, startTime = sp.TNat, stopTime = sp.TNat, tokenAddress = sp.TAddress).layout(("deposit", ("ratePerSecond", ("receiver", ("remainingBalance", ("sender", ("startTime", ("stopTime", "tokenAddress")))))))))).layout(("nextStreamId", "streams")))
    self.init(nextStreamId = 0,
              streams = {})