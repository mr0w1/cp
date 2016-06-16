#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: CP v0.4a QT
# Generated: Tue Jun 14 23:39:51 2016
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from dsd_chain import dsd_chain  # grc-generated hier_block
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from nbfm_chain import nbfm_chain  # grc-generated hier_block
from optparse import OptionParser
from wbfm_chain import wbfm_chain  # grc-generated hier_block
import osmosdr
import sip
import time


class cp04aQT(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "CP v0.4a QT")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("CP v0.4a QT")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "cp04aQT")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.radio_freq = radio_freq = 100
        self.samp_rate = samp_rate = 2.4e6
        self.rf_gain = rf_gain = 10
        self.freq = freq = radio_freq * 1000000
        self.ch3_volume = ch3_volume = 1
        self.ch3_squelch = ch3_squelch = -30
        self.ch3_mute = ch3_mute = 1
        self.ch3_modulation = ch3_modulation = 0
        self.ch3_invert = ch3_invert = 1
        self.ch3_freq = ch3_freq = radio_freq
        self.ch2_volume = ch2_volume = 1
        self.ch2_squelch = ch2_squelch = -30
        self.ch2_mute = ch2_mute = 1
        self.ch2_modulation = ch2_modulation = 0
        self.ch2_invert = ch2_invert = 1
        self.ch2_freq = ch2_freq = radio_freq
        self.ch1_volume = ch1_volume = 1
        self.ch1_squelch = ch1_squelch = -30
        self.ch1_mute = ch1_mute = 1
        self.ch1_modulation = ch1_modulation = 0
        self.ch1_invert = ch1_invert = 1
        self.ch1_freq = ch1_freq = radio_freq

        ##################################################
        # Blocks
        ##################################################
        self.settings = Qt.QTabWidget()
        self.settings_widget_0 = Qt.QWidget()
        self.settings_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.settings_widget_0)
        self.settings_grid_layout_0 = Qt.QGridLayout()
        self.settings_layout_0.addLayout(self.settings_grid_layout_0)
        self.settings.addTab(self.settings_widget_0, "Settings")
        self.top_grid_layout.addWidget(self.settings, 4,3,2,3)
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, "Ch 1")
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, "Ch 2")
        self.tabs_widget_2 = Qt.QWidget()
        self.tabs_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_2)
        self.tabs_grid_layout_2 = Qt.QGridLayout()
        self.tabs_layout_2.addLayout(self.tabs_grid_layout_2)
        self.tabs.addTab(self.tabs_widget_2, "Ch 3")
        self.top_grid_layout.addWidget(self.tabs, 4,0,2,3)
        self._rf_gain_range = Range(0, 50, 1, 10, 100)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, "RF Gain", "counter_slider", float)
        self.settings_grid_layout_0.addWidget(self._rf_gain_win, 1,0,1,1)
        self._ch3_volume_range = Range(0, 10, 1, 1, 50)
        self._ch3_volume_win = RangeWidget(self._ch3_volume_range, self.set_ch3_volume, "Volume", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ch3_volume_win, 2,2,1,1)
        self._ch3_squelch_range = Range(-70, 0, 10, -30, 50)
        self._ch3_squelch_win = RangeWidget(self._ch3_squelch_range, self.set_ch3_squelch, "Squelch", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ch3_squelch_win, 2,3,1,1)
        _ch3_mute_check_box = Qt.QCheckBox("Mute")
        self._ch3_mute_choices = {True: 0, False: 1}
        self._ch3_mute_choices_inv = dict((v,k) for k,v in self._ch3_mute_choices.iteritems())
        self._ch3_mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch3_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._ch3_mute_choices_inv[i]))
        self._ch3_mute_callback(self.ch3_mute)
        _ch3_mute_check_box.stateChanged.connect(lambda i: self.set_ch3_mute(self._ch3_mute_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ch3_mute_check_box, 2,5,1,1)
        self._ch3_modulation_options = (0, 1, 2, )
        self._ch3_modulation_labels = ("DMR", "NBFM", "WBFM", )
        self._ch3_modulation_tool_bar = Qt.QToolBar(self)
        self._ch3_modulation_tool_bar.addWidget(Qt.QLabel("Modulation"+": "))
        self._ch3_modulation_combo_box = Qt.QComboBox()
        self._ch3_modulation_tool_bar.addWidget(self._ch3_modulation_combo_box)
        for label in self._ch3_modulation_labels: self._ch3_modulation_combo_box.addItem(label)
        self._ch3_modulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ch3_modulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ch3_modulation_options.index(i)))
        self._ch3_modulation_callback(self.ch3_modulation)
        self._ch3_modulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ch3_modulation(self._ch3_modulation_options[i]))
        self.top_grid_layout.addWidget(self._ch3_modulation_tool_bar, 2,1,1,1)
        _ch3_invert_check_box = Qt.QCheckBox("Invert")
        self._ch3_invert_choices = {True: -1, False: 1}
        self._ch3_invert_choices_inv = dict((v,k) for k,v in self._ch3_invert_choices.iteritems())
        self._ch3_invert_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch3_invert_check_box, "setChecked", Qt.Q_ARG("bool", self._ch3_invert_choices_inv[i]))
        self._ch3_invert_callback(self.ch3_invert)
        _ch3_invert_check_box.stateChanged.connect(lambda i: self.set_ch3_invert(self._ch3_invert_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ch3_invert_check_box, 2,4,1,1)
        self._ch3_freq_tool_bar = Qt.QToolBar(self)
        self._ch3_freq_tool_bar.addWidget(Qt.QLabel("Ch3 Freq (MHz)"+": "))
        self._ch3_freq_line_edit = Qt.QLineEdit(str(self.ch3_freq))
        self._ch3_freq_tool_bar.addWidget(self._ch3_freq_line_edit)
        self._ch3_freq_line_edit.returnPressed.connect(
        	lambda: self.set_ch3_freq(eng_notation.str_to_num(str(self._ch3_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._ch3_freq_tool_bar, 2,0,1,1)
        self._ch2_volume_range = Range(0, 10, 1, 1, 50)
        self._ch2_volume_win = RangeWidget(self._ch2_volume_range, self.set_ch2_volume, "Volume", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ch2_volume_win, 1,2,1,1)
        self._ch2_squelch_range = Range(-70, 0, 10, -30, 50)
        self._ch2_squelch_win = RangeWidget(self._ch2_squelch_range, self.set_ch2_squelch, "Squelch", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ch2_squelch_win, 1,3,1,1)
        _ch2_mute_check_box = Qt.QCheckBox("Mute")
        self._ch2_mute_choices = {True: 0, False: 1}
        self._ch2_mute_choices_inv = dict((v,k) for k,v in self._ch2_mute_choices.iteritems())
        self._ch2_mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch2_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._ch2_mute_choices_inv[i]))
        self._ch2_mute_callback(self.ch2_mute)
        _ch2_mute_check_box.stateChanged.connect(lambda i: self.set_ch2_mute(self._ch2_mute_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ch2_mute_check_box, 1,5,1,1)
        self._ch2_modulation_options = (0, 1, 2, )
        self._ch2_modulation_labels = ("DMR", "NBFM", "WBFM", )
        self._ch2_modulation_tool_bar = Qt.QToolBar(self)
        self._ch2_modulation_tool_bar.addWidget(Qt.QLabel("Modulation"+": "))
        self._ch2_modulation_combo_box = Qt.QComboBox()
        self._ch2_modulation_tool_bar.addWidget(self._ch2_modulation_combo_box)
        for label in self._ch2_modulation_labels: self._ch2_modulation_combo_box.addItem(label)
        self._ch2_modulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ch2_modulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ch2_modulation_options.index(i)))
        self._ch2_modulation_callback(self.ch2_modulation)
        self._ch2_modulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ch2_modulation(self._ch2_modulation_options[i]))
        self.top_grid_layout.addWidget(self._ch2_modulation_tool_bar, 1,1,1,1)
        _ch2_invert_check_box = Qt.QCheckBox("Invert")
        self._ch2_invert_choices = {True: -1, False: 1}
        self._ch2_invert_choices_inv = dict((v,k) for k,v in self._ch2_invert_choices.iteritems())
        self._ch2_invert_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch2_invert_check_box, "setChecked", Qt.Q_ARG("bool", self._ch2_invert_choices_inv[i]))
        self._ch2_invert_callback(self.ch2_invert)
        _ch2_invert_check_box.stateChanged.connect(lambda i: self.set_ch2_invert(self._ch2_invert_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ch2_invert_check_box, 1,4,1,1)
        self._ch2_freq_tool_bar = Qt.QToolBar(self)
        self._ch2_freq_tool_bar.addWidget(Qt.QLabel("Ch2 Freq (MHz)"+": "))
        self._ch2_freq_line_edit = Qt.QLineEdit(str(self.ch2_freq))
        self._ch2_freq_tool_bar.addWidget(self._ch2_freq_line_edit)
        self._ch2_freq_line_edit.returnPressed.connect(
        	lambda: self.set_ch2_freq(eng_notation.str_to_num(str(self._ch2_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._ch2_freq_tool_bar, 1,0,1,1)
        self._ch1_volume_range = Range(0, 10, 1, 1, 100)
        self._ch1_volume_win = RangeWidget(self._ch1_volume_range, self.set_ch1_volume, "Volume", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ch1_volume_win, 0,2,1,1)
        self._ch1_squelch_range = Range(-70, 0, 10, -30, 100)
        self._ch1_squelch_win = RangeWidget(self._ch1_squelch_range, self.set_ch1_squelch, "Squelch", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ch1_squelch_win, 0,3,1,1)
        _ch1_mute_check_box = Qt.QCheckBox("Mute")
        self._ch1_mute_choices = {True: 0, False: 1}
        self._ch1_mute_choices_inv = dict((v,k) for k,v in self._ch1_mute_choices.iteritems())
        self._ch1_mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch1_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._ch1_mute_choices_inv[i]))
        self._ch1_mute_callback(self.ch1_mute)
        _ch1_mute_check_box.stateChanged.connect(lambda i: self.set_ch1_mute(self._ch1_mute_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ch1_mute_check_box, 0,5,1,1)
        self._ch1_modulation_options = (0, 1, 2, )
        self._ch1_modulation_labels = ("DMR", "NBFM", "WBFM", )
        self._ch1_modulation_tool_bar = Qt.QToolBar(self)
        self._ch1_modulation_tool_bar.addWidget(Qt.QLabel("Modulation"+": "))
        self._ch1_modulation_combo_box = Qt.QComboBox()
        self._ch1_modulation_tool_bar.addWidget(self._ch1_modulation_combo_box)
        for label in self._ch1_modulation_labels: self._ch1_modulation_combo_box.addItem(label)
        self._ch1_modulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ch1_modulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ch1_modulation_options.index(i)))
        self._ch1_modulation_callback(self.ch1_modulation)
        self._ch1_modulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ch1_modulation(self._ch1_modulation_options[i]))
        self.top_grid_layout.addWidget(self._ch1_modulation_tool_bar, 0,1,1,1)
        _ch1_invert_check_box = Qt.QCheckBox("Invert")
        self._ch1_invert_choices = {True: -1, False: 1}
        self._ch1_invert_choices_inv = dict((v,k) for k,v in self._ch1_invert_choices.iteritems())
        self._ch1_invert_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch1_invert_check_box, "setChecked", Qt.Q_ARG("bool", self._ch1_invert_choices_inv[i]))
        self._ch1_invert_callback(self.ch1_invert)
        _ch1_invert_check_box.stateChanged.connect(lambda i: self.set_ch1_invert(self._ch1_invert_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ch1_invert_check_box, 0,4,1,1)
        self._ch1_freq_tool_bar = Qt.QToolBar(self)
        self._ch1_freq_tool_bar.addWidget(Qt.QLabel("Ch1 Freq (MHz)"+": "))
        self._ch1_freq_line_edit = Qt.QLineEdit(str(self.ch1_freq))
        self._ch1_freq_tool_bar.addWidget(self._ch1_freq_line_edit)
        self._ch1_freq_line_edit.returnPressed.connect(
        	lambda: self.set_ch1_freq(eng_notation.str_to_num(str(self._ch1_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._ch1_freq_tool_bar, 0,0,1,1)
        self.wbfm_chain_0_0_0 = wbfm_chain()
        self.wbfm_chain_0_0 = wbfm_chain()
        self.wbfm_chain_0 = wbfm_chain()
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(rf_gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=400000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=400000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=400000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self._radio_freq_tool_bar = Qt.QToolBar(self)
        self._radio_freq_tool_bar.addWidget(Qt.QLabel("Radio Freq (MHz)"+": "))
        self._radio_freq_line_edit = Qt.QLineEdit(str(self.radio_freq))
        self._radio_freq_tool_bar.addWidget(self._radio_freq_line_edit)
        self._radio_freq_line_edit.returnPressed.connect(
        	lambda: self.set_radio_freq(eng_notation.str_to_num(str(self._radio_freq_line_edit.text().toAscii()))))
        self.settings_grid_layout_0.addWidget(self._radio_freq_tool_bar, 0,0,1,1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 10,0,10,6)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	512, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	(ch3_freq * 1000000), #fc
        	400000, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0,0,1,1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	512, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	(ch2_freq * 1000000), #fc
        	400000, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win, 0,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	512, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	(ch1_freq * 1000000), #fc
        	400000, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.nbfm_chain_0_0_0 = nbfm_chain()
        self.nbfm_chain_0_0 = nbfm_chain()
        self.nbfm_chain_0 = nbfm_chain()
        self.freq_xlating_fft_filter_ccc_0_0_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), (ch3_freq * 1000000) - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), (ch2_freq * 1000000) - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), (ch1_freq * 1000000) - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.dsd_chain_0_0_0 = dsd_chain()
        self.dsd_chain_0_0 = dsd_chain()
        self.dsd_chain_0 = dsd_chain()
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/jason/Desktop/test.wav", 1, 48000, 8)
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_vff((ch3_invert * ch3_mute, ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((ch2_invert * ch2_mute, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((ch1_invert * ch1_mute, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((ch3_volume, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((ch2_volume, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((ch1_volume, ))
        self.blks2_selector_0_1_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=3,
        	input_index=0,
        	output_index=ch3_modulation,
        )
        self.blks2_selector_0_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=3,
        	input_index=0,
        	output_index=ch2_modulation,
        )
        self.blks2_selector_0_0_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=ch3_modulation,
        	output_index=0,
        )
        self.blks2_selector_0_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=ch2_modulation,
        	output_index=0,
        )
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=ch1_modulation,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=3,
        	input_index=0,
        	output_index=ch1_modulation,
        )
        self.audio_sink_0_0_0 = audio.sink(48000, "", True)
        self.audio_sink_0_0 = audio.sink(48000, "", True)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_pwr_squelch_xx_0_0_0_0 = analog.pwr_squelch_cc(ch3_squelch, 1e-4, 0, True)
        self.analog_pwr_squelch_xx_0_0_0 = analog.pwr_squelch_cc(ch2_squelch, 1e-4, 0, True)
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(ch1_squelch, 1e-4, 0, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_0, 0), (self.blks2_selector_0_1, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_0_0, 0), (self.blks2_selector_0_1_0, 0))    
        self.connect((self.blks2_selector_0, 0), (self.dsd_chain_0, 0))    
        self.connect((self.blks2_selector_0, 1), (self.nbfm_chain_0, 0))    
        self.connect((self.blks2_selector_0, 2), (self.wbfm_chain_0, 0))    
        self.connect((self.blks2_selector_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blks2_selector_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blks2_selector_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blks2_selector_0_1, 0), (self.dsd_chain_0_0, 0))    
        self.connect((self.blks2_selector_0_1, 1), (self.nbfm_chain_0_0, 0))    
        self.connect((self.blks2_selector_0_1, 2), (self.wbfm_chain_0_0, 0))    
        self.connect((self.blks2_selector_0_1_0, 0), (self.dsd_chain_0_0_0, 0))    
        self.connect((self.blks2_selector_0_1_0, 1), (self.nbfm_chain_0_0_0, 0))    
        self.connect((self.blks2_selector_0_1_0, 2), (self.wbfm_chain_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.audio_sink_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.audio_sink_0_0_0, 0))    
        self.connect((self.dsd_chain_0, 0), (self.blks2_selector_0_0, 0))    
        self.connect((self.dsd_chain_0_0, 0), (self.blks2_selector_0_0_0, 0))    
        self.connect((self.dsd_chain_0_0_0, 0), (self.blks2_selector_0_0_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.analog_pwr_squelch_xx_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))    
        self.connect((self.nbfm_chain_0, 0), (self.blks2_selector_0_0, 1))    
        self.connect((self.nbfm_chain_0_0, 0), (self.blks2_selector_0_0_0, 1))    
        self.connect((self.nbfm_chain_0_0_0, 0), (self.blks2_selector_0_0_0_0, 1))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.wbfm_chain_0, 0), (self.blks2_selector_0_0, 2))    
        self.connect((self.wbfm_chain_0_0, 0), (self.blks2_selector_0_0_0, 2))    
        self.connect((self.wbfm_chain_0_0_0, 0), (self.blks2_selector_0_0_0_0, 2))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "cp04aQT")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_radio_freq(self):
        return self.radio_freq

    def set_radio_freq(self, radio_freq):
        self.radio_freq = radio_freq
        self.set_ch1_freq(self.radio_freq)
        self.set_ch2_freq(self.radio_freq)
        self.set_ch3_freq(self.radio_freq)
        self.set_freq(self.radio_freq * 1000000)
        Qt.QMetaObject.invokeMethod(self._radio_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.radio_freq)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fft_filter_ccc_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.freq_xlating_fft_filter_ccc_0_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.freq_xlating_fft_filter_ccc_0_0_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.rtlsdr_source_0.set_gain(self.rf_gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.freq_xlating_fft_filter_ccc_0.set_center_freq((self.ch1_freq * 1000000) - self.freq)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq((self.ch2_freq * 1000000) - self.freq)
        self.freq_xlating_fft_filter_ccc_0_0_0.set_center_freq((self.ch3_freq * 1000000) - self.freq)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

    def get_ch3_volume(self):
        return self.ch3_volume

    def set_ch3_volume(self, ch3_volume):
        self.ch3_volume = ch3_volume
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.ch3_volume, ))

    def get_ch3_squelch(self):
        return self.ch3_squelch

    def set_ch3_squelch(self, ch3_squelch):
        self.ch3_squelch = ch3_squelch
        self.analog_pwr_squelch_xx_0_0_0_0.set_threshold(self.ch3_squelch)

    def get_ch3_mute(self):
        return self.ch3_mute

    def set_ch3_mute(self, ch3_mute):
        self.ch3_mute = ch3_mute
        self._ch3_mute_callback(self.ch3_mute)
        self.blocks_multiply_const_vxx_1_0_0.set_k((self.ch3_invert * self.ch3_mute, ))

    def get_ch3_modulation(self):
        return self.ch3_modulation

    def set_ch3_modulation(self, ch3_modulation):
        self.ch3_modulation = ch3_modulation
        self._ch3_modulation_callback(self.ch3_modulation)
        self.blks2_selector_0_0_0_0.set_input_index(int(self.ch3_modulation))
        self.blks2_selector_0_1_0.set_output_index(int(self.ch3_modulation))

    def get_ch3_invert(self):
        return self.ch3_invert

    def set_ch3_invert(self, ch3_invert):
        self.ch3_invert = ch3_invert
        self._ch3_invert_callback(self.ch3_invert)
        self.blocks_multiply_const_vxx_1_0_0.set_k((self.ch3_invert * self.ch3_mute, ))

    def get_ch3_freq(self):
        return self.ch3_freq

    def set_ch3_freq(self, ch3_freq):
        self.ch3_freq = ch3_freq
        Qt.QMetaObject.invokeMethod(self._ch3_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ch3_freq)))
        self.freq_xlating_fft_filter_ccc_0_0_0.set_center_freq((self.ch3_freq * 1000000) - self.freq)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range((self.ch3_freq * 1000000), 400000)

    def get_ch2_volume(self):
        return self.ch2_volume

    def set_ch2_volume(self, ch2_volume):
        self.ch2_volume = ch2_volume
        self.blocks_multiply_const_vxx_0_0.set_k((self.ch2_volume, ))

    def get_ch2_squelch(self):
        return self.ch2_squelch

    def set_ch2_squelch(self, ch2_squelch):
        self.ch2_squelch = ch2_squelch
        self.analog_pwr_squelch_xx_0_0_0.set_threshold(self.ch2_squelch)

    def get_ch2_mute(self):
        return self.ch2_mute

    def set_ch2_mute(self, ch2_mute):
        self.ch2_mute = ch2_mute
        self._ch2_mute_callback(self.ch2_mute)
        self.blocks_multiply_const_vxx_1_0.set_k((self.ch2_invert * self.ch2_mute, ))

    def get_ch2_modulation(self):
        return self.ch2_modulation

    def set_ch2_modulation(self, ch2_modulation):
        self.ch2_modulation = ch2_modulation
        self._ch2_modulation_callback(self.ch2_modulation)
        self.blks2_selector_0_0_0.set_input_index(int(self.ch2_modulation))
        self.blks2_selector_0_1.set_output_index(int(self.ch2_modulation))

    def get_ch2_invert(self):
        return self.ch2_invert

    def set_ch2_invert(self, ch2_invert):
        self.ch2_invert = ch2_invert
        self._ch2_invert_callback(self.ch2_invert)
        self.blocks_multiply_const_vxx_1_0.set_k((self.ch2_invert * self.ch2_mute, ))

    def get_ch2_freq(self):
        return self.ch2_freq

    def set_ch2_freq(self, ch2_freq):
        self.ch2_freq = ch2_freq
        Qt.QMetaObject.invokeMethod(self._ch2_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ch2_freq)))
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq((self.ch2_freq * 1000000) - self.freq)
        self.qtgui_freq_sink_x_0_0.set_frequency_range((self.ch2_freq * 1000000), 400000)

    def get_ch1_volume(self):
        return self.ch1_volume

    def set_ch1_volume(self, ch1_volume):
        self.ch1_volume = ch1_volume
        self.blocks_multiply_const_vxx_0.set_k((self.ch1_volume, ))

    def get_ch1_squelch(self):
        return self.ch1_squelch

    def set_ch1_squelch(self, ch1_squelch):
        self.ch1_squelch = ch1_squelch
        self.analog_pwr_squelch_xx_0_0.set_threshold(self.ch1_squelch)

    def get_ch1_mute(self):
        return self.ch1_mute

    def set_ch1_mute(self, ch1_mute):
        self.ch1_mute = ch1_mute
        self._ch1_mute_callback(self.ch1_mute)
        self.blocks_multiply_const_vxx_1.set_k((self.ch1_invert * self.ch1_mute, ))

    def get_ch1_modulation(self):
        return self.ch1_modulation

    def set_ch1_modulation(self, ch1_modulation):
        self.ch1_modulation = ch1_modulation
        self._ch1_modulation_callback(self.ch1_modulation)
        self.blks2_selector_0.set_output_index(int(self.ch1_modulation))
        self.blks2_selector_0_0.set_input_index(int(self.ch1_modulation))

    def get_ch1_invert(self):
        return self.ch1_invert

    def set_ch1_invert(self, ch1_invert):
        self.ch1_invert = ch1_invert
        self._ch1_invert_callback(self.ch1_invert)
        self.blocks_multiply_const_vxx_1.set_k((self.ch1_invert * self.ch1_mute, ))

    def get_ch1_freq(self):
        return self.ch1_freq

    def set_ch1_freq(self, ch1_freq):
        self.ch1_freq = ch1_freq
        Qt.QMetaObject.invokeMethod(self._ch1_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ch1_freq)))
        self.freq_xlating_fft_filter_ccc_0.set_center_freq((self.ch1_freq * 1000000) - self.freq)
        self.qtgui_freq_sink_x_0.set_frequency_range((self.ch1_freq * 1000000), 400000)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = cp04aQT()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
