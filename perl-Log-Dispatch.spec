%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch
Summary:	Log::Dispatch module - dispatches messages to multiple Log::Dispatch::* objects
Summary(pl):	Modu� Log::Dispatch - wysy�aj�cy komunikaty do wielu obiekt�w Log::Distatch::*
Name:		perl-%{pdir}-%{pnam}
Version:	2.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Dispatch is a suite of OO modules for logging messages to multiple
outputs, each of which can have a minimum and maximum log level.  It is
designed to be easily subclassed, both for creating a new dispatcher
object and particularly for creating new outputs.

%description -l pl
Log::Dispatch to zestaw obiektowo zorientowanych modu��w do logowania
komunikat�w na wiele wyj��, z kt�rych ka�de mo�e mie� podany minimalny
i maksymalny poziom logowania. Pakiet ten zosta� zaprojektowany tak,
by �atwo mo�na by�o stworzy� klasy potomne, w celu tworzenia nowych
obiekt�w wysy�aj�cych, jak i (szczeg�lnie) nowych wyj��.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
