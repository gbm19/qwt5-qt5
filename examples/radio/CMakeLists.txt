
set( HEADERS
  "radio.h"
  "ampfrm.h"
  "tunerfrm.h"
  )
set( SRCS
  "radio.cpp"
  "ampfrm.cpp"
  "tunerfrm.cpp"
  )

add_executable( radio WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( radio qwt5-qt5 )
