
set( HEADERS
  "sliders.h"
  )
set( SRCS
  "sliders.cpp"
  )

add_executable( sliders WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( sliders qwt5-qt5 )
