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

        # EVEX.128.66.0F38.W0 7D /r
        # VPERMT2B xmm1 {k1}{z}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}7d20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x7d)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermt2b ')
        assert_equal(myDisasm.instr.repr, 'vpermt2b xmm4, xmm0, xmmword ptr [rax]')

        # EVEX.256.66.0F38.W0 7D /r
        # VPERMT2B ymm1 {k1}{z}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}7d20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x7d)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermt2b ')
        assert_equal(myDisasm.instr.repr, 'vpermt2b ymm4, ymm0, ymmword ptr [rax]')

        # EVEX.512.66.0F38.W0 7D /r
        # VPERMT2B zmm1 {k1}{z}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}7d20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x7d)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermt2b ')
        assert_equal(myDisasm.instr.repr, 'vpermt2b zmm4, zmm0, zmmword ptr [rax]')

        # EVEX.128.66.0F38.W1 7D /r
        # VPERMT2W xmm1 {k1}{z}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        Buffer = '{}7d20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x7d)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermt2w ')
        assert_equal(myDisasm.instr.repr, 'vpermt2w xmm4, xmm0, xmmword ptr [rax]')

        # EVEX.256.66.0F38.W1 7D /r
        # VPERMT2W ymm1 {k1}{z}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}7d20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x7d)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermt2w ')
        assert_equal(myDisasm.instr.repr, 'vpermt2w ymm4, ymm0, ymmword ptr [rax]')

        # EVEX.512.66.0F38.W1 7D /r
        # VPERMT2W zmm1 {k1}{z}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}7d20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x7d)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermt2w ')
        assert_equal(myDisasm.instr.repr, 'vpermt2w zmm4, zmm0, zmmword ptr [rax]')
