unit_list:
  -   - condition:
          - if 0%{?with_devel}
        Summary: etcd golang devel libraries
      - BuildArch: noarch
        condition:
          - if 0%{?with_devel}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/alarm) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/auth) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/auth/authpb) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/client) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/client/integration) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/clientv3) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/clientv3/concurrency) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/clientv3/integration) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/clientv3/mirror) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/clientv3/naming) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/compactor) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/contrib/recipes) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/discovery) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/e2e) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/embed) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/error) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdctl/ctlv2) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdctl/ctlv2/command) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdctl/ctlv3) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdctl/ctlv3/command) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdmain) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/api) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/api/v2http) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/api/v2http/httptypes) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/api/v3rpc) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/api/v3rpc/rpctypes) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/auth) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/etcdserverpb) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/membership) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/etcdserver/stats) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/integration) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/lease) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/lease/leasehttp) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/lease/leasepb) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/mvcc) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/mvcc/backend) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/mvcc/mvccpb) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/adt) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/contention) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/cors) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/cpuutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/crc) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/expect) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/fileutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/flags) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/httputil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/idutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/ioutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/logutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/mock/mockstorage) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/mock/mockstore) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/mock/mockwait) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/monotime) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/netutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/osutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/pathutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/pbutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/report) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/runtime) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/schedule) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/stringutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/testutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/tlsutil) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/transport) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/types) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/pkg/wait) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/proxy/grpcproxy) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/proxy/grpcproxy/cache) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/proxy/httpproxy) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/proxy/tcpproxy) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/raft) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/raft/raftpb) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/raft/rafttest) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/rafthttp) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/snap) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/snap/snappb) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/store) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/tools/benchmark/cmd) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/tools/functional-tester/etcd-agent/client)
            = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/tools/functional-tester/etcd-runner/command)
            = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/version) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/wal) = %{version}-%{release}
      - condition:
          - if 0%{?with_devel}
        Provides: golang(%{import_path}/wal/walpb) = %{version}-%{release}
      - name: devel
        condition:
          - if 0%{?with_devel}
      - description: "golang development libraries for etcd, a highly-available key\
            \ value store for\nshared configuration."
        condition:
          - if 0%{?with_devel}
      - runtime:
            dependencies:
              - name: golang(github.com/bgentry/speakeasy)
              - name: golang(github.com/boltdb/bolt)
              - name: golang(github.com/cheggaaa/pb)
              - name: golang(github.com/cockroachdb/cmux)
              - name: golang(github.com/coreos/go-semver/semver)
              - name: golang(github.com/coreos/go-systemd/daemon)
              - name: golang(github.com/coreos/go-systemd/util)
              - name: golang(github.com/coreos/pkg/capnslog)
              - name: golang(github.com/dustin/go-humanize)
              - name: golang(github.com/ghodss/yaml)
              - name: golang(github.com/gogo/protobuf/proto)
              - name: golang(github.com/golang/protobuf/proto)
              - name: golang(github.com/google/btree)
              - name: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
              - name: golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
              - name: golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
              - name: golang(github.com/jonboulle/clockwork)
              - name: golang(github.com/karlseguin/ccache)
              - name: golang(github.com/kr/pty)
              - name: golang(github.com/olekukonko/tablewriter)
              - name: golang(github.com/prometheus/client_golang/prometheus)
              - name: golang(github.com/spf13/cobra)
              - name: golang(github.com/spf13/pflag)
              - name: golang(github.com/ugorji/go/codec)
              - name: golang(github.com/urfave/cli)
              - name: golang(github.com/xiang90/probing)
              - name: golang(golang.org/x/crypto/bcrypt)
              - name: golang(golang.org/x/net/context)
              - name: golang(golang.org/x/net/http2)
              - name: golang(golang.org/x/time/rate)
              - name: golang(google.golang.org/grpc)
              - name: golang(google.golang.org/grpc/codes)
              - name: golang(google.golang.org/grpc/credentials)
              - name: golang(google.golang.org/grpc/grpclog)
              - name: golang(google.golang.org/grpc/metadata)
              - name: golang(google.golang.org/grpc/naming)
  -   - condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
        Summary: Unit tests for %{name} package
      - name: unit-test
        condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
      - description: "%{summary}\n\nThis package contains unit tests for project\n\
            providing packages with %{import_path} prefix."
        condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
      - buildtime:
            dependencies:
              - name: '%{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}'
      - runtime:
            dependencies:
              - name: '%{name}-devel = %{version}-%{release}'
  -   - files:
            meta:
                file: devel.file-list
            list:
              - '%license LICENSE'
              - '%doc *.md'
              - '%doc glide.lock'
              - '%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}'
        condition:
          - if 0%{?with_devel}
  -   - files:
            meta:
                file: unit-test.file-list
            list:
              - '%license LICENSE'
              - '%doc *.md'
        condition:
          - if 0%{?with_unit_test}
