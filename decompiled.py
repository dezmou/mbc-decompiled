#
#  Panoramix v4 Oct 2019 
#  Decompiled source of 0x8C051C68D9601771CE96d4c9e971985aeDE480f7
# 
#  Let's make the world open source 
# 

def storage:
  stor0 is addr at storage 0 # owner
  cost is uint256 at storage 1
  percent is uint256 at storage 2

def cost(): # not payable
  return cost

def percent(): # not payable
  return percent

def pages(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  require _param2 < 4
  require _param3 < 4
  mem[224] = stor[sha3((3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1)].field_0
  idx = 224
  s = 0
  while stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length + 224 > idx + 32:
      mem[idx + 32] = stor[s + sha3((3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1)].field_256
      idx = idx + 32
      s = s + 1
      continue 
  return stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0, 
         Array(len=stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length, data=mem[224 len stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length + (floor32(stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length - 1) + -stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length + 32 % 32)]),
         stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512

#
#  Regular functions
#

def _fallback() payable: # default function
  stop

def contractBalance(): # not payable
  require stor0 == caller
  return eth.balance(this.address)

def updateCost(uint256 _newCost): # not payable
  require stor0 == caller
  cost = _newCost

def updateOwner(address _newOwner): # not payable
  require stor0 == caller
  stor0 = _newOwner

def updatePercent(uint256 _param1): # not payable
  require stor0 == caller
  percent = _param1

def withdraw(): # not payable
  require stor0 == caller
  call stor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success

def setPrice(uint256 _param1, uint32 _param2, uint32 _param3, uint256 _param4): # not payable
  require _param2 < 4
  require _param3 < 4
  require stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0 == caller
  require _param2 < 4
  require _param3 < 4
  stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512 = _param4
  require _param2 < 4
  require _param3 < 4
  require _param2 < 4
  require _param3 < 4
  mem[320] = stor[sha3((3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1)].field_0
  idx = 320
  s = 0
  while stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length + 320 > idx + 32:
      mem[idx + 32] = stor[s + sha3((3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1)].field_256
      idx = idx + 32
      s = s + 1
      continue 
  log 0x6ea16f87: _param1, _param2 << 224, _param3 << 224, stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0, Array(len=stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length, data=mem3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length + (floor32(stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length - 1) + -stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1].length + 32 % 32)]), _param4

def setHtml(): # not payable
  require uint32(cd) < 4
  require uint32(cd) < 4
  require stor[(3 * uint32(cd)) + (12 * uint32(cd)) + ('map', ('cd', 4), ('name', 'pages', 3))].field_0 == caller
  require uint32(cd) < 4
  require uint32(cd) < 4
  stor[(3 * uint32(cd)) + (12 * uint32(cd)) + ('map', ('cd', 4), ('name', 'pages', 3))].field_256 = (2 * ('cd', 100).length) + 1
  s = 0
  idx = cd[100] + 36
  while cd('cd', 100).length + 36 > idx:
      stor[s + sha3((3 * uint32(cd)) + (12 * uint32(cd)) + ('map', ('cd', 4), ('name', 'pages', 3)) + 1)].field_0 = cd[idx]
      s = s + 1
      idx = idx + 32
      continue 
  idx = Mask(251, 0, ('cd', 100).length + 31) >> 5
  while stor[(3 * uint32(cd)) + (12 * uint32(cd)) + ('map', ('cd', 4), ('name', 'pages', 3)) + 1].length + 31 / 32 > idx:
      stor[idx + sha3((3 * uint32(cd)) + (12 * uint32(cd)) + ('map', ('cd', 4), ('name', 'pages', 3)) + 1)].field_0 = 0
      idx = idx + 1
      continue 
  require uint32(cd) < 4
  require uint32(cd) < 4
  require uint32(cd) < 4
  require uint32(cd) < 4
  log 0x6ea16f87: cdap', ('cd', 4), ('name', 'pages', 3))].field_0, Array(len=('cd', 100).length, data=call.data[cdap', ('cd', 4), ('name', 'pages', 3))].field_512

def buyTile(uint256 _param1, uint32 _param2, uint32 _param3, array _param4) payable: 
  require _param2 < 4
  require _param3 < 4
  if not stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0:
      require call.value >= cost
      log 0xe1500d0d: _param1, _param2 << 224, _param3 << 224, addr(this.address), caller, cost
  else:
      require stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0 != caller
      require stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512
      require call.value >= stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512
      log 0xe1500d0d: _param1, _param2 << 224, _param3 << 224, stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0, caller, stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512
      call stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0 with:
         value stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512 * percent / 100 wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
  require _param2 < 4
  require _param3 < 4
  stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_0 = caller
  stor[sha3((3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3)) + 1)][].field_0 = Array(len=_param4.length, data=_param4[all])
  stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'pages', 3))].field_512 = 0

