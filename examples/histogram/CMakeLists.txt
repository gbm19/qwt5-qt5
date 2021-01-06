
set( HEADERS
  "histogram_item.h"
  )
set( SRCS
  "histogram_item.cpp"
  "main.cpp"
  )

add_executable( histogram WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( histogram qwt5-qt5 )
