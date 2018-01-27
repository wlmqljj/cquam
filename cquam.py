#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Motorola CQUAM v1.4
# Author: jowijo
# Description: Working implementation of AM Stereo
# Generated: Tue Jan 23 16:26:09 2018
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class cquam(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Motorola CQUAM v1.4")

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	1, 44100, 11e3, 1e3, firdes.WIN_BLACKMAN, 6.76))
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/mnt/mediay/SEND/output_4.wav', 2, 44100, 16)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.3, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_3 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_source_0 = audio.source(44100, 'tx_source', True)
        self.analog_sig_source_x_2_0_0 = analog.sig_source_f(44100, analog.GR_SIN_WAVE, 25, 0.08, 0)
        self.analog_sig_source_x_2_0 = analog.sig_source_f(44100, analog.GR_COS_WAVE, 0, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_2_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_2_0_0, 0), (self.blocks_add_xx_3, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.audio_source_0, 1), (self.blocks_add_xx_1, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.audio_source_0, 1), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_wavfile_sink_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_add_xx_3, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_float_0, 0))


def main(top_block_cls=cquam, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
