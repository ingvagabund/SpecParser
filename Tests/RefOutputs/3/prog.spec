%if ! 0%{?first_if:1}
  # problem 1
  # taky patri do prvni urovne

  %define first_define first_body

  %if druhej_if
    # comment jak svina
  %endif

  %if treti_if
    # treti comment
  %endif

  %if ctvrty_if
    #posledni comment
  %endif    
%endif

