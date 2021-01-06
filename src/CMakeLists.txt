
set( HEADERS
  "qwt.h"
  "qwt_abstract_scale_draw.h"
  "qwt_array.h"
  "qwt_color_map.h"
  "qwt_clipper.h"
  "qwt_double_interval.h"
  "qwt_double_rect.h"
  "qwt_dyngrid_layout.h"
  "qwt_global.h"
  "qwt_layout_metrics.h"
  "qwt_math.h"
  "qwt_magnifier.h"
  "qwt_paint_buffer.h"
  "qwt_painter.h"
  "qwt_panner.h"
  "qwt_picker.h"
  "qwt_picker_machine.h"
  "qwt_polygon.h"
  "qwt_round_scale_draw.h"
  "qwt_scale_div.h"
  "qwt_scale_draw.h"
  "qwt_scale_engine.h"
  "qwt_scale_map.h"
  "qwt_spline.h"
  "qwt_symbol.h"
  "qwt_text_engine.h"
  "qwt_text_label.h"
  "qwt_text.h"
  "qwt_valuelist.h"
  )

set( SRCS
  "qwt_abstract_scale_draw.cpp"
  "qwt_color_map.cpp"
  "qwt_clipper.cpp"
  "qwt_double_interval.cpp"
  "qwt_double_rect.cpp"
  "qwt_dyngrid_layout.cpp"
  "qwt_layout_metrics.cpp"
  "qwt_math.cpp"
  "qwt_magnifier.cpp"
  "qwt_paint_buffer.cpp"
  "qwt_panner.cpp"
  "qwt_painter.cpp"
  "qwt_picker.cpp"
  "qwt_round_scale_draw.cpp"
  "qwt_scale_div.cpp"
  "qwt_scale_draw.cpp"
  "qwt_scale_map.cpp"
  "qwt_spline.cpp"
  "qwt_text_engine.cpp"
  "qwt_text_label.cpp"
  "qwt_text.cpp"
  "qwt_event_pattern.cpp"
  "qwt_picker_machine.cpp"
  "qwt_scale_engine.cpp"
  "qwt_symbol.cpp"
  )

if( QWT_PLOT )
  list( APPEND HEADERS
    "qwt_curve_fitter.h"
    "qwt_data.h"
    "qwt_event_pattern.h"
    "qwt_interval_data.h"
    "qwt_legend.h"
    "qwt_legend_item.h"
    "qwt_legend_itemmanager.h"
    "qwt_plot.h"
    "qwt_plot_curve.h"
    "qwt_plot_dict.h"
    "qwt_plot_grid.h"
    "qwt_plot_item.h"
    "qwt_plot_layout.h"
    "qwt_plot_marker.h"
    "qwt_plot_printfilter.h"
    "qwt_plot_rasteritem.h"
    "qwt_plot_spectrogram.h"
    "qwt_plot_scaleitem.h"
    "qwt_plot_canvas.h"
    "qwt_plot_rescaler.h"
    "qwt_plot_panner.h"
    "qwt_plot_picker.h"
    "qwt_plot_zoomer.h"
    "qwt_plot_magnifier.h"
    "qwt_raster_data.h"
    "qwt_scale_widget.h"
    )
  list( APPEND SRCS
    "qwt_curve_fitter.cpp"
    "qwt_data.cpp"
    "qwt_interval_data.cpp"
    "qwt_legend.cpp"
    "qwt_legend_item.cpp"
    "qwt_plot.cpp"
    "qwt_plot_print.cpp"
    "qwt_plot_xml.cpp"
    "qwt_plot_axis.cpp"
    "qwt_plot_curve.cpp"
    "qwt_plot_dict.cpp"
    "qwt_plot_grid.cpp"
    "qwt_plot_item.cpp"
    "qwt_plot_spectrogram.cpp"
    "qwt_plot_scaleitem.cpp"
    "qwt_plot_marker.cpp"
    "qwt_plot_layout.cpp"
    "qwt_plot_printfilter.cpp"
    "qwt_plot_rasteritem.cpp"
    "qwt_plot_canvas.cpp"
    "qwt_plot_rescaler.cpp"
    "qwt_plot_panner.cpp"
    "qwt_plot_picker.cpp"
    "qwt_plot_zoomer.cpp"
    "qwt_plot_magnifier.cpp"
    "qwt_raster_data.cpp"
    "qwt_scale_widget.cpp"
    )
endif()

if( QWT_SVG_ITEM )
  list( APPEND HEADERS "qwt_plot_svgitem.h" )
  list( APPEND SRCS "qwt_plot_svgitem.cpp" )
endif()

if( QWT_WIDGETS )
  list( APPEND HEADERS
    "qwt_abstract_slider.h"
    "qwt_abstract_scale.h"
    "qwt_arrow_button.h"
    "qwt_analog_clock.h"
    "qwt_compass.h"
    "qwt_compass_rose.h"
    "qwt_counter.h"
    "qwt_dial.h"
    "qwt_dial_needle.h"
    "qwt_double_range.h"
    "qwt_knob.h"
    "qwt_slider.h"
    "qwt_thermo.h"
    "qwt_wheel.h"
    )
  list( APPEND SRCS
    "qwt_abstract_slider.cpp"
    "qwt_abstract_scale.cpp"
    "qwt_arrow_button.cpp"
    "qwt_analog_clock.cpp"
    "qwt_compass.cpp"
    "qwt_compass_rose.cpp"
    "qwt_counter.cpp"
    "qwt_dial.cpp"
    "qwt_dial_needle.cpp"
    "qwt_double_range.cpp"
    "qwt_knob.cpp"
    "qwt_slider.cpp"
    "qwt_thermo.cpp"
    "qwt_wheel.cpp"
    )
endif()

add_library( qwt5-qt5 ${SRCS} ${HEADERS} )

target_link_libraries( qwt5-qt5 Qt5::Core Qt5::Gui Qt5::Widgets Qt5::PrintSupport )

target_include_directories( qwt5-qt5 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} )

if( QWT_SVG_ITEM )
  target_link_libraries( qwt5-qt5 Qt5::Svg )
endif()

if( WIN32 AND BUILD_SHARED_LIBS )
  target_compile_definitions( qwt5-qt5 PUBLIC QT_DLL QWT_DLL QWT_MAKEDLL )
endif()

install( TARGETS qwt5-qt5
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  PUBLIC_HEADER DESTINATION include/qt5/qwt5-qt5
  )
install( DIRECTORY ${CMAKE_SOURCE_DIR}/doc/html/ DESTINATION ${CMAKE_INSTALL_DATADIR}/doc/qt5/html/qwt5-qt5 )
install( FILES ${HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/qt5/qwt5-qt5 )
# install( FILES doc/qwt-5.2.0.qch DESTINATION doc/qch )
if( UNIX )
  install( DIRECTORY ${CMAKE_SOURCE_DIR}/doc/man/ DESTINATION ${CMAKE_INSTALL_DATADIR}/man )
endif()
