
set( HEADERS
  "bode.h"
  "bode_plot.h"
  "cplx.h"
  "pixmaps.h"
  )
set( SRCS
  "bode.cpp"
  "bode_plot.cpp"
  )

add_executable( bode WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( bode qwt5-qt5 )
