
if( QWT_PLOT )

  add_subdirectory( cpuplot )
  add_subdirectory( curvdemo1 )
  add_subdirectory( curvdemo2 )
  add_subdirectory( simple_plot )
  add_subdirectory( realtime_plot )
  add_subdirectory( spectrogram )
  add_subdirectory( histogram )
  
  if( QWT_WIDGETS )
    add_subdirectory( bode )
    add_subdirectory( data_plot )
    add_subdirectory( event_filter )
  endif()
  
  if( QWT_SVG_ITEM )
    add_subdirectory( svgmap )
  endif()

endif()

if( QWT_WIDGETS )
  add_subdirectory( sysinfo )
  add_subdirectory( radio )
  add_subdirectory( dials )
  add_subdirectory( sliders )
endif()
