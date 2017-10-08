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
      - buildtime:
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
    \ %1 %3\n#021%0 %1 %3\n#60%5\n\n#61%0 %1\n#022%0 %1 %3\n#61%3\n#023%0 %1   %3\n\
    #61%5\n\n#62%0 %1\n#024%0 %1%2 %3 \n#62%5\n\n#025%0 %1        %3\n#026%0 %1  \
    \  %3\n#027%0 %1         %3\n#028%0 %1            %3\n#42%0\n#029%0 %1 %3\n#030%0\
    \ %1     %3\n#031%0 %1          %3\n#032%0 %1     %3\n\n#00[0]%0\t\t%2\n#01[1]%0\t\
    %2\n#02[2]%0\t%2\n#03[3]%0\t%2\n#04[4]%0\t%2\n#05[5]%0\t\t%2\n#06[6]%0\t%2\n#07[7]%0\t\
    %2\n#08[8]%0\t%2\n#09[9]%0         %2\n#010[10]%0         %2\n\n#43%0\n#011[11]%0\
    \  %2\n#44%0\n#10[12]%0  %2\n\n#63%0 %1\n#11[13]%0 %2\n#12[14]%0 %2\n#13[15]%0\
    \ %2\n#14[16]%0 %2\n#15[17]%0 %2\n#16[18]%0 %2\n#17[19]%0 %2\n#18[20]%0 %2\n#19[21]%0\
    \ %2\n#110[22]%0 %2\n#111[23]%0 %2\n#112[24]%0 %2\n#113[25]%0 %2\n#114[26]%0 %2\n\
    #115[27]%0 %2\n#116[28]%0 %2\n#117[29]%0 %2\n#118[30]%0 %2\n#119[31]%0 %2\n#120[32]%0\
    \ %2\n#121[33]%0 %2\n#122[34]%0 %2\n#123[35]%0 %2\n#124[36]%0 %2\n#125[37]%0 %2\n\
    #126[38]%0 %2\n#127[39]%0 %2\n#128[40]%0 %2\n#129[41]%0 %2\n#130[42]%0 %2\n#131[43]%0\
    \ %2\n#132[44]%0 %2\n#133[45]%0 %2\n#134[46]%0 %2\n#135[47]%0 %2\n#136[48]%0 %2\n\
    #137[49]%0 %2\n#63%5\n\n#138[50]%0\t%2\n\n#139[51]%0%1\t%2\n#140[52]%0%1 %2\n\
    #141[53]%0%1 %2\n#142[54]%0%1 %2\n\n#143[0]%0\n%4\n\n#64%0 %1\n#2<1>158[1]%0 %3\n\
    #2<1>0[55]%0        %2\n#2<1>1[56]%0      %2\n\n#65%0 %1\n#2<1>2[57]%0 %2\n#2<1>3[58]%0\
    \ %2\n#2<1>4[59]%0 %2\n#2<1>5[60]%0 %2\n#2<1>6[61]%0 %2\n#2<1>7[62]%0 %2\n#2<1>8[63]%0\
    \ %2\n#2<1>9[64]%0 %2\n#2<1>10[65]%0 %2\n#2<1>11[66]%0 %2\n#2<1>12[67]%0 %2\n\
    #2<1>13[68]%0 %2\n#2<1>14[69]%0 %2\n#2<1>15[70]%0 %2\n#2<1>16[71]%0 %2\n#2<1>17[72]%0\
    \ %2\n#2<1>18[73]%0 %2\n#2<1>19[74]%0 %2\n#2<1>20[75]%0 %2\n#2<1>21[76]%0 %2\n\
    #2<1>22[77]%0 %2\n#2<1>23[78]%0 %2\n#2<1>24[79]%0 %2\n#2<1>25[80]%0 %2\n#2<1>26[81]%0\
    \ %2\n#2<1>27[82]%0 %2\n#2<1>28[83]%0 %2\n#2<1>29[84]%0 %2\n#2<1>30[85]%0 %2\n\
    #2<1>31[86]%0 %2\n#2<1>32[87]%0 %2\n#2<1>33[88]%0 %2\n#2<1>34[89]%0 %2\n#2<1>35[90]%0\
    \ %2\n#2<1>36[91]%0 %2\n#2<1>37[92]%0 %2\n#65%5\n\n#2<1>38[93]%0 %2\n#2<1>39[94]%0\
    \ %2\n#2<1>40[95]%0 %2\n#2<1>41[96]%0 %2\n#2<1>42[97]%0 %2\n#2<1>43[98]%0 %2\n\
    #2<1>44[99]%0 %2\n#2<1>45[100]%0 %2\n#2<1>46[101]%0 %2\n#2<1>47[102]%0 %2\n#2<1>48[103]%0\
    \ %2\n#2<1>49[104]%0 %2\n#2<1>50[105]%0 %2\n#2<1>51[106]%0 %2\n#2<1>52[107]%0\
    \ %2\n#2<1>53[108]%0 %2\n#2<1>54[109]%0 %2\n#2<1>55[110]%0 %2\n#2<1>56[111]%0\
    \ %2\n#2<1>57[112]%0 %2\n#2<1>58[113]%0 %2\n#2<1>59[114]%0 %2\n#2<1>60[115]%0\
    \ %2\n#2<1>61[116]%0 %2\n#2<1>62[117]%0 %2\n#2<1>63[118]%0 %2\n#2<1>64[119]%0\
    \ %2\n#2<1>65[120]%0 %2\n#2<1>66[121]%0 %2\n#2<1>67[122]%0 %2\n#2<1>68[123]%0\
    \ %2\n#2<1>69[124]%0 %2\n#2<1>70[125]%0 %2\n#2<1>71[126]%0 %2\n#2<1>72[127]%0\
    \ %2\n#2<1>73[128]%0 %2\n\n#2<1>74[129]%0 %2\n#2<1>75[130]%0 %2\n#2<1>76[131]%0\
    \ %2\n#2<1>77[132]%0 %2\n#2<1>78[133]%0 %2\n#2<1>79[134]%0 %2\n#2<1>80[135]%0\
    \ %2\n#2<1>81[136]%0 %2\n#2<1>82[137]%0 %2\n#2<1>83[138]%0 %2\n#2<1>84[139]%0\
    \ %2\n#2<1>85[140]%0 %2\n#2<1>86[141]%0 %2\n#2<1>87[142]%0 %2\n#2<1>88[143]%0\
    \ %2\n#2<1>89[144]%0 %2\n#2<1>90[145]%0 %2\n#2<1>91[146]%0 %2\n#2<1>92[147]%0\
    \ %2\n#2<1>93[148]%0 %2\n#2<1>94[149]%0 %2\n#2<1>95[150]%0 %2\n#2<1>96[151]%0\
    \ %2\n#2<1>97[152]%0 %2\n#2<1>98[153]%0 %2\n#2<1>99[154]%0 %2\n#2<1>100[155]%0\
    \ %2\n#2<1>101[156]%0 %2\n#2<1>102[157]%0 %2\n#2<1>103[158]%0 %2\n#2<1>104[159]%0\
    \ %2\n#2<1>105[160]%0 %2\n#2<1>106[161]%0 %2\n#2<1>107[162]%0 %2\n#2<1>108[163]%0\
    \ %2\n#2<1>109[164]%0 %2\n#2<1>110[165]%0 %2\n#2<1>111[166]%0 %2\n#2<1>112[167]%0\
    \ %2\n#2<1>113[168]%0 %2\n#2<1>114[169]%0 %2\n#2<1>115[170]%0 %2\n#2<1>116[171]%0\
    \ %2\n#2<1>117[172]%0 %2\n#2<1>118[173]%0 %2\n#2<1>119[174]%0 %2\n#2<1>120[175]%0\
    \ %2\n#2<1>121[176]%0 %2\n#2<1>122[177]%0 %2\n#2<1>123[178]%0 %2\n#2<1>124[179]%0\
    \ %2\n#2<1>125[180]%0 %2\n#2<1>126[181]%0 %2\n#2<1>127[182]%0 %2\n#2<1>128[183]%0\
    \ %2\n#2<1>129[184]%0 %2\n#2<1>130[185]%0 %2\n#2<1>131[186]%0 %2\n#2<1>132[187]%0\
    \ %2\n#2<1>133[188]%0 %2\n#2<1>134[189]%0 %2\n#2<1>135[190]%0 %2\n#2<1>136[191]%0\
    \ %2\n#2<1>137[192]%0 %2\n#2<1>138[193]%0 %2\n#2<1>139[194]%0 %2\n#2<1>140[195]%0\
    \ %2\n#2<1>141[196]%0 %2\n#2<1>142[197]%0 %2\n#2<1>143[198]%0 %2\n#2<1>144[199]%0\
    \ %2\n#2<1>145[200]%0 %2\n#2<1>146[201]%0 %2\n#2<1>147[202]%0 %2\n#2<1>148[203]%0\
    \ %2\n#2<1>149[204]%0 %2\n#2<1>150[205]%0 %2\n#2<1>151[206]%0 %2\n#2<1>152[207]%0\
    \ %2\n#2<1>153[208]%0 %2\n#2<1>154[209]%0 %2\n#2<1>155[210]%0 %2\n#2<1>156[211]%0\
    \ %2\n#2<1>157[212]%0 %2\n\n#2<1>159[2]%0 %1\n%4\n#2<1>158[1]%4#64%5\n\n#66%0\
    \ %1\n#2<2>3[3]%0 %3\n#2<2>0[213]%0         %2\n#45%0\n#2<2>1[214]%0  %2\n\n#67%0\
    \ %1\n#46%0\n#47%0\n#67%5\n\n#48%0\n#2<2>2[215]%0        %2\n\n#2<2>4[4]%0 %1\n\
    %4\n#2<2>3[3]%4#66%5\n\n#144[5]%0\n%4\n\n#145[6]%0\n%4\n\n#146[7]%0\n%4\n\n#147[8]%0\n\
    %4\n\n#148[9]%0\n%4\n\n#149[10]%0\n%4\n\n#150[11]%0\n%4\n\n#151[12]%0\n%4\n#70%0%1#033%0\
    \ %1 %3#70%3\n\n#152[13]%0\n%40\n%41\n%42\n%43\n%44\n%45\n%46\n\n#68%0 %1\n#2<3>0[14]%0\
    \ %1 %2 %3\n%40\n%41\n%42\n%43\n#68%5\n\n#69%0 %1\n#2<4>0[15]%0 %1 %2 %3\n%40\n\
    %41\n#69%5\n\n#30%0\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\
    \n%4\n\n%4\n\n%4\n\n%4\n\n%4\n\n"
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
  - runtime:
        dependencies:
          - name: systemd
          - name: systemd
          - name: systemd
          - name: shadow-utils
  - buildtime:
        dependencies:
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

