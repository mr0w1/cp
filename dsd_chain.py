##################################################
# GNU Radio Python Flow Graph
# Title: DSD Chain
# Generated: Fri May 20 18:34:18 2016
##################################################

from gnuradio import analog
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
import dsd
import math


class dsd_chain(gr.hier_block2):

    def __init__(self):
        gr.hier_block2.__init__(
            self, "DSD Chain",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_3 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=8000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=48000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.dsd_block_ff_0 = dsd.block_ff(dsd.dsd_FRAME_DMR_MOTOTRBO,dsd.dsd_MOD_GFSK,3,True,3)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf(1.6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.dsd_block_ff_0, 0))    
        self.connect((self.dsd_block_ff_0, 0), (self.rational_resampler_xxx_3, 0))    
        self.connect((self, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.analog_quadrature_demod_cf_1, 0))    
        self.connect((self.rational_resampler_xxx_3, 0), (self, 0))    


