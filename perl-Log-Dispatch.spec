%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch
Summary:	Log::Dispatch module - dispatches messages to multiple Log::Dispatch::* objects
Summary(pl):	Modu³ Log::Dispatch - wysy³aj±cy komunikaty do wielu obiektów Log::Distatch::*
Name:		perl-%{pdir}-%{pnam}
Version:	2.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Dispatch is a suite of OO modules for logging messages to multiple
outputs, each of which can have a minimum and maximum log level.  It is
designed to be easily subclassed, both for creating a new dispatcher
object and particularly for creating new outputs.

%description -l pl
Log::Dispatch to zestaw obiektowo zorientowanych modu³ów do logowania
komunikatów na wiele wyj¶æ, z których ka¿de mo¿e mieæ podany minimalny
i maksymalny poziom logowania. Pakiet ten zosta³ zaprojektowany tak,
by ³atwo mo¿na by³o stworzyæ klasy potomne, w celu tworzenia nowych
obiektów wysy³aj±cych, jak i (szczególnie) nowych wyj¶æ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL < /dev/null
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
