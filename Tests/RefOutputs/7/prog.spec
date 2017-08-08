%if ! 0%{?first_if:1}
  %define first_define first_body
  %if druhej_if
    # comment jak svina
  %endif
  # problem 1
  %if treti_if
    # treti comment
  %endif
  %if ctvrty_if
    #posledni comment
  %endif    
  # taky patri do prvni urovne
%endif
