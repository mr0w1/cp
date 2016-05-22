##################################################
# GNU Radio Python Flow Graph
# Title: NBFM Chain
# Generated: Fri May 20 18:45:25 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes


class nbfm_chain(gr.hier_block2):

    def __init__(self):
        gr.hier_block2.__init__(
            self, "NBFM Chain",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=192000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 192000, 5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((5, ))
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=192000,
        	tau=75e-6,
        	max_dev=2.5e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_1, 0))    


