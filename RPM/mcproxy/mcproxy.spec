Name: mcproxy
Version: 1.1.1
Release: 1%{?dist}
Summary: Multicast Proxy for IGMP/MLD

License: GPL-2.0 License
URL: https://github.com/mcproxy/mcproxy
Source0: https://github.com/mcproxy/mcproxy/archive/refs/tags/v1.1.1.tar.gz

BuildRequires: qt-devel

#Requires:

%description
Multicast Proxy for IGMP/MLD

%prep
%setup -q


%build
cd mcproxy/
qmake-qt4
make



%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc



%changelog
