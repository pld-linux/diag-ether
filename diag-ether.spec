Summary:	Diagnostic program for Ethernet adapters under Linux.
Summary(pl):	Programy diagnostyczne dla kart sieciowych.
Name:		diag-ether
# Version is last update date: yyyymmdd
Version:	20010318
Release:	1
Vendor:		Donald Becker <becker@scyld.com>
License:	GPL
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
# Manually packaged using sources at: ftp://www.scyld.com/pub/diag/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diagnostic and configuration programs for most common Ethernet adapters                             supported by Linux.

%description -l pl
Narzêdzia diagnostyczne i konfiguracyjne dla najbardziej popularnych
kart Ethernet pracuj±cych pod Linuxem.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-g -O0}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

for bin in *; do
	if [ -x $bin ]; then
		install $bin	$RPM_BUILD_ROOT%{_sbindir}
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html

%attr(755,root,root) %{_sbindir}/*
