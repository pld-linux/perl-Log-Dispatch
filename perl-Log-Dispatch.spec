#
# Conditional build:
# _without_tests - do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch
Summary:	Log::Dispatch module - dispatches messages to multiple Log::Dispatch::* objects
Summary(pl):	Modu³ Log::Dispatch - wysy³aj±cy komunikaty do wielu obiektów Log::Dispatch::*
Name:		perl-%{pdir}-%{pnam}
Version:	2.06
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a7d6f11ceabca75587efa4c2251a134
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Params-Validate >= 0.15
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level. It is designed to be easily subclassed, both for creating a new
dispatcher object and particularly for creating new outputs.

%description -l pl
Log::Dispatch to zestaw obiektowo zorientowanych modu³ów do logowania
komunikatów na wiele wyj¶æ, z których ka¿de mo¿e mieæ podany minimalny
i maksymalny poziom logowania. Pakiet ten zosta³ zaprojektowany tak,
by ³atwo mo¿na by³o stworzyæ klasy potomne, w celu tworzenia nowych
obiektów wysy³aj±cych, jak i (szczególnie) nowych wyj¶æ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config="sitelib=%{perl_vendorlib} sitearch=%{perl_vendorarch}"
./Build

# man pages not yet supported by Module::Build :/
pod2man lib/Log/Dispatch.pm Log::Dispatch.3pm
for f in lib/Log/Dispatch/*.pm ; do
	pod2man $f Log::Dispatch::`basename $f .pm`.3pm
done
for f in lib/Log/Dispatch/Email/*.pm ; do
	pod2man $f Log::Dispatch::Email::`basename $f .pm`.3pm
done

%{!?_without_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man3
install *.3pm $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
