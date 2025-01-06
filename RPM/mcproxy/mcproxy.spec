Name: mcproxy
Version: 1.1.1
Release: 1%{?dist}
Summary: Multicast Proxy for IGMP/MLD

License: GPL-2.0 License
URL: https://github.com/%{name}/%{name}
Source0: https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: (qt5-qtbase-devel or qt-devel)
#Requires:

%description
Multicast Proxy for IGMP/MLD

%global debug_package %{nil}

%prep
%setup -q

%build
cat > mcproxy.service <<EOF
[Unit]
Description=Multicast Proxy for IGMP/MLD
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/mcproxy -f /etc/mcproxy/mcproxy.conf

[Install]
WantedBy=multi-user.target
EOF
ls -l 
cd mcproxy/
qmake-qt4 || qmake-qt5
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 mcproxy/mcproxy $RPM_BUILD_ROOT/usr/bin/mcproxy
install -D -m 644 mcproxy/mcproxy.conf $RPM_BUILD_ROOT/etc/mcproxy/mcproxy.conf
install -D -m 644 mcproxy.service $RPM_BUILD_ROOT/usr/lib/systemd/system/mcproxy.service
#%pre
%post
systemctl daemon-reload

%files
%attr(0755, root, root) /usr/bin/mcproxy
%dir %attr(0755, root, root) /etc/mcproxy
%config(noreplace) %attr(0644, root, root) /etc/mcproxy/mcproxy.conf
%attr(0644, root, root) /usr/lib/systemd/system/mcproxy.service

#%changelog
