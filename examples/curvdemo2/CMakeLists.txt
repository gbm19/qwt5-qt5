
set( HEADERS
  "curvdemo2.h"
  )
set( SRCS
  "curvdemo2.cpp"
  )

add_executable( curvdemo2 WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( curvdemo2 qwt5-qt5 )
