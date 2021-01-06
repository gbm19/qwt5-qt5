
set( HEADERS
  "plot.h"
  )
set( SRCS
  "plot.cpp"
  "main.cpp"
  )

add_executable( svgmap WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( svgmap qwt5-qt5 )
