
set( HEADERS
  "attitude_indicator.h"
  "speedo_meter.h"
  "cockpit_grid.h"
  "compass_grid.h"
  )
set( SRCS
  "attitude_indicator.cpp"
  "speedo_meter.cpp"
  "cockpit_grid.cpp"
  "compass_grid.cpp"
  "dials.cpp"
  )

add_executable( dials WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( dials qwt5-qt5 )
