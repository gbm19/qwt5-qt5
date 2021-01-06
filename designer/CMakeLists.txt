
set( CMAKE_AUTORCC ON )

add_library( qwt5_designer_plugin SHARED
  "qwt_designer_plugin.cpp"
  "qwt_designer_plugin.h"
  "qwt_designer_plugin.qrc"
  )

if( QWT_PLOT )
  target_sources( qwt5_designer_plugin PRIVATE
    "qwt_designer_plotdialog.cpp"
    "qwt_designer_plotdialog.h"
    )
endif()

target_link_libraries( qwt5_designer_plugin qwt5-qt5 Qt5::Designer )

if( NOT QWT_PLOT )
  target_compile_definitions( qwt5_designer_plugin PRIVATE NO_QWT_PLOT )
endif()

if( NOT QWT_WIDGETS )
  target_compile_definitions( qwt5_designer_plugin PRIVATE NO_QWT_WIDGETS )
endif()

install( TARGETS qwt5_designer_plugin
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/qt5/plugins/designer
  )
