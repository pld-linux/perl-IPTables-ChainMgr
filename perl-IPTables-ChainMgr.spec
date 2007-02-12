#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPTables
%define		pnam	ChainMgr
Summary:	Perl interface to add and delete rules to an iptables chain
Summary(pl.UTF-8):	Perlowy interfejs do dodawania i usuwania reguł z łańcuchów iptables
Name:		perl-IPTables-ChainMgr
Version:	0.4
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cipherdyne.org/psad/download/psad-2.0.1.tar.gz
# Source0-md5:	a1604b68e31178e7e0cbbfd7c1cd4edf
URL:		http://www.cipherdyne.org/psad/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPTables-Parse
BuildRequires:	perl-Net-IPv4Addr
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to add and delete rules to an iptables chain. The most
common application of this module is to create a custom chain and then
add blocking rules to it. Rule additions are (mostly) guaranteed to be
unique.

%description -l pl.UTF-8
Perlowy interfejs do dodawania i usuwania reguł z łańcuchów iptables.
Najpopularniejszym zastosowaniem tego modułu jest tworzenie własnego
łańcucha, a następnie dodawanie do niego reguł blokujących. Dodawanie
reguł gwarantuje (w większości) ich unikalność.

%prep
%setup -q -n psad-2.0.1

%build
cd IPTables-ChainMgr
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C IPTables-ChainMgr pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc IPTables-ChainMgr/{Changes,README}
%{_mandir}/man3/IPTables::ChainMgr.3pm*
%{perl_vendorlib}/IPTables/ChainMgr.pm
