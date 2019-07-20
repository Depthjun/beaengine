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

        # EVEX.128.66.0F38.W0 54 /r
        # VPOPCNTB xmm1{k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}540e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x54)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpopcntb ')
        assert_equal(myDisasm.instr.repr, 'vpopcntb xmm1, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W0 54 /r
        # VPOPCNTB ymm1{k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}540e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x54)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpopcntb ')
        assert_equal(myDisasm.instr.repr, 'vpopcntb ymm1, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W0 54 /r
        # VPOPCNTB zmm1{k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}540e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x54)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpopcntb ')
        assert_equal(myDisasm.instr.repr, 'vpopcntb zmm1, zmmword ptr [rsi]')

        # EVEX.128.66.0F38.W1 54 /r
        # VPOPCNTW xmm1{k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}540e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x54)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpopcntw ')
        assert_equal(myDisasm.instr.repr, 'vpopcntw xmm1, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W1 54 /r
        # VPOPCNTW ymm1{k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}540e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x54)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpopcntw ')
        assert_equal(myDisasm.instr.repr, 'vpopcntw ymm1, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W1 54 /r
        # VPOPCNTW zmm1{k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}540e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x54)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpopcntw ')
        assert_equal(myDisasm.instr.repr, 'vpopcntw zmm1, zmmword ptr [rsi]')