metastring: "#60%0 %1\n#012%0 %1 %3\n#013%0 %1 %3\n#014%0 %1 %3\n#40%0\n#41%0\n#015%0\
    \ %1 %3\n#016%0 %1 %3\n#60%3\n#017%0 %1 %3\n#018%0 %1 %3\n#019%0 %1 %3\n#020%0\
    \ %1 %3\n#021%0 %1 %3\n#60%5\n\n#61%0 %1\n#0130%0 %1 %3\n#61%3\n#0131%0 %1   %3\n\
    #61%5\n\n#62%0 %1\n#0132%0 %1%2 %3 \n#62%5\n\n#0133%0 %1        %3\n#0134%0 %1\
    \    %3\n#0135%0 %1         %3\n#0136%0 %1            %3\n#42%0\n#0137%0 %1 %3\n\
    #0138%0 %1     %3\n#0139%0 %1          %3\n#0140%0 %1     %3\n\n#00%0\t\t%2\n\
    #01%0\t%2\n#02%0\t%2\n#03%0\t%2\n#04%0\t%2\n#05%0\t\t%2\n#06%0\t%2\n#07%0\t%2\n\
    #08%0\t%2\n#09%0         %2\n#010%0         %2\n\n#43%0\n#011%0  %2\n#44%0\n#10[12]%0\
    \  %2\n\n#63%0 %1\n#11[13]%0 %2\n#12[14]%0 %2\n#13[15]%0 %2\n#14[16]%0 %2\n#15[17]%0\
    \ %2\n#16[18]%0 %2\n#17[19]%0 %2\n#18[20]%0 %2\n#19[21]%0 %2\n#110[22]%0 %2\n\
    #111[23]%0 %2\n#112[24]%0 %2\n#113[25]%0 %2\n#114[26]%0 %2\n#115[27]%0 %2\n#116[28]%0\
    \ %2\n#117[29]%0 %2\n#118[30]%0 %2\n#119[31]%0 %2\n#120[32]%0 %2\n#121[33]%0 %2\n\
    #122[34]%0 %2\n#123[35]%0 %2\n#124[36]%0 %2\n#125[37]%0 %2\n#126[38]%0 %2\n#127[39]%0\
    \ %2\n#128[40]%0 %2\n#129[41]%0 %2\n#130[42]%0 %2\n#131[43]%0 %2\n#132[44]%0 %2\n\
    #133[45]%0 %2\n#134[46]%0 %2\n#135[47]%0 %2\n#136[48]%0 %2\n#137[49]%0 %2\n#63%5\n\
    \n#138[50]%0\t%2\n\n#139[51]%0%1\t%2\n#140[52]%0%1 %2\n#141[53]%0%1 %2\n#142[54]%0%1\
    \ %2\n\n#179%0\n%4\n\n#64%0 %1\n#2125[1]%0 %3\n#055%0        %2\n#056%0      %2\n\
    \n#65%0 %1\n#143[57]%0 %2\n#144[58]%0 %2\n#145[59]%0 %2\n#146[60]%0 %2\n#147[61]%0\
    \ %2\n#148[62]%0 %2\n#149[63]%0 %2\n#150[64]%0 %2\n#151[65]%0 %2\n#152[66]%0 %2\n\
    #153[67]%0 %2\n#154[68]%0 %2\n#155[69]%0 %2\n#156[70]%0 %2\n#157[71]%0 %2\n#158[72]%0\
    \ %2\n#159[73]%0 %2\n#160[74]%0 %2\n#161[75]%0 %2\n#162[76]%0 %2\n#163[77]%0 %2\n\
    #164[78]%0 %2\n#165[79]%0 %2\n#166[80]%0 %2\n#167[81]%0 %2\n#168[82]%0 %2\n#169[83]%0\
    \ %2\n#170[84]%0 %2\n#171[85]%0 %2\n#172[86]%0 %2\n#173[87]%0 %2\n#174[88]%0 %2\n\
    #175[89]%0 %2\n#176[90]%0 %2\n#177[91]%0 %2\n#178[92]%0 %2\n#65%5\n\n#093%0 %2\n\
    #094%0 %2\n#095%0 %2\n#096%0 %2\n#097%0 %2\n#098%0 %2\n#099%0 %2\n#0100%0 %2\n\
    #0101%0 %2\n#0102%0 %2\n#0103%0 %2\n#0104%0 %2\n#0105%0 %2\n#0106%0 %2\n#0107%0\
    \ %2\n#0108%0 %2\n#0109%0 %2\n#0110%0 %2\n#0111%0 %2\n#0112%0 %2\n#0113%0 %2\n\
    #0114%0 %2\n#0115%0 %2\n#0116%0 %2\n#0117%0 %2\n#0118%0 %2\n#0119%0 %2\n#10[12]0%0\
    \ %2\n#10[12]1%0 %2\n#10[12]2%0 %2\n#10[12]3%0 %2\n#10[12]4%0 %2\n#10[12]5%0 %2\n\
    #10[12]6%0 %2\n#10[12]7%0 %2\n#10[12]8%0 %2\n\n#10[12]9%0 %2\n#11[13]0%0 %2\n\
    #11[13]1%0 %2\n#11[13]2%0 %2\n#11[13]3%0 %2\n#11[13]4%0 %2\n#11[13]5%0 %2\n#11[13]6%0\
    \ %2\n#11[13]7%0 %2\n#11[13]8%0 %2\n#11[13]9%0 %2\n#12[14]0%0 %2\n#12[14]1%0 %2\n\
    #12[14]2%0 %2\n#12[14]3%0 %2\n#12[14]4%0 %2\n#12[14]5%0 %2\n#12[14]6%0 %2\n#12[14]7%0\
    \ %2\n#12[14]8%0 %2\n#12[14]9%0 %2\n#13[15]0%0 %2\n#13[15]1%0 %2\n#13[15]2%0 %2\n\
    #13[15]3%0 %2\n#13[15]4%0 %2\n#13[15]5%0 %2\n#13[15]6%0 %2\n#13[15]7%0 %2\n#13[15]8%0\
    \ %2\n#13[15]9%0 %2\n#14[16]0%0 %2\n#14[16]1%0 %2\n#14[16]2%0 %2\n#14[16]3%0 %2\n\
    #14[16]4%0 %2\n#14[16]5%0 %2\n#14[16]6%0 %2\n#14[16]7%0 %2\n#14[16]8%0 %2\n#14[16]9%0\
    \ %2\n#15[17]0%0 %2\n#15[17]1%0 %2\n#15[17]2%0 %2\n#15[17]3%0 %2\n#15[17]4%0 %2\n\
    #15[17]5%0 %2\n#15[17]6%0 %2\n#15[17]7%0 %2\n#15[17]8%0 %2\n#15[17]9%0 %2\n#16[18]0%0\
    \ %2\n#16[18]1%0 %2\n#16[18]2%0 %2\n#16[18]3%0 %2\n#16[18]4%0 %2\n#16[18]5%0 %2\n\
    #16[18]6%0 %2\n#16[18]7%0 %2\n#16[18]8%0 %2\n#16[18]9%0 %2\n#17[19]0%0 %2\n#17[19]1%0\
    \ %2\n#17[19]2%0 %2\n#17[19]3%0 %2\n#17[19]4%0 %2\n#17[19]5%0 %2\n#17[19]6%0 %2\n\
    #17[19]7%0 %2\n#17[19]8%0 %2\n#17[19]9%0 %2\n#18[20]0%0 %2\n#18[20]1%0 %2\n#18[20]2%0\
    \ %2\n#18[20]3%0 %2\n#18[20]4%0 %2\n#18[20]5%0 %2\n#18[20]6%0 %2\n#18[20]7%0 %2\n\
    #18[20]8%0 %2\n#18[20]9%0 %2\n#19[21]0%0 %2\n#19[21]1%0 %2\n#19[21]2%0 %2\n\n\
    #2126[2]%0 %1\n%4\n#2125[1]%4#64%5\n\n#66%0 %1\n#2127[3]%0 %3\n#19[21]3%0    \
    \     %2\n#45%0\n#19[21]4%0  %2\n\n#67%0 %1\n#46%0\n#47%0\n#67%5\n\n#48%0\n#19[21]5%0\
    \        %2\n\n#2128[4]%0 %1\n%4\n#2127[3]%4#66%5\n\n#184%0\n%4\n\n#185%0\n%4\n\
    \n#186%0\n%4\n\n#187%0\n%4\n\n#188%0\n%4\n\n#189%0\n%4\n\n#190%0\n%4\n\n#191%0\n\
    %4\n#30%0%1#0141%0 %1 %3#30%3\n\n#192%0\n%40\n%41\n%42\n%43\n%44\n%45\n%46\n\n\
    #68%0 %1\n#2129[14]%0 %1 %2 %3\n%40\n%41\n%42\n%43\n#68%5\n\n#69%0 %1\n#2130[15]%0\
    \ %1 %2 %3\n%40\n%41\n#69%5\n\n#30%0\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n"
