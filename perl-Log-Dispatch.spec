#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch
Summary:	Log::Dispatch module - dispatches messages to multiple Log::Dispatch::* objects
Summary(pl):	Modu³ Log::Dispatch - wysy³aj±cy komunikaty do wielu obiektów Log::Dispatch::*
Name:		perl-%{pdir}-%{pnam}
Version:	2.08
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a8ca65b5e73c695d37a99967822f983c
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-Params-Validate >= 0.15
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(Apache::Log)' 'perl(MIME::Lite)' 'perl(Mail::Send)' 'perl(Mail::Sender)' 'perl(Mail::Sendmail)'

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
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
