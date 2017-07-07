%if ! 0%{?first_if:1}
  %define first_define first_body
  %if second_if
    %define second_define(o:) second_body
  %else
    %define second_else scond_else_body
    %if third_if
      %define third_if third_body
    %else
      # third else comment
    %endif
    # inter comment
    %if fourth_if
      # fourth if comment
      %if fifth_if
        # fifth if comment
      %endif
    %else
      # fourth else comment
    %endif
  %endif

%else
  %define secondelse(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif
