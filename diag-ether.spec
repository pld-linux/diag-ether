Summary:	Diagnostic program for Ethernet adapters under Linux
Summary(pl):	Programy diagnostyczne dla kart sieciowych
Name:		diag-ether
# Version is last update date: yyyymmdd
Version:	20021228
Release:	1
Vendor:		Donald Becker <becker@scyld.com>
License:	GPL
Group:		Networking/Admin
# Manually packaged using sources at: ftp://www.scyld.com/pub/diag/
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	9725293e341f131b994df33ee9b48123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diagnostic and configuration programs for most common Ethernet
adapters supported by Linux.

%description -l pl
Narzêdzia diagnostyczne i konfiguracyjne dla najbardziej popularnych
kart Ethernet pracuj±cych pod Linuxem.

%prep
%setup -q -n %{name}

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
for bin in *; do
	if [ -x $bin ]; then
		install $bin	$RPM_BUILD_ROOT%{_sbindir}
	fi
done
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man8/*
