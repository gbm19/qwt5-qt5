
set( HEADERS
  "plot.h"
  )
set( SRCS
  "plot.cpp"
  "main.cpp"
  )

add_executable( spectrogram WIN32 ${HEADERS} ${SRCS} )

target_link_libraries( spectrogram qwt5-qt5 )
