metastring: "#60%0 %1\n  #00%0 %1 %3\n  #61%0 %1\n    #01%0 %1%2 %3\n  #61%3\n   \
    \ #02%0 %1 %3\n    #62%0 %1\n      #03%0 %1 %3\n    #62%3\n      #40%0\n    #62%5\n\
    \    #41%0\n    #63%0 %1\n      #42%0\n      #64%0 %1\n        #43%0\n      #64%5\n\
    \    #63%3\n      #44%0\n    #63%5\n  #61%5\n\n#60%3\n  #04%0 %1%2 %3 \n#60%5\n"
comments:
  -   - '# third else comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if NOT second_if
          - if NOT third_if
  -   - '# inter comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if NOT second_if
  -   - '# fourth if comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if NOT second_if
          - if fourth_if
  -   - '# fifth if comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if NOT second_if
          - if fourth_if
          - if fifth_if
  -   - '# fourth else comment'
      - condition:
          - if ! 0%{?first_if:1}
          - if NOT second_if
          - if NOT fourth_if
metadata:
  - '%first_define': first_body
    condition:
      - if ! 0%{?first_if:1}
  - condition:
      - if ! 0%{?first_if:1}
      - if second_if
    '%second_define': second_body
  - condition:
      - if ! 0%{?first_if:1}
      - if NOT second_if
    '%second_else': scond_else_body
  - '%third_if': third_body
    condition:
      - if ! 0%{?first_if:1}
      - if NOT second_if
      - if third_if
  - '%secondelse': go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od
        -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
    condition:
      - if NOT ! 0%{?first_if:1}

