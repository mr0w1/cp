#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: CP v0.1a
# Generated: Sat May 21 19:05:12 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dsd
import math
import osmosdr
import time
import wx


class cp01a(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="CP v0.1a")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.freq = freq = 92.9e6
        self.samp_rate = samp_rate = 2.4e6
        self.ch2_volume = ch2_volume = 1
        self.ch2_squelch = ch2_squelch = -30
        self.ch2_mute = ch2_mute = 1
        self.ch2_modulation = ch2_modulation = 0
        self.ch2_invert = ch2_invert = 1
        self.ch2_freq = ch2_freq = freq
        self.ch1_volume = ch1_volume = 1
        self.ch1_squelch = ch1_squelch = -30
        self.ch1_mute = ch1_mute = 1
        self.ch1_modulation = ch1_modulation = 0
        self.ch1_invert = ch1_invert = 1
        self.ch1_freq = ch1_freq = freq

        ##################################################
        # Blocks
        ##################################################
        self.tab = self.tab = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.tab.AddPage(grc_wxgui.Panel(self.tab), "Ch 1")
        self.tab.AddPage(grc_wxgui.Panel(self.tab), "Ch 2")
        self.GridAdd(self.tab, 3, 0, 1, 7)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Radio Center Freq",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._freq_text_box, 19, 0, 1, 10)
        _ch2_volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ch2_volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ch2_volume_sizer,
        	value=self.ch2_volume,
        	callback=self.set_ch2_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ch2_volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ch2_volume_sizer,
        	value=self.ch2_volume,
        	callback=self.set_ch2_volume,
        	minimum=0,
        	maximum=10,
        	num_steps=20,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_ch2_volume_sizer, 2, 2, 1, 1)
        _ch2_squelch_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ch2_squelch_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ch2_squelch_sizer,
        	value=self.ch2_squelch,
        	callback=self.set_ch2_squelch,
        	label="Squelch",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ch2_squelch_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ch2_squelch_sizer,
        	value=self.ch2_squelch,
        	callback=self.set_ch2_squelch,
        	minimum=-70,
        	maximum=0,
        	num_steps=14,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_ch2_squelch_sizer, 2, 3, 1, 1)
        self._ch2_mute_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.ch2_mute,
        	callback=self.set_ch2_mute,
        	label="Mute",
        	true=0,
        	false=1,
        )
        self.GridAdd(self._ch2_mute_check_box, 2, 5, 1, 1)
        self._ch2_modulation_chooser = forms.button(
        	parent=self.GetWin(),
        	value=self.ch2_modulation,
        	callback=self.set_ch2_modulation,
        	label="Modulation",
        	choices=[0, 1],
        	labels=["DMR","NBFM"],
        )
        self.GridAdd(self._ch2_modulation_chooser, 2, 1, 1, 1)
        self._ch2_invert_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.ch2_invert,
        	callback=self.set_ch2_invert,
        	label="Invert",
        	true=-1,
        	false=1,
        )
        self.GridAdd(self._ch2_invert_check_box, 2, 4, 1, 1)
        self._ch2_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.ch2_freq,
        	callback=self.set_ch2_freq,
        	label="Ch2 Freq",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._ch2_freq_text_box, 2, 0, 1, 1)
        _ch1_volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ch1_volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ch1_volume_sizer,
        	value=self.ch1_volume,
        	callback=self.set_ch1_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ch1_volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ch1_volume_sizer,
        	value=self.ch1_volume,
        	callback=self.set_ch1_volume,
        	minimum=0,
        	maximum=10,
        	num_steps=40,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_ch1_volume_sizer, 0, 2, 1, 1)
        _ch1_squelch_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ch1_squelch_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ch1_squelch_sizer,
        	value=self.ch1_squelch,
        	callback=self.set_ch1_squelch,
        	label="Squelch",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ch1_squelch_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ch1_squelch_sizer,
        	value=self.ch1_squelch,
        	callback=self.set_ch1_squelch,
        	minimum=-70,
        	maximum=0,
        	num_steps=14,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_ch1_squelch_sizer, 0, 3, 1, 1)
        self._ch1_mute_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.ch1_mute,
        	callback=self.set_ch1_mute,
        	label="Mute",
        	true=0,
        	false=1,
        )
        self.GridAdd(self._ch1_mute_check_box, 0, 5, 1, 1)
        self._ch1_modulation_chooser = forms.button(
        	parent=self.GetWin(),
        	value=self.ch1_modulation,
        	callback=self.set_ch1_modulation,
        	label="Modulation",
        	choices=[0, 1],
        	labels=["DMR","NBFM"],
        )
        self.GridAdd(self._ch1_modulation_chooser, 0, 1, 1, 1)
        self._ch1_invert_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.ch1_invert,
        	callback=self.set_ch1_invert,
        	label="Invert",
        	true=-1,
        	false=1,
        )
        self.GridAdd(self._ch1_invert_check_box, 0, 4, 1, 1)
        self._ch1_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.ch1_freq,
        	callback=self.set_ch1_freq,
        	label="Ch1 Freq",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._ch1_freq_text_box, 0, 0, 1, 1)
        self.wxgui_waterfallsink2_1 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.GridAdd(self.wxgui_waterfallsink2_1.win, 4, 0, 15, 10)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.tab.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1333,
        	title="Channel 2",
        	peak_hold=False,
        )
        self.tab.GetPage(1).GridAdd(self.wxgui_fftsink2_0_0.win, 0, 0, 12, 7)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.tab.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1333,
        	title="Channel 1",
        	peak_hold=False,
        )
        self.tab.GetPage(0).GridAdd(self.wxgui_fftsink2_0.win, 0, 0, 12, 7)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_3_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=8000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_3 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=8000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2_0 = filter.rational_resampler_ccc(
                interpolation=48000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=48000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=192000,
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=192000,
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_1_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 192000, 5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 192000, 5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fft_filter_ccc_0_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), ch2_freq - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), ch1_freq - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.dsd_block_ff_0_0 = dsd.block_ff(dsd.dsd_FRAME_DMR_MOTOTRBO,dsd.dsd_MOD_GFSK,3,True,3)
        self.dsd_block_ff_0 = dsd.block_ff(dsd.dsd_FRAME_DMR_MOTOTRBO,dsd.dsd_MOD_GFSK,3,True,3)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((ch2_invert * ch2_mute, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((ch1_invert * ch1_mute, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((ch2_volume, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((ch1_volume, ))
        self.blks2_selector_0_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=ch2_modulation,
        )
        self.blks2_selector_0_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=ch2_modulation,
        	output_index=0,
        )
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=ch1_modulation,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=ch1_modulation,
        )
        self.audio_sink_0_0 = audio.sink(48000, "", True)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_quadrature_demod_cf_1_0 = analog.quadrature_demod_cf(1.6)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf(1.6)
        self.analog_pwr_squelch_xx_0_0_0 = analog.pwr_squelch_cc(ch2_squelch, 1e-4, 0, True)
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(ch1_squelch, 1e-4, 0, True)
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=192000,
        	tau=75e-6,
        	max_dev=2.5e3,
        )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=192000,
        	tau=75e-6,
        	max_dev=2.5e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.blks2_selector_0_0, 1))    
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.blks2_selector_0_0_0, 1))    
        self.connect((self.analog_pwr_squelch_xx_0_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_0, 0), (self.blks2_selector_0_1, 0))    
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.dsd_block_ff_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_1_0, 0), (self.dsd_block_ff_0_0, 0))    
        self.connect((self.blks2_selector_0, 1), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blks2_selector_0, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.blks2_selector_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blks2_selector_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blks2_selector_0_1, 1), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.blks2_selector_0_1, 0), (self.rational_resampler_xxx_2_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.audio_sink_0_0, 0))    
        self.connect((self.dsd_block_ff_0, 0), (self.rational_resampler_xxx_3, 0))    
        self.connect((self.dsd_block_ff_0_0, 0), (self.rational_resampler_xxx_3_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.analog_pwr_squelch_xx_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.low_pass_filter_1_0, 0), (self.analog_nbfm_rx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_1, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_1_0, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.analog_quadrature_demod_cf_1, 0))    
        self.connect((self.rational_resampler_xxx_2_0, 0), (self.analog_quadrature_demod_cf_1_0, 0))    
        self.connect((self.rational_resampler_xxx_3, 0), (self.blks2_selector_0_0, 0))    
        self.connect((self.rational_resampler_xxx_3_0, 0), (self.blks2_selector_0_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_waterfallsink2_1, 0))    


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_ch1_freq(self.freq)
        self.set_ch2_freq(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.ch1_freq - self.freq)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq(self.ch2_freq - self.freq)
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fft_filter_ccc_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.freq_xlating_fft_filter_ccc_0_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_waterfallsink2_1.set_sample_rate(self.samp_rate)

    def get_ch2_volume(self):
        return self.ch2_volume

    def set_ch2_volume(self, ch2_volume):
        self.ch2_volume = ch2_volume
        self._ch2_volume_slider.set_value(self.ch2_volume)
        self._ch2_volume_text_box.set_value(self.ch2_volume)
        self.blocks_multiply_const_vxx_0_0.set_k((self.ch2_volume, ))

    def get_ch2_squelch(self):
        return self.ch2_squelch

    def set_ch2_squelch(self, ch2_squelch):
        self.ch2_squelch = ch2_squelch
        self._ch2_squelch_slider.set_value(self.ch2_squelch)
        self._ch2_squelch_text_box.set_value(self.ch2_squelch)
        self.analog_pwr_squelch_xx_0_0_0.set_threshold(self.ch2_squelch)

    def get_ch2_mute(self):
        return self.ch2_mute

    def set_ch2_mute(self, ch2_mute):
        self.ch2_mute = ch2_mute
        self._ch2_mute_check_box.set_value(self.ch2_mute)
        self.blocks_multiply_const_vxx_2.set_k((self.ch2_invert * self.ch2_mute, ))

    def get_ch2_modulation(self):
        return self.ch2_modulation

    def set_ch2_modulation(self, ch2_modulation):
        self.ch2_modulation = ch2_modulation
        self._ch2_modulation_chooser.set_value(self.ch2_modulation)
        self.blks2_selector_0_0_0.set_input_index(int(self.ch2_modulation))
        self.blks2_selector_0_1.set_output_index(int(self.ch2_modulation))

    def get_ch2_invert(self):
        return self.ch2_invert

    def set_ch2_invert(self, ch2_invert):
        self.ch2_invert = ch2_invert
        self._ch2_invert_check_box.set_value(self.ch2_invert)
        self.blocks_multiply_const_vxx_2.set_k((self.ch2_invert * self.ch2_mute, ))

    def get_ch2_freq(self):
        return self.ch2_freq

    def set_ch2_freq(self, ch2_freq):
        self.ch2_freq = ch2_freq
        self._ch2_freq_text_box.set_value(self.ch2_freq)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq(self.ch2_freq - self.freq)

    def get_ch1_volume(self):
        return self.ch1_volume

    def set_ch1_volume(self, ch1_volume):
        self.ch1_volume = ch1_volume
        self._ch1_volume_slider.set_value(self.ch1_volume)
        self._ch1_volume_text_box.set_value(self.ch1_volume)
        self.blocks_multiply_const_vxx_0.set_k((self.ch1_volume, ))

    def get_ch1_squelch(self):
        return self.ch1_squelch

    def set_ch1_squelch(self, ch1_squelch):
        self.ch1_squelch = ch1_squelch
        self._ch1_squelch_slider.set_value(self.ch1_squelch)
        self._ch1_squelch_text_box.set_value(self.ch1_squelch)
        self.analog_pwr_squelch_xx_0_0.set_threshold(self.ch1_squelch)

    def get_ch1_mute(self):
        return self.ch1_mute

    def set_ch1_mute(self, ch1_mute):
        self.ch1_mute = ch1_mute
        self._ch1_mute_check_box.set_value(self.ch1_mute)
        self.blocks_multiply_const_vxx_1.set_k((self.ch1_invert * self.ch1_mute, ))

    def get_ch1_modulation(self):
        return self.ch1_modulation

    def set_ch1_modulation(self, ch1_modulation):
        self.ch1_modulation = ch1_modulation
        self._ch1_modulation_chooser.set_value(self.ch1_modulation)
        self.blks2_selector_0.set_output_index(int(self.ch1_modulation))
        self.blks2_selector_0_0.set_input_index(int(self.ch1_modulation))

    def get_ch1_invert(self):
        return self.ch1_invert

    def set_ch1_invert(self, ch1_invert):
        self.ch1_invert = ch1_invert
        self._ch1_invert_check_box.set_value(self.ch1_invert)
        self.blocks_multiply_const_vxx_1.set_k((self.ch1_invert * self.ch1_mute, ))

    def get_ch1_freq(self):
        return self.ch1_freq

    def set_ch1_freq(self, ch1_freq):
        self.ch1_freq = ch1_freq
        self._ch1_freq_text_box.set_value(self.ch1_freq)
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.ch1_freq - self.freq)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = cp01a()
    tb.Start(True)
    tb.Wait()
