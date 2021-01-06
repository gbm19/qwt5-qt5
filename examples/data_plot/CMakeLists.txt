
set( HEADERS
  "data_plot.h"
  )
set( SRCS
  "data_plot.cpp"
  "main.cpp"
  )

add_executable( data_plot WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( data_plot qwt5-qt5 )