main_unit:
  - description: A highly-available key value store for shared configuration.
  - prep: "%setup -q -n %{name}-%{commit}\n# move content of vendor under Godeps as\
        \ has been so far\nmkdir -p Godeps/_workspace/src\nmv cmd/vendor/* Godeps/_workspace/src/.\n\
        \n%patch2 -p1\n%patch3 -p1"
  - build: "mkdir -p src/github.com/coreos\nln -s ../../../ src/github.com/coreos/etcd\n\
        \n%if ! 0%{?with_bundled}\nexport GOPATH=$(pwd):%{gopath}\n%else\nexport GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{gopath}\n\
        %endif\n\nexport LDFLAGS=\"-X %{import_path}/version.GitSHA=%{shortcommit}\"\
        \n%gobuild -o bin/etcd %{import_path}/cmd/etcd\n%gobuild -o bin/etcdctl %{import_path}/etcdctl"
  - install: "install -D -p -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}\ninstall\
        \ -D -p -m 0755 bin/%{name}ctl %{buildroot}%{_bindir}/%{name}ctl\ninstall\
        \ -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service\ninstall\
        \ -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}\ninstall -m 644 -t %{buildroot}%{_sysconfdir}/%{name}\
        \ %{SOURCE2}\n\n# And create /var/lib/etcd\ninstall -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}\n\
        \n# source codes for building projects\n%if 0%{?with_devel}\ninstall -d -p\
        \ %{buildroot}/%{gopath}/src/%{import_path}/\necho \"%%dir %%{gopath}/src/%%{import_path}/.\"\
        \ >> devel.file-list\n# find all *.go but no *_test.go files and generate\
        \ devel.file-list\nfor file in $(find . -iname \"*.go\" \\! -iname \"*_test.go\"\
        ) ; do\n    echo \"%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)\"\
        \ >> devel.file-list\n    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname\
        \ $file)\n    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file\n\
        \    echo \"%%{gopath}/src/%%{import_path}/$file\" >> devel.file-list\ndone\n\
        %endif\n\n# testing files for this project\n%if 0%{?with_unit_test} && 0%{?with_devel}\n\
        install -d -p %{buildroot}/%{gopath}/src/%{import_path}/\n# find all *_test.go\
        \ files and generate unit-test.file-list\nfor file in $(find . -iname \"*_test.go\"\
        ); do\n    echo \"%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)\"\
        \ >> devel.file-list\n    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname\
        \ $file)\n    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file\n\
        \    echo \"%%{gopath}/src/%%{import_path}/$file\" >> unit-test.file-list\n\
        done\n\ninstall -dp %{buildroot}/%{gopath}/src/%{import_path}/integration/\n\
        cp -rpav integration/fixtures %{buildroot}/%{gopath}/src/%{import_path}/integration/.\n\
        echo \"%%{gopath}/src/%%{import_path}/integration/fixtures\" >> unit-test.file-list\n\
        \ninstall -dp %{buildroot}/%{gopath}/src/%{import_path}/etcdserver/api/v2http/testdata\n\
        cp -rpav etcdserver/api/v2http/testdata %{buildroot}/%{gopath}/src/%{import_path}/etcdserver/api/v2http/.\n\
        echo \"%%{gopath}/src/%%{import_path}/etcdserver/api/v2http/testdata\" >>\
        \ unit-test.file-list\n%endif\n\n%if 0%{?with_devel}\nsort -u -o devel.file-list\
        \ devel.file-list\n%endif"
  - check: "%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}\n%if ! 0%{?with_bundled}\n\
        export GOPATH=%{buildroot}/%{gopath}:%{gopath}\n%else\nexport GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}\n\
        %endif\n\n%if ! 0%{?gotest:1}\n%global gotest go test\n%endif\n\n%ifarch x86_64\n\
        RACE=\"--race\"\n%else\nRACE=\"\"\n%endif\n\n# unit-tests\n# TODO(jchaloup):\
        \ read all the envs from test file\nexport IGNORE_PKGS=\"(cmd|vendor|etcdserverpb|rafttest)\"\
        \nexport INTEGRATION_PKGS=\"(integration|e2e|contrib|functional-tester)\"\n\
        export TEST_PKGS=`find . -name \\*_test.go | while read a; do dirname $a;\
        \ done | sort | uniq | egrep -v \"$IGNORE_PKGS\" | sed \"s|\\./||g\"`\nexport\
        \ TESTS=`echo \"$TEST_PKGS\" | egrep -v \"$INTEGRATION_PKGS\"`\n\nfor test\
        \ in ${TESTS}; do\n%gotest -timeout 3m -cover ${RACE} -cpu 1,2,4 -run=Test\
        \ github.com/coreos/etcd/${test}\ndone\n\n./test\n\n%endif"
  - pre: "getent group %{name} >/dev/null || groupadd -r %{name}\ngetent passwd %{name}\
        \ >/dev/null || useradd -r -g %{name} -d %{_sharedstatedir}/%{name} \\\n\t\
        -s /sbin/nologin -c \"etcd user\" %{name}"
  - post: '%systemd_post %{name}.service'
  - preun: '%systemd_preun %{name}.service'
  - postun: "%systemd_postun %{name}.service\n\n#define license tag if not already\
        \ defined"
  - files:
        list:
          - '%license LICENSE'
          - '%doc *.md'
          - '%config(noreplace) %{_sysconfdir}/%{name}'
          - '%{_bindir}/%{name}'
          - '%{_bindir}/%{name}ctl'
          - '%dir %attr(-,%{name},%{name}) %{_sharedstatedir}/%{name}'
          - '%{_unitdir}/%{name}.service'
  - buildtime:
        dependencies:
          - name: golang(google.golang.org/grpc/naming)
          - name: golang(google.golang.org/grpc/metadata)
          - name: golang(google.golang.org/grpc/grpclog)
          - name: golang(google.golang.org/grpc/credentials)
          - name: golang(google.golang.org/grpc/codes)
          - name: golang(google.golang.org/grpc)
          - name: golang(golang.org/x/time/rate)
          - name: golang(golang.org/x/net/http2)
          - name: golang(golang.org/x/net/context)
          - name: golang(golang.org/x/crypto/bcrypt)
          - name: golang(github.com/xiang90/probing)
          - name: golang(github.com/urfave/cli)
          - name: golang(github.com/ugorji/go/codec)
          - name: golang(github.com/spf13/pflag)
          - name: golang(github.com/spf13/cobra)
          - name: golang(github.com/prometheus/client_golang/prometheus)
          - name: golang(github.com/olekukonko/tablewriter)
          - name: golang(github.com/kr/pty)
          - name: golang(github.com/karlseguin/ccache)
          - name: golang(github.com/jonboulle/clockwork)
          - name: golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
          - name: golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
          - name: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
          - name: golang(github.com/google/btree)
          - name: golang(github.com/golang/protobuf/proto)
          - name: golang(github.com/gogo/protobuf/proto)
          - name: golang(github.com/ghodss/yaml)
          - name: golang(github.com/dustin/go-humanize)
          - name: golang(github.com/coreos/pkg/capnslog)
          - name: golang(github.com/coreos/go-systemd/util)
          - name: golang(github.com/coreos/go-systemd/daemon)
          - name: golang(github.com/coreos/go-semver/semver)
          - name: golang(github.com/cockroachdb/cmux)
          - name: golang(github.com/cheggaaa/pb)
          - name: golang(github.com/boltdb/bolt)
          - name: golang(github.com/bgentry/speakeasy)
          - name: systemd
          - name: golang(google.golang.org/grpc/transport)
          - name: golang(google.golang.org/grpc/naming)
          - name: golang(google.golang.org/grpc/metadata)
          - name: golang(google.golang.org/grpc/grpclog)
          - name: golang(google.golang.org/grpc/credentials)
          - name: golang(google.golang.org/grpc/codes)
          - name: golang(google.golang.org/grpc)
          - name: golang(golang.org/x/time/rate)
          - name: golang(golang.org/x/net/http2)
          - name: golang(golang.org/x/net/context)
          - name: golang(golang.org/x/crypto/bcrypt)
          - name: golang(github.com/xiang90/probing)
          - name: golang(github.com/urfave/cli)
          - name: golang(github.com/ugorji/go/codec)
          - name: golang(github.com/spf13/pflag)
          - name: golang(github.com/spf13/cobra)
          - name: golang(github.com/prometheus/client_golang/prometheus)
          - name: golang(github.com/olekukonko/tablewriter)
          - name: golang(github.com/kr/pty)
          - name: golang(github.com/karlseguin/ccache)
          - name: golang(github.com/jonboulle/clockwork)
          - name: golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
          - name: golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
          - name: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
          - name: golang(github.com/google/btree)
          - name: golang(github.com/golang/protobuf/proto)
          - name: golang(github.com/gogo/protobuf/proto)
          - name: golang(github.com/ghodss/yaml)
          - name: golang(github.com/dustin/go-humanize)
          - name: golang(github.com/coreos/pkg/capnslog)
          - name: golang(github.com/coreos/go-systemd/util)
          - name: golang(github.com/coreos/go-systemd/daemon)
          - name: golang(github.com/coreos/go-semver/semver)
          - name: golang(github.com/cockroachdb/cmux)
          - name: golang(github.com/cheggaaa/pb)
          - name: golang(github.com/boltdb/bolt)
          - name: golang(github.com/bgentry/speakeasy)
          - name: '%{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}'
  - runtime:
        dependencies:
          - name: systemd
          - name: systemd
          - name: systemd
          - name: shadow-utils
