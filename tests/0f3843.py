#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):

        # EVEX.NDS.LIG.66.0F38.W0 43 /r
        # VGETEXPSS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}

        myEVEX = EVEX('EVEX.NDS.LIG.66.0F38.W0')
        Buffer = '{}430e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x43)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vgetexpss ')
        assert_equal(myDisasm.instr.repr, 'vgetexpss xmm1, xmm15, dword ptr [rsi]')

        # EVEX.NDS.LIG.66.0F38.W1 43 /r
        # VGETEXPSD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}

        myEVEX = EVEX('EVEX.NDS.LIG.66.0F38.W1')
        Buffer = '{}430e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x43)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vgetexpsd ')
        assert_equal(myDisasm.instr.repr, 'vgetexpsd xmm1, xmm15, qword ptr [rsi]')
