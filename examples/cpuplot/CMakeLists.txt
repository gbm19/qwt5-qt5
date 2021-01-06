
set( HEADERS
  "cpuplot.h"
  "cpustat.h"
  "cpupiemarker.h"
  )
set( SRCS
  "cpuplot.cpp"
  "cpustat.cpp"
  "cpupiemarker.cpp"
  )

add_executable( cpuplot WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( cpuplot qwt5-qt5 )