history:
    '60':
        comment: '- https://fedoraproject.org/wiki/Changes/golang1.7'
        date: Thu Jul 21 2016
        mark: '- 3.0.0-0.2.beta0'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '61':
        comment: "- Update to 3.0.2\n  resolves: #1351818"
        date: Thu Jul 28 2016
        mark: '- 3.0.2-1'
        author: jchaloup <jchaloup@redhat.com>
    '62':
        comment: "- Update to 3.0.4\n  related: #1351818"
        date: Tue Aug 02 2016
        mark: '- 3.0.4-1'
        author: jchaloup <jchaloup@redhat.com>
    '63':
        comment: "- Hack test to provide ability to run unit-tests and integration\
            \ tests\n  Still, keeping it disabled by default as it keeps failing\n\
            \  related: #1351818"
        date: Tue Aug 16 2016
        mark: '- 3.0.4-2'
        author: jchaloup <jchaloup@redhat.com>
    '64':
        comment: "- Update to v3.0.7\n  resolves: #1370678"
        date: Fri Sep 09 2016
        mark: '- 3.0.7-1'
        author: jchaloup <jchaloup@redhat.com>
    '65':
        comment: "- Update to v3.0.8\n  resolves: #1374880"
        date: Wed Sep 14 2016
        mark: '- 3.0.8-1'
        author: jchaloup <jchaloup@redhat.com>
    '66':
        comment: "- Update to v3.0.9\n  related: #1374880"
        date: Fri Sep 16 2016
        mark: '- 3.0.9-1'
        author: jchaloup <jchaloup@redhat.com>
    '67':
        comment: "- Update to v3.0.12\n  related: #1382965"
        date: Thu Oct 13 2016
        mark: '- 3.0.12-1'
        author: jchaloup <jchaloup@redhat.com>
    '68':
        comment: '- Extend supported architectures with s390x'
        date: Mon Oct 24 2016
        mark: '- 3.0.12-2'
        author: jchaloup <jchaloup@redhat.com>
    '69':
        comment: "- Update to v3.0.13\n  related: #1382965"
        date: Thu Oct 27 2016
        mark: '- 3.0.13-1'
        author: jchaloup <jchaloup@redhat.com>
    '24':
        comment: "- Update to v2.0.8\n  resolves: #1207881"
        date: Wed Apr 01 2015
        mark: '- 2.0.8-0.1'
        author: jchaloup <jchaloup@redhat.com>
    '25':
        comment: "- Update spec file to fit for rhel too (thanks to eparis)\n  related:\
            \ #1207881"
        date: Fri Apr 03 2015
        mark: '- 2.0.8-0.2'
        author: jchaloup <jchaloup@redhat.com>
    '26':
        comment: "- Update to v2.0.9\n  resolves: #1209666"
        date: Wed Apr 08 2015
        mark: '- 2.0.9-1'
        author: jchaloup <jchaloup@redhat.com>
    '27':
        comment: "- Update to v2.0.10\n  resolves: #1214705"
        date: Thu Apr 23 2015
        mark: '- 2.0.10-1'
        author: jchaloup <jchaloup@redhat.com>
    '20':
        comment: '- Bump to upstream 4d728cc8c488a545a8bdeafd054d9ccc2bfb6876'
        date: Fri Feb 20 2
        mark: '- 2.0.3-0.1'
        author: 015 jchaloup <jchaloup@redhat.com>
    '21':
        comment: '- Fix .service files to work if no config file'
        date: Tue Mar 10 2015
        mark: '- 2.0.3-0.2'
        author: Eric Paris <eparis@redhat.com>
    '22':
        comment: '- Bump to 9481945228b97c5d019596b921d8b03833964d9e (v2.0.5)'
        date: Thu Mar 12 2015
        mark: '- 2.0.5-0.1'
        author: jchaloup <jchaloup@redhat.com>
    '23':
        comment: "- Update to v2.0.7\n  Add Godeps.json to doc\n  related: #1191441"
        date: Tue Mar 31 2015
        mark: '- 2.0.7-0.1'
        author: jchaloup <jchaloup@redhat.com>
    '28':
        comment: "- Update to v2.0.11\n  resolves: #1222416"
        date: Mon May 18 2015
        mark: '- 2.0.11-1'
        author: jchaloup <jchaloup@redhat.com>
    '29':
        comment: "- ETCD_ADVERTISE_CLIENT_URLS has to be set if ETCD_LISTEN_CLIENT_URLS\
            \ is\n  related: #1222416"
        date: Fri May 22 2015
        mark: '- 2.0.11-2'
        author: jchaloup <jchaloup@redhat.com>
    '0':
        comment: '- Initial creation'
        date: Mon Aug 26 2013
        mark: '- 0.1.1-1'
        author: Luke Cypret <cypret@fedoraproject.org>
    '2':
        comment: '- Fix typo in the etc.service file'
        date: Sat Oct 12 2013
        mark: '- 0.1.2-2'
        author: Peter Lemenkov <lemenkov@gmail.com>
    '4':
        comment: '- go.net library unbundled (see rhbz #1018476)'
        date: Sun Oct 13 2013
        mark: '- 0.1.2-4'
        author: Peter Lemenkov <lemenkov@gmail.com>
    '6':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild'
        date: Sat Jun 07 2014
        mark: '- 0.1.2-6'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '8':
        comment: '- Add devel sub-package'
        date: Tue Aug 19 2014
        mark: '- 0.4.6-3'
        author: Adam Miller <maxamillion@fedoraproject.org>
    '59':
        comment: "- Update to v3.0.0-beta0 (build from bundled until new deps appear\
            \ in dist-git)\n  resolves: #1333988"
        date: Sun May 15 2016
        mark: '- 3.0.0-0.1.beta0'
        author: jchaloup <jchaloup@redhat.com>
    '58':
        comment: "- Update to v2.3.3\n  resolves: #1331896"
        date: Sat Apr 30 2016
        mark: '- 2.3.3-1'
        author: jchaloup <jchaloup@redhat.com>
    '11':
        comment: "- related: #1047194\n  Remove dependency on go.net"
        date: Mon Oct 06 2014
        mark: '- 0.4.6-6'
        author: jchaloup <jchaloup@redhat.com>
    '10':
        comment: "- Fix the .service file so it can launch!\n  related: #1047194"
        date: Mon Oct 06 2014
        mark: '- 0.4.6-5'
        author: jchaloup <jchaloup@redhat.com>
    '13':
        comment: "- Resolves: rhbz#1176138 - update to v2.0.0-rc1\n- do not redefine\
            \ gopath\n- use jonboulle/clockwork from within Godeps"
        date: Tue Dec 23 2014
        mark: '- 2.0.0-0.1.rc1'
        author: Lokesh Mandvekar <lsm5@fedoraproject.org>
    '12':
        comment: '- Add ExclusiveArch for go_arches'
        date: Fri Oct 17 2014
        mark: '- 0.4.6-7'
        author: jchaloup <jchaloup@redhat.com>
    '15':
        comment: "- default to /var/lib/etcd/default.etcd as 2.0 uses that default\
            \ (f21 commit byt eparis)\n  related: #1176138\n  fix /etc/etcd/etcd.conf\
            \ path"
        date: Mon Jan 26 2015
        mark: '- 2.0.0-0.3.rc1'
        author: jchaloup <jchaloup@redhat.com>
    '14':
        comment: "- Update of BuildRequires/Requires, Provides and test\n  Add BuildRequire\
            \ on jonboulle/clockwork\n  related: #1176138"
        date: Tue Jan 20 2
        mark: '- 2.0.0-0.2.rc1'
        author: 015 jchaloup <jchaloup@redhat.com>
    '17':
        comment: "- Add missing debug info to binaries (patch from Jan Kratochvil)\n\
            \  resolves: #1184257"
        date: Mon Feb 09 2015
        mark: '- 2.0.0-0.5'
        author: jchaloup <jchaloup@redhat.com>
    '16':
        comment: "- Update to etcd-2.0.0\n- use gopath as the last directory to search\
            \ for source code\n  related: #1176138"
        date: Fri Jan 30 2015
        mark: '- 2.0.0-0.4'
        author: jchaloup <jchaloup@redhat.com>
    '19':
        comment: "- Update configuration and service file\n  Fix depricated ErrWrongType\
            \ after update of gogo/protobuf\n  related: #1191441"
        date: Wed Feb 18 2015
        mark: '- 2.0.1-0.2'
        author: jchaloup <jchaloup@redhat.com>
    '54':
        comment: "- Update to v.2.3.1\n  resolves: #1323375"
        date: Mon Apr 04 2016
        mark: '- 2.3.1-1'
        author: jchaloup <jchaloup@redhat.com>
    '57':
        comment: "- Update to v2.3.2\n  resolves: #1329438"
        date: Fri Apr 22 2016
        mark: '- 2.3.2-1'
        author: jchaloup <jchaloup@redhat.com>
    '56':
        comment: '- Enable aarch64'
        date: Sat Apr  9 2016
        mark: 2.3.1-3
        author: Peter Robinson <pbrobinson@fedoraproject.org>
    '51':
        comment: "- Extend archs to all supported\n  resolves: #1315419"
        date: Tue Mar 08 2016
        mark: '- 2.2.5-3'
        author: jchaloup <jchaloup@redhat.com>
    '50':
        comment: '- https://fedoraproject.org/wiki/Changes/golang1.6'
        date: Mon Feb 22 2016
        mark: '- 2.2.5-2'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '53':
        comment: "- Update to v2.3.0\n  resolves: #1314441"
        date: Sun Mar 20 2
        mark: '- 2.3.0-1'
        author: 016 jchaloup <jchaloup@redhat.com>
    '52':
        comment: "- Only ppc64le is supported, ppc64 not\n  related: #1315419"
        date: Wed Mar 09 2016
        mark: '- 2.2.5-4'
        author: jchaloup <jchaloup@redhat.com>
    '55':
        comment: "- Don't apply patch (for tests only which are disabled atm)"
        date: Wed Apr 06 2016
        mark: '- 2.3.1-2'
        author: jchaloup <jchaloup@redhat.com>
    '18':
        comment: "- Update to 2.0.1\n  resolves: #1191441"
        date: Wed Feb 11 2015
        mark: '- 2.0.1-0.1'
        author: jchaloup <jchaloup@redhat.com>
    '48':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild'
        date: Wed Feb 03 2016
        mark: '- 2.2.4-2'
        author: Fedora Release Engineering <releng@fedoraproject.org>
    '49':
        comment: '- Update to v2.2.5'
        date: Thu Feb 18 2016
        mark: '- 2.2.5-1'
        author: jchaloup <jchaloup@redhat.com>
    '46':
        comment: "- Update to v2.2.3\n  resolves: #1296809"
        date: Fri Jan 08 2016
        mark: '- 2.2.3-1'
        author: jchaloup <jchaloup@redhat.com>
    '47':
        comment: "- Update to v2.2.4\n  resolves: #1300558"
        date: Thu Jan 21 2016
        mark: '- 2.2.4-1'
        author: jchaloup <jchaloup@redhat.com>
    '44':
        comment: '- Update to v2.2.2'
        date: Mon Dec 07 2015
        mark: '- 2.2.2-1'
        author: jchaloup <jchaloup@redhat.com>
    '45':
        comment: "- add missing options to etcd help (thanks to Joy Pu ypu@redhat.com)\n\
            - add more information when running etcd as a service"
        date: Tue Dec 29 2015
        mark: '- 2.2.2-2'
        author: jchaloup <jchaloup@redhat.com>
    '42':
        comment: "- Add After=network-online.target and Wants=network-online.target\n\
            \  to etcd.service"
        date: Fri Oct 30 2015
        mark: '- 2.2.1-3'
        author: jchaloup <jchaloup@redhat.com>
    '43':
        comment: '- Update etcd.conf: add new options, fix current'
        date: Mon Nov 16 2015
        mark: '- 2.2.1-4'
        author: jchaloup <jchaloup@redhat.com>
    '40':
        comment: "- Update to v2.2.1\n  resolves: #1272438"
        date: Fri Oct 16 2015
        mark: '- 2.2.1-1'
        author: jchaloup <jchaloup@redhat.com>
    '41':
        comment: "- Set Type=notify instead of simple in etcd.service (upstream #1576)\n\
            \  related: #1272438"
        date: Tue Oct 20 2
        mark: '- 2.2.1-2'
        author: 015 jchaloup <jchaloup@redhat.com>
    '1':
        comment: "- Ver. 0.1.2\n- Integrate with systemd"
        date: Sat Oct 12 2013
        mark: '- 0.1.2-1'
        author: Peter Lemenkov <lemenkov@gmail.com>
    '3':
        comment: "- Prepare for packages unbundling\n- Verbose build"
        date: Sat Oct 12 2013
        mark: '- 0.1.2-3'
        author: Peter Lemenkov <lemenkov@gmail.com>
    '5':
        comment: "- goprotobuf library unbundled (see rhbz #1018477)\n- go-log library\
            \ unbundled (see rhbz #1018478)\n- go-raft library unbundled (see rhbz\
            \ #1018479)\n- go-systemd library unbundled (see rhbz #1018480)\n- kardianos\
            \ library unbundled (see rhbz #1018481)"
        date: Sun Oct 20 2
        mark: '- 0.1.2-5'
        author: 013 Peter Lemenkov <lemenkov@gmail.com>
    '7':
        comment: "- Bump to 0.4.6\n- run as etcd, not root"
        date: Wed Aug 13 2014
        mark: '- 0.4.6-2'
        author: Eric Paris <eparis@redhat.com>
    '9':
        comment: "- resolves: #1047194\n  Update to 0.4.6 from https://github.com/projectatomic/etcd-package"
        date: Mon Sep 22 2014
        mark: '- 0.4.6-4'
        author: jchaloup <jchaloup@redhat.com>
    '77':
        comment: "- Update to 3.1.4\n  resolves: #1435028"
        date: Mon Mar 27 2017
        mark: '- 3.1.4-1'
        author: Jan Chaloupka <jchaloup@redhat.com>
    '76':
        comment: "- Update to v3.1.3\n  related: #1415341"
        date: Mon Mar 20 2
        mark: '- 3.1.3-1'
        author: 017 Jan Chaloupka <jchaloup@redhat.com>
    '75':
        comment: "- Update to v3.1.0\n  related: #1415341"
        date: Tue Mar 14 2017
        mark: '- 3.1.0-1'
        author: Jan Chaloupka <jchaloup@redhat.com>
    '74':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild'
        date: Fri Feb 10 2017
        mark: '- 3.0.17-2'
        author: Fedora Release Engineering <releng@fedoraproject.org>
    '73':
        comment: "- Update to v3.0.17\n  etcd-top removed by upstream\n  resolves:\
            \ #1415622"
        date: Mon Jan 23 2017
        mark: '- 3.0.17-1'
        author: Jan Chaloupka <jchaloup@redhat.com>
    '72':
        comment: "- Remove ppc64le architecture restriction\n  resolves: #1396463"
        date: Fri Nov 18 2016
        mark: '- 3.0.15-2'
        author: jchaloup <jchaloup@redhat.com>
    '71':
        comment: "- Update to v3.0.15\n  related: #1382965"
        date: Tue Nov 15 2016
        mark: '- 3.0.15-1'
        author: jchaloup <jchaloup@redhat.com>
    '70':
        comment: "- Update to v3.0.14\n  related: #1382965"
        date: Mon Nov 07 2016
        mark: '- 3.0.14-1'
        author: jchaloup <jchaloup@redhat.com>
    '79':
        comment: "- Update to 3.1.6\n  resolves: #1444068"
        date: Thu Apr 20 2
        mark: '- 3.1.6-1'
        author: 017 Jan Chaloupka <jchaloup@redhat.com>
    '78':
        comment: "- Update to 3.1.5\n  resolves: #1436452"
        date: Tue Mar 28 2017
        mark: '- 3.1.5-1'
        author: Jan Chaloupka <jchaloup@redhat.com>
    '39':
        comment: "- Update to v2.2.0 (etcd-migrate gone)\n- Update to spec-2.1\n \
            \ resolves: #1253864"
        date: Fri Sep 11 2015
        mark: '- 2.2.0-1'
        author: jchaloup <jchaloup@redhat.com>
    '38':
        comment: "- Update to v2.1.2\n  resolves: #1258599"
        date: Mon Aug 31 2015
        mark: '- 2.1.2-1'
        author: jchaloup <jchaloup@redhat.com>
    '33':
        comment: '- Update to v2.0.13'
        date: Fri Jun 26 2015
        mark: '- 2.0.13-1'
        author: jchaloup <jchaloup@redhat.com>
    '32':
        comment: "- Add restart policy and set LimitNOFILE to/in etcd.service file\n\
            - Update etcd.config file: add new flags and remove depricated\n- Update\
            \ 'go build' flags for GIT_SHA (used in build script)\n- Don't use 4001\
            \ and 7001 ports in etcd.conf, they are replaced with 2379 and 2380"
        date: Thu Jun 25 2015
        mark: '- 2.0.12-2'
        author: jchaloup <jchaloup@redhat.com>
    '31':
        comment: "- Update to v2.0.12\n- Polish spec file"
        date: Wed Jun 24 2015
        mark: '- 2.0.12-1'
        author: jchaloup <jchaloup@redhat.com>
    '30':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild'
        date: Wed Jun 17 2015
        mark: '- 2.0.11-3'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '37':
        comment: "- Enable debug info again\n  related: #1214958"
        date: Thu Jul 30 2015
        mark: '- 2.1.1-2'
        author: jchaloup <jchaloup@redhat.com>
    '36':
        comment: "- fix definition of GOPATH for go1.5\n- fix definition of gobuild\
            \ function for non-debug way\n- Update to v2.1.1\n  resolves: #1214958"
        date: Mon Jul 20 2
        mark: '- 2.1.1-1'
        author: 015 jchaloup <jchaloup@redhat.com>
    '35':
        comment: '- set GOMAXPROCS to use all processors available'
        date: Fri Jul 10 2015
        mark: '- 2.0.13-3'
        author: jchaloup <jchaloup@redhat.com>
    '34':
        comment: "- Remove -s option from -ldflags string as it removes symbol table\n\
            \  'go tool l6' gives explanation of all available options\n  resolves:\
            \ #1236320"
        date: Mon Jun 29 2015
        mark: '- 2.0.13-2'
        author: jchaloup <jchaloup@redhat.com>
