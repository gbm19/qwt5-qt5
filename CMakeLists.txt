cmake_minimum_required( VERSION 3.16.3 )

project( qwt5-qt5
  VERSION 5.2.3
  DESCRIPTION "Qt Widgets for Technical Applications adapted to work with Qt5"
  HOMEPAGE_URL "https://github.com/gbm19/qwt5-qt5"
  LANGUAGES CXX )

include(GNUInstallDirs)

set( CMAKE_CXX_STANDARD 17)
set( CMAKE_CXX_STANDARD_REQUIRED TRUE )
set( CMAKE_CXX_EXTENSIONS OFF )

set( CMAKE_AUTOUIC OFF )
set( CMAKE_AUTORCC OFF )
set( CMAKE_AUTOMOC ON )

find_package( Qt5
  COMPONENTS
  Core
  Gui
  Widgets
  PrintSupport
  REQUIRED
  )

option( QWT_PLOT "Enable all classes, that are needed to use the QwtPlot widget" ON )

option( QWT_WIDGETS "Enable all classes, that are needed to use the all other widgets \
  (sliders, dials, ...)" ON )

option( QWT_SVG_ITEM "Display SVG images on the plot canvas" ON )
if( QWT_SVG_ITEM )
  find_package( Qt5 COMPONENTS Svg REQUIRED )
endif()

option( QWT_DESIGNER "Build Designer Plugin" ON )
if( QWT_DESIGNER )
  find_package( Qt5 COMPONENTS Designer REQUIRED )
endif()

option( BUILD_EXAMPLES "Build Examples" ON )

add_subdirectory( src )

if( QWT_DESIGNER )
  add_subdirectory( designer )
endif()

if( BUILD_EXAMPLES )
  add_subdirectory( examples )
endif()

configure_file( "${CMAKE_CURRENT_SOURCE_DIR}/qwt5-qt5.pc.in" "${CMAKE_CURRENT_BINARY_DIR}/qwt5-qt5.pc" @ONLY )
install( FILES "${CMAKE_CURRENT_BINARY_DIR}/qwt5-qt5.pc" DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig )
