[38;5;8m# Palkeoramix decompiler. [0m

[32mdef [0mstorage:
  [32mstor0[0m is addr [38;5;8mat storage 0[0m[38;5;8m[0m
  [32mcost[0m is uint256 [38;5;8mat storage 1[0m[38;5;8m[0m
  [32mpercent[0m is uint256 [38;5;8mat storage 2[0m[38;5;8m[0m

[95mdef [0mcost(): [38;5;8m# not payable[0m
  return [32mcost[0m

[95mdef [0mpercent(): [38;5;8m# not payable[0m
  return [32mpercent[0m

[95mdef [0munknownc056b707(uint256 [32m_param1[0m, uint256 [32m_param2[0m, uint256 [32m_param3[0m): [38;5;8m# not payable[0m
  require [32m_param2[0m[1m < [0m4
  require [32m_param3[0m[1m < [0m4
  [95mmem[[0m224[95m][0m = [32mstor[[0msha3((3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_0[0m
  [94midx[0m = 224
  [94ms[0m = 0
  [32mwhile [0m[32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m + 224[1m > [0m[94midx[0m + 32[32m:[0m
      [95mmem[[0m[94midx[0m + 32[95m][0m = [32mstor[[0m[94ms[0m + sha3((3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_256[0m
      [94midx[0m = [94midx[0m + 32
      [94ms[0m = [94ms[0m + 1
      [32mcontinue [0m
  return [32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m, 
         [38;5;8mArray(len=[0m[32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m[38;5;8m, data=[0m[95mmem[[0m224[95m len [0m[32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m + (floor32([32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m - 1) + -[32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m + 32[1m % [0m32)[95m][0m[38;5;8m)[0m,
         [32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_512[0m

[38;5;8m#
#  Regular functions
#[0m

[95mdef [0m_fallback()[95m payable[0m: [38;5;8m# default function[0m
  stop

[95mdef [0mcontractBalance(): [38;5;8m# not payable[0m
  require [32mstor0[0m[1m == [0mcaller
  return eth.balance(this.address)

[95mdef [0mupdateCost(uint256 [32m_newCost[0m): [38;5;8m# not payable[0m
  require [32mstor0[0m[1m == [0mcaller
  [32mcost[0m = [32m_newCost[0m

[95mdef [0mupdateOwner(address [32m_newOwner[0m): [38;5;8m# not payable[0m
  require [32mstor0[0m[1m == [0mcaller
  [32mstor0[0m = [32m_newOwner[0m

[95mdef [0munknown2e723593(uint256 [32m_param1[0m): [38;5;8m# not payable[0m
  require [32mstor0[0m[1m == [0mcaller
  [32mpercent[0m = [32m_param1[0m

[95mdef [0mwithdraw(): [38;5;8m# not payable[0m
  require [32mstor0[0m[1m == [0mcaller
  call [32mstor0[0m with:
     value eth.balance(this.address) [38;5;8mwei[0m
       gas 2300 * is_zero(value) [38;5;8mwei[0m
  require ext_call.success

[95mdef [0munknown8260dd31(uint256 [32m_param1[0m, uint32 [32m_param2[0m, uint32 [32m_param3[0m, uint256 [32m_param4[0m): [38;5;8m# not payable[0m
  require [32m_param2[0m[1m < [0m4
  require [32m_param3[0m[1m < [0m4
  require [32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m[1m == [0mcaller
  require [32m_param2[0m[1m < [0m4
  require [32m_param3[0m[1m < [0m4
  [32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_512[0m = [32m_param4[0m
  require [32m_param2[0m[1m < [0m4
  require [32m_param3[0m[1m < [0m4
  require [32m_param2[0m[1m < [0m4
  require [32m_param3[0m[1m < [0m4
  [95mmem[[0m320[95m][0m = [32mstor[[0msha3((3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_0[0m
  [94midx[0m = 320
  [94ms[0m = 0
  [32mwhile [0m[32mstor[[0m(3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m + 320[1m > [0m[94midx[0m + 32[32m:[0m
      [95mmem[[0m[94midx[0m + 32[95m][0m = [32mstor[[0m[94ms[0m + sha3((3[1m * [0m[32m_param3[0m) + (12[1m * [0m[32m_param2[0m) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_256[0m
      [94midx[0m = [94midx[0m + 32
      [94ms[0m = [94ms[0m + 1
      [32mcontinue [0m
  [38;5;8mlog 0x6ea16f87: _param1, _param2 << 224, _param3 << 224, stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3))].field_0, Array(len=stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1].length, data=mem[320 len stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1].length + (floor32(stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1].length - 1) + -stor[(3 * _param3) + (12 * _param2) + ('map', ('param', '_param1'), ('name', 'unknownc056b707', 3)) + 1].length + 32 % 32)]), _param4[0m

[95mdef [0munknownc6030f4d(): [38;5;8m# not payable[0m
  require [38;5;8muint32([0mcd[36][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[68][38;5;8m)[0m[1m < [0m4
  require [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m[1m == [0mcaller
  require [38;5;8muint32([0mcd[36][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[68][38;5;8m)[0m[1m < [0m4
  [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_256[0m = (2[1m * [0m[32m('cd', 100).length[0m) + 1
  [94ms[0m = 0
  [94midx[0m = cd[100] + 36
  [32mwhile [0mcd[100] + [32m('cd', 100).length[0m + 36[1m > [0m[94midx[0m[32m:[0m
      [32mstor[[0m[94ms[0m + sha3((3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_0[0m = cd[[94midx[0m]
      [94ms[0m = [94ms[0m + 1
      [94midx[0m = [94midx[0m + 32
      [32mcontinue [0m
  [94midx[0m = Mask(251, 0, [32m('cd', 100).length[0m + 31)[1m >> [0m5
  [32mwhile [0m[32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m + 31[1m / [0m32[1m > [0m[94midx[0m[32m:[0m
      [32mstor[[0m[94midx[0m + sha3((3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_0[0m = 0
      [94midx[0m = [94midx[0m + 1
      [32mcontinue [0m
  require [38;5;8muint32([0mcd[36][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[68][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[36][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[68][38;5;8m)[0m[1m < [0m4
  [38;5;8mlog 0x6ea16f87: cd[4], cd[36] << 224, cd[68] << 224, stor[(3 * uint32(cd[68])) + (12 * uint32(cd[36])) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))].field_0, Array(len=('cd', 100).length, data=call.data[cd[100] + 36 len ('cd', 100).length]), stor[(3 * uint32(cd[68])) + (12 * uint32(cd[36])) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))].field_512[0m

[95mdef [0munknown93ec714e()[95m payable[0m: 
  require [38;5;8muint32([0mcd[36][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[68][38;5;8m)[0m[1m < [0m4
  if not [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m:
      require call.value[1m >= [0m[32mcost[0m
      [38;5;8mlog 0xe1500d0d: cd[4], cd[36] << 224, cd[68] << 224, addr(this.address), caller, cost[0m
  else:
      require [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m != caller
      require [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_512[0m
      require call.value[1m >= [0m[32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_512[0m
      [38;5;8mlog 0xe1500d0d: cd[4], cd[36] << 224, cd[68] << 224, stor[(3 * uint32(cd[68])) + (12 * uint32(cd[36])) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))].field_0, caller, stor[(3 * uint32(cd[68])) + (12 * uint32(cd[36])) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))].field_512[0m
      call [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m with:
         value [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_512[0m[1m * [0m[32mpercent[0m[1m / [0m100 [38;5;8mwei[0m
           gas 2300 * is_zero(value) [38;5;8mwei[0m
      require ext_call.success
  require [38;5;8muint32([0mcd[36][38;5;8m)[0m[1m < [0m4
  require [38;5;8muint32([0mcd[68][38;5;8m)[0m[1m < [0m4
  [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_0[0m = caller
  [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_256[0m = (2[1m * [0m[32m('cd', 100).length[0m) + 1
  [94ms[0m = 0
  [94midx[0m = cd[100] + 36
  [32mwhile [0mcd[100] + [32m('cd', 100).length[0m + 36[1m > [0m[94midx[0m[32m:[0m
      [32mstor[[0m[94ms[0m + sha3((3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_0[0m = cd[[94midx[0m]
      [94ms[0m = [94ms[0m + 1
      [94midx[0m = [94midx[0m + 32
      [32mcontinue [0m
  [94midx[0m = Mask(251, 0, [32m('cd', 100).length[0m + 31)[1m >> [0m5
  [32mwhile [0m[32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3)) + 1[32m][0m[32m.length[0m + 31[1m / [0m32[1m > [0m[94midx[0m[32m:[0m
      [32mstor[[0m[94midx[0m + sha3((3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3)) + 1)[32m][0m[32m.field_0[0m = 0
      [94midx[0m = [94midx[0m + 1
      [32mcontinue [0m
  [32mstor[[0m(3[1m * [0m[38;5;8muint32([0mcd[68][38;5;8m)[0m) + (12[1m * [0m[38;5;8muint32([0mcd[36][38;5;8m)[0m) + ('map', ('cd', 4), ('name', 'unknownc056b707', 3))[32m][0m[32m.field_512[0m = 0