comments:
  -   - '# Some tests fails and it takes a lot of time to investigate'
      - condition:
          - if 0%{?fedora}
  -   - '# what is wrong'
      - condition:
          - if 0%{?fedora}
  - '# https://github.com/coreos/etcd'
  - '# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required'
  - '# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.'
  -   - '# If go_compiler is not set to 1, there is no virtual provide. Use golang
        instead.'
      - condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
  -   - '#Here comes all BuildRequires: PACKAGE the unit tests'
      - condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
          - if 0%{?with_check}
  -   - '#in %%check section need for running'
      - condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
          - if 0%{?with_check}
  -   - '# test subpackage tests code from devel subpackage'
      - condition:
          - if 0%{?with_unit_test} && 0%{?with_devel}
metadata:
  - Name: '%{repo}'
  - Version: 3.1.6
  - Release: 1%{?dist}
  - Summary: A highly-available key value store for shared configuration
  - License: ASL 2.0
  - URL: https://%{provider_prefix}
  - Source0: https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
  - Source1: '%{name}.service'
  - Source2: '%{name}.conf'
  - Patch2: change-import-path.patch
  - Patch3: run-etcd-on-ppc64le-by-default.patch
  - ExclusiveArch: '%{ix86} x86_64 %{arm} aarch64 ppc64le s390x'
  - '%with_devel': '1'
    condition:
      - if 0%{?fedora}
  - '%with_bundled': '0'
    condition:
      - if 0%{?fedora}
  - condition:
      - if 0%{?fedora}
    '%with_debug': '1'
  - '%with_check': '0'
    condition:
      - if 0%{?fedora}
  - '%with_unit_test': '1'
    condition:
      - if 0%{?fedora}
  - '%with_devel': '0'
    condition:
      - if NOT 0%{?fedora}
  - '%with_bundled': '1'
    condition:
      - if NOT 0%{?fedora}
  - condition:
      - if NOT 0%{?fedora}
    '%with_debug': '0'
  - '%with_check': '0'
    condition:
      - if NOT 0%{?fedora}
  - '%with_unit_test': '0'
    condition:
      - if NOT 0%{?fedora}
  - '%_dwz_low_mem_die_limit': '0'
    condition:
      - if 0%{?with_debug}
  - '%debug_package': '%{nil}'
    condition:
      - if NOT 0%{?with_debug}
  - '%gobuild': go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An
        -tx1|tr -d ' \\n')" -a -v -x %{?**};
    condition:
      - if ! 0%{?gobuild:1}
  - '%provider': github
  - '%provider_tld': com
  - '%project': coreos
  - '%repo': etcd
  - '%provider_prefix': '%{provider}.%{provider_tld}/%{project}/%{repo}'
  - '%import_path': '%{provider_prefix}'
  - '%commit': e5b7ee2d03627ca33201da428b8110ef7c3e95f1
  - '%shortcommit': '%(c=%{commit}; echo ${c:0:7})'
  - '%license': '%doc'
    condition:
      - NOT _licensedir

