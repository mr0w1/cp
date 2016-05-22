##################################################
# GNU Radio Python Flow Graph
# Title: WBFM Chain
# Generated: Sat May 21 16:22:10 2016
##################################################

from gnuradio import analog
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes


class wbfm_chain(gr.hier_block2):

    def __init__(self):
        gr.hier_block2.__init__(
            self, "WBFM Chain",
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
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 2400000, 200e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=192000,
        	audio_decimation=4,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    


