Summary:	Diagnostic program for Ethernet adapters under Linux
Summary(pl):	Programy diagnostyczne dla kart sieciowych
Name:		diag-ether
# Version is last update date: yyyymmdd
Version:	20031219
Release:	1
Vendor:		Donald Becker <becker@scyld.com>
License:	GPL
Group:		Networking/Admin
# Manually packaged using sources at: ftp://www.scyld.com/pub/diag/
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	d583860be20e9efc20487ff416f1f8b6
Patch0:		%{name}-alta-diag.patch
Patch1:		%{name}-diag-example.patch
Patch2:		%{name}-eepro100-diag.patch
Patch3:		%{name}-mii-diag.patch
Patch4:		%{name}-natsemi-diag.patch
Patch5:		%{name}-ne2k-pci.patch
Patch6:		%{name}-ns820-diag.patch
Patch7:		%{name}-pci-config.patch
Patch8:		%{name}-pcnet-diag.patch
Patch9:		%{name}-rtl8139-diag.patch
Patch10:	%{name}-tulip-diag.patch
Patch11:	%{name}-winbond-diag.patch
Patch12:	%{name}-ether-wake.patch
Patch13:	%{name}-myson-diag.patch
Patch14:	%{name}-novia-diag.patch

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diagnostic and configuration programs for most common Ethernet
adapters supported by Linux.

%description -l pl
Narzêdzia diagnostyczne i konfiguracyjne dla najbardziej popularnych
kart Ethernet pracuj±cych pod Linuksem.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
# TODO: fix via-diag and remove patch14
%patch14 -p1

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
