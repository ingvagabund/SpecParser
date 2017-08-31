metastring: "#60%0 %1\n  #00%0 %1 %3\n  #61%0 %1\n    #40%0\n  #61%5\n  #41%0\n  #62%0\
    \ %1\n    #42%0\n  #62%5\n  #63%0 %1\n    #43%0\n  #63%5    \n  #44%0\n#60%5\n"
comments:
  -   - '# comment jak svina'
      - condition:
          - if ! 0%{?first_if:1}
          - if druhej_if
  -   - '# problem 1'
      - condition:
          - if ! 0%{?first_if:1}
  -   - '# treti comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if treti_if
  -   - '#posledni comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if ctvrty_if
  -   - '# taky patri do prvni urovne'
      - condition:
          - if ! 0%{?first_if:1}
metadata:
  - '%first_define': first_body
    condition:
      - if ! 0%{?first_if:1}

