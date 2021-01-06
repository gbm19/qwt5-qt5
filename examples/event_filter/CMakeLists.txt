
set( HEADERS
  "colorbar.h"
  "scalepicker.h"
  "canvaspicker.h"
  "plot.h"
  )
set( SRCS
  "colorbar.cpp"
  "scalepicker.cpp"
  "canvaspicker.cpp"
  "plot.cpp"
  "event_filter.cpp"
  )

add_executable( event_filter WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( event_filter qwt5-qt5 )
