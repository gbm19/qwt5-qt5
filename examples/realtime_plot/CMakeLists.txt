
set( HEADERS
  "mainwindow.h"
  "scrollzoomer.h"
  "scrollbar.h"
  "incrementalplot.h"
  "randomplot.h"
  )
set( SRCS
  "mainwindow.cpp"
  "scrollzoomer.cpp"
  "scrollbar.cpp"
  "incrementalplot.cpp"
  "randomplot.cpp"
  "realtime.cpp"
  )

add_executable( realtime_plot WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( realtime_plot qwt5-qt5 )
